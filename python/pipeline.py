"""Pipeline des permis de la Ville de Québec.

Lit le CSV brut, recharge la base SQLite, recrée la table nettoyée
et exporte les indicateurs en CSV. Peut être relancé sans dupliquer les données.
"""
import argparse
import sqlite3
import urllib.request
from datetime import date
from pathlib import Path

import pandas as pd

INDICATEURS = {
    "permis_par_mois": """
        SELECT mois, COUNT(*) AS nb_permis
        FROM permis GROUP BY mois ORDER BY mois
    """,
    "permis_par_type": """
        SELECT COALESCE(type_permis, 'Type non précisé') AS type_permis,
               COUNT(*) AS nb_permis,
               ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM permis), 1) AS part_pct
        FROM permis GROUP BY type_permis ORDER BY nb_permis DESC
    """,
    "permis_par_domaine": """
        SELECT domaine, COUNT(*) AS nb_permis
        FROM permis GROUP BY domaine ORDER BY nb_permis DESC
    """,
    "permis_par_arrondissement_annee": """
        SELECT arrondissement, annee, COUNT(*) AS nb_permis
        FROM permis GROUP BY arrondissement, annee ORDER BY arrondissement, annee
    """,
    "variation_mensuelle": """
        SELECT mois, nb_permis,
               LAG(nb_permis) OVER (ORDER BY mois) AS nb_mois_precedent,
               ROUND(100.0 * (nb_permis - LAG(nb_permis) OVER (ORDER BY mois))
                     / LAG(nb_permis) OVER (ORDER BY mois), 1) AS variation_pct
        FROM (SELECT mois, COUNT(*) AS nb_permis FROM permis GROUP BY mois)
        ORDER BY mois
    """,
}


def main():
    parser = argparse.ArgumentParser(description="Pipeline des permis de la Ville de Québec")
    parser.add_argument("--projet", default=Path(__file__).resolve().parents[1],
                        help="Dossier racine du projet")
    parser.add_argument("--url", default=None,
                        help="Adresse du CSV à télécharger (sinon, dernier fichier de data/raw)")
    args = parser.parse_args()

    projet = Path(args.projet)
    raw = projet / "data" / "raw"
    clean = projet / "data" / "clean"

    # 1. Trouver ou télécharger le fichier brut
    if args.url:
        fichier = raw / f"permis_{date.today():%Y-%m-%d}.csv"
        urllib.request.urlretrieve(args.url, fichier)
    else:
        fichier = max(raw.glob("*.csv"), key=lambda f: f.stat().st_mtime)
    print("Fichier brut :", fichier.name)

    # 2. Charger dans la base (remplace la table, donc aucun doublon au second passage)
    df = pd.read_csv(fichier, low_memory=False)
    connexion = sqlite3.connect(clean / "permis.db")
    df.to_sql("permis_raw", connexion, if_exists="replace", index=False)

    # 3. Recréer la table nettoyée avec le script SQL du projet
    script = (projet / "sql" / "01_create_tables.sql").read_text(encoding="utf-8")
    connexion.executescript(script)
    nb_lignes = connexion.execute("SELECT COUNT(*) FROM permis").fetchone()[0]
    print("Lignes brutes :", len(df), "- Lignes nettoyées :", nb_lignes)

    # 4. Exporter les indicateurs
    for nom, requete in INDICATEURS.items():
        pd.read_sql(requete, connexion).to_csv(
            clean / f"{nom}.csv", index=False, encoding="utf-8-sig")
        print("Indicateur exporté :", nom)

    connexion.commit()
    connexion.close()
    print("Pipeline terminé.")


if __name__ == "__main__":
    main()