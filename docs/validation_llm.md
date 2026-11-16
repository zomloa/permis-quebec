| Fais-moi le rapport hebdomadaire des permis | Oui | Oui, 5 sur 5 | Mois incomplet bien écarté ; date de la semaine déduite, absente des fichiers |

Aucun écart sur les chiffres.
Limites constatées : pas de répartition par type pour un mois donné ; date d'extraction absente des fichiers.

| Quels sont les KPI des permis... | Oui | Oui, 11 sur 11 | Section arrondissements ajoutée hors format ; date du titre différente du 1er essai ; « baisse normale à l'automne » non prouvée (fausse en 2024) |

## Version 2 du skill (après correction)

Corrections : titre fondé sur le mois, 6 sections fixes, tableau de 4 lignes,
interdiction d'expliquer une variation sans preuve, ton neutre.

| Formulation | Skill déclenché ? | Chiffres justes ? | Format respecté ? |
|---|---|---|---|
| Résume l'activité des permis | Oui | Oui | Oui, 6 sections sur 6 |

Conclusion : le skill est fiable sur le déclenchement, les chiffres et le format.
## Version 3 du skill : accès direct à la base par MCP

Test du 16 novembre 2026 : rapport produit en interrogeant `permis.db` par le serveur MCP `permis-quebec`, sans fichier CSV.

| Indicateur | Avec les CSV (v2) | Avec la base (MCP) |
|---|---|---|
| Total d'octobre 2026 | 990 | 990 |
| Variation sur un an | −14,1 % | −14,1 % |
| Type dominant | 61,6 %, toute la période 2020-2026 | 65,1 %, octobre 2026 seul |
| Arrondissement le plus actif | 2 468, novembre partiel inclus | 2 369, de janvier à octobre 2026 |

Constat : le skill était écrit pour les fichiers CSV. L'accès SQL corrige les deux limites relevées en v2.
Correction (v3) : la base devient la source prioritaire, avec des requêtes de référence ; les CSV restent la solution de repli.
