----Une anomalie à noter---

La Ville de Québec compte six arrondissements. Or la colonne en contient trois autres valeurs : 
Saint-Augustin-de-Desmaures (18), L’Ancienne-Lorette (7) et Wendake (1). 
Ce ne sont pas des arrondissements, mais des territoires voisins. 
Ces 26 lignes ne sont pas des erreurs à supprimer : à la phase 3, vous les regrouperez sous une étiquette comme « Hors arrondissements » et vous l’écrirez dans vos notes.

Les trois questions métier, confirmées

#	Question	                                                                                          Colonnes utilisées

1	Combien de permis sont délivrés chaque mois depuis 2020, et y a-t-il une saisonnalité ?	                     DATE_DELIVRANCE
2	Quels types et domaines dominent, et comment se répartissent-ils entre les six arrondissements ?	TYPE_PERMIS, DOMAINE, ARRONDISSEMENT
3	La dernière semaine est-elle normale ou inhabituelle par rapport à la moyenne ?	                             DATE_DELIVRANCE


## Doublons découverts à la phase 2

Le fichier brut contient 71 612 lignes, dont 2 303 sont des copies exactes
d'une autre ligne (2 216 numéros de permis répétés, jusqu'à 4 fois).
Vérification : toutes les colonnes sont identiques, aucune information n'est perdue.
Décision : les copies sont retirées dans la table "permis" (SELECT DISTINCT).
La table nettoyée compte 69 309 lignes : 69 306 permis numérotés et 3 sans numéro.
La table "permis_raw" reste intacte.