"""Serveur MCP en lecture seule sur la base des permis de la Ville de Québec."""
import sqlite3
from pathlib import Path

from mcp.server.mcpserver import MCPServer

BASE = Path(__file__).resolve().parents[1] / "data" / "clean" / "permis.db"
LIGNES_MAX = 200

mcp = MCPServer("permis-quebec")


def connexion():
    """Ouvre la base en lecture seule : aucune modification n'est possible."""
    con = sqlite3.connect(f"file:{BASE.as_posix()}?mode=ro", uri=True)
    con.execute("PRAGMA query_only = ON")
    return con


@mcp.tool()
def lister_tables() -> list[str]:
    """Liste les tables de la base des permis."""
    con = connexion()
    tables = [r[0] for r in con.execute(
        "SELECT name FROM sqlite_master WHERE type = 'table' ORDER BY name")]
    con.close()
    return tables


@mcp.tool()
def decrire_table(table: str) -> list[dict]:
    """Donne le nom et le type de chaque colonne d'une table."""
    if table not in lister_tables():
        raise ValueError(f"Table inconnue : {table}")
    con = connexion()
    colonnes = [{"colonne": r[1], "type": r[2]}
                for r in con.execute(f'PRAGMA table_info("{table}")')]
    con.close()
    return colonnes


@mcp.tool()
def executer_requete(sql: str) -> list[dict]:
    """Exécute une requête SELECT en lecture seule et renvoie au plus 200 lignes."""
    if not sql.strip().lower().startswith(("select", "with")):
        raise ValueError("Seules les requêtes SELECT sont autorisées.")
    con = connexion()
    curseur = con.execute(sql)
    noms = [c[0] for c in curseur.description]
    lignes = [dict(zip(noms, ligne)) for ligne in curseur.fetchmany(LIGNES_MAX)]
    con.close()
    return lignes


if __name__ == "__main__":
    mcp.run()