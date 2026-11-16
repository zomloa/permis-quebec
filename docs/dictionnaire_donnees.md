# Dictionnaire de données – Permis délivrés à la Ville de Québec

Fichier : data/raw/permis_2026-11-15.csv
Taille : 71 612 lignes, 10 colonnes

| Colonne | Type | Exemple | Signification | Manquantes |
|---|---|---|---|---|
| NUMERO_PERMIS | texte | 20261021-016D | Identifiant du permis. Le préfixe ressemble à une date (demande ?) : à confirmer | 3 |
| DATE_DELIVRANCE | texte (date AAAA-MM-JJ) | 2026-10-23 | Date de délivrance du permis | 0 |
| ADRESSE_TRAVAUX | texte | 391 Rue Audouart Québec Québec G1C6M2 | Adresse des travaux. Ne pas publier en liste | 0 |
| DOMAINE | texte | Aménagement extérieur | Domaine de l'intervention | 0 |
| LOTS_IMPACTES | texte | 1 474 358 | Numéro(s) de lot cadastral concerné(s) | 178 |
| TYPE_PERMIS | texte | Certificat d'autorisation | Type de permis émis | 8 |
| ARRONDISSEMENT | texte | Beauport | Arrondissement où ont lieu les travaux | 0 |
| RAISON | texte | Abattage d'arbre | Motif précis des travaux | 6 |
| LONGITUDE | nombre décimal | -71.191655 | Coordonnée géographique | 0 |
| LATITUDE | nombre décimal | 46.883927 | Coordonnée géographique | 0 |

## Points à confirmer
- Sens du préfixe de NUMERO_PERMIS et de la lettre finale (D).
- Liste des valeurs distinctes de DOMAINE, TYPE_PERMIS et ARRONDISSEMENT.
- Plage des dates (première et dernière délivrance).