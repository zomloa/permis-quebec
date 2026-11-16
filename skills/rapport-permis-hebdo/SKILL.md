---
name: rapport-permis-hebdo
description: Rédige le rapport hebdomadaire des permis délivrés à la Ville de Québec, à partir de la base des permis (serveur MCP permis-quebec) ou des fichiers d'indicateurs CSV du projet. À utiliser quand on demande une synthèse, un rapport, des KPI ou un bilan sur les permis de la Ville de Québec.
---

# Rapport hebdomadaire des permis – Ville de Québec

## Source des chiffres (par ordre de priorité)

### 1. La base des permis, si le serveur MCP `permis-quebec` est disponible
Si les outils `lister_tables` et `executer_requete` du serveur `permis-quebec` sont accessibles, calculer tous les indicateurs par requête SQL sur la table `permis`, plutôt qu'à partir des fichiers.

Colonnes utiles de la table `permis` : `date_delivrance` (AAAA-MM-JJ), `mois` (texte AAAA-MM), `annee` (texte AAAA), `type_permis`, `arrondissement`.

Requêtes de référence (remplacer `AAAA-MM` par le dernier mois complet, `AAAA-1-MM` par le même mois un an avant, `AAAA` par l'année en cours) :
- Période couverte : `SELECT MIN(date_delivrance), MAX(date_delivrance), COUNT(*) FROM permis`
- Total d'un mois : `SELECT COUNT(*) FROM permis WHERE mois = 'AAAA-MM'`
- Type dominant du mois : `SELECT COALESCE(type_permis, 'Type non précisé') AS type_permis, COUNT(*) AS nb FROM permis WHERE mois = 'AAAA-MM' GROUP BY type_permis ORDER BY nb DESC`
- Arrondissements depuis janvier : `SELECT arrondissement, COUNT(*) AS nb FROM permis WHERE annee = 'AAAA' AND mois <= 'AAAA-MM' GROUP BY arrondissement ORDER BY nb DESC`

La base est en lecture seule : n'envoyer que des requêtes SELECT.

### 2. Sinon, les fichiers CSV joints
- `permis_par_mois.csv` : colonnes `mois`, `nb_permis`
- `variation_mensuelle.csv` : colonnes `mois`, `nb_permis`, `nb_mois_precedent`, `variation_pct`
- `permis_par_type.csv` : colonnes `type_permis`, `nb_permis`, `part_pct`
- `permis_par_arrondissement_annee.csv` : colonnes `arrondissement`, `annee`, `nb_permis`

Si un fichier manque, le dire et ne rédiger que ce qui est possible.

## Étapes
1. Choisir la source des chiffres (base en priorité, sinon fichiers) et vérifier qu'elle est complète.
2. Repérer le dernier mois complet. Le dernier mois présent dans les données est considéré comme incomplet : ne jamais le comparer à un mois complet.
3. Comparer le dernier mois complet au même mois de l'année précédente.
4. Rédiger le rapport en suivant exactement le format ci-dessous.

## Format du rapport (sections fixes, dans cet ordre, sans en ajouter)
1. **Titre** : « Permis délivrés – [dernier mois complet] » (exemple : « Permis délivrés – octobre 2026 »). Ne pas inventer de date de semaine.
2. **En bref** : 3 phrases au maximum, chacune avec un chiffre.
3. **Indicateurs clés** : un tableau de 4 lignes exactement :
   - total du dernier mois complet ;
   - variation par rapport au même mois de l'année précédente ;
   - type dominant : pour le dernier mois complet avec la base ; sur toute la période du fichier avec les CSV (le préciser) ;
   - arrondissement le plus actif depuis janvier : jusqu'au dernier mois complet avec la base ; année en cours entière avec les CSV (le préciser).
4. **À surveiller** : une alerte seulement si la variation sur un an dépasse 30 %, en plus ou en moins. Sinon, écrire « Aucune alerte. »
5. **Notes sur les données** : 3 puces au maximum (mois incomplet, source utilisée, limites).
6. **Source** : Ville de Québec, Données Québec (CC-BY 4.0), avec la période couverte.

## Règles
- Ne jamais inventer un chiffre : chaque nombre doit venir d'une requête sur la base ou d'un fichier fourni.
- Ne jamais modifier la base : lecture seule.
- Ne jamais expliquer une variation (saison, cause, contexte) si les données ne le démontrent pas. Décrire les chiffres, sans les interpréter.
- Signaler les valeurs manquantes au lieu de les deviner.
- Ne jamais citer d'adresse : résultats par arrondissement uniquement.
- Écrire en français, phrases courtes, ton neutre : pas de « je », pas de tutoiement.
