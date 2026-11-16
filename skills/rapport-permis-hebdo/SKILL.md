---
name: rapport-permis-hebdo
description: Rédige le rapport hebdomadaire des permis délivrés à la Ville de Québec à partir des fichiers d'indicateurs CSV du projet. À utiliser quand on demande une synthèse, un rapport, des KPI ou un bilan sur les permis de la Ville de Québec.
---

# Rapport hebdomadaire des permis – Ville de Québec

## Données attendues
- `permis_par_mois.csv` : colonnes `mois`, `nb_permis`
- `variation_mensuelle.csv` : colonnes `mois`, `nb_permis`, `nb_mois_precedent`, `variation_pct`
- `permis_par_type.csv` : colonnes `type_permis`, `nb_permis`, `part_pct`
- `permis_par_arrondissement_annee.csv` : colonnes `arrondissement`, `annee`, `nb_permis`

Si un fichier manque, le dire et ne rédiger que ce qui est possible.

## Étapes
1. Vérifier que les fichiers sont présents et que les colonnes correspondent.
2. Repérer le dernier mois complet. Le dernier mois des fichiers est considéré comme incomplet : ne jamais le comparer à un mois complet.
3. Comparer le dernier mois complet au même mois de l'année précédente.
4. Rédiger le rapport en suivant exactement le format ci-dessous.

## Format du rapport (sections fixes, dans cet ordre, sans en ajouter)
1. **Titre** : « Permis délivrés – [dernier mois complet] » (exemple : « Permis délivrés – octobre 2026 »). Ne pas inventer de date de semaine.
2. **En bref** : 3 phrases au maximum, chacune avec un chiffre.
3. **Indicateurs clés** : un tableau de 4 lignes exactement :
   - total du dernier mois complet ;
   - variation par rapport au même mois de l'année précédente ;
   - type dominant (préciser la période couverte par le fichier) ;
   - arrondissement le plus actif depuis le début de l'année.
4. **À surveiller** : une alerte seulement si la variation sur un an dépasse 30 %, en plus ou en moins. Sinon, écrire « Aucune alerte. »
5. **Notes sur les données** : 3 puces au maximum (mois incomplet, limites des fichiers).
6. **Source** : Ville de Québec, Données Québec (CC-BY 4.0), avec la période couverte.

## Règles
- Ne jamais inventer un chiffre : chaque nombre doit venir d'un fichier fourni.
- Ne jamais expliquer une variation (saison, cause, contexte) si les fichiers ne le démontrent pas. Décrire les chiffres, sans les interpréter.
- Signaler les valeurs manquantes au lieu de les deviner.
- Ne jamais citer d'adresse : résultats par arrondissement uniquement.
- Écrire en français, phrases courtes, ton neutre : pas de « je », pas de tutoiement.