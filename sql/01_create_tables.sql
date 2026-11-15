-- Crée la table nettoyée "permis" à partir de la table brute "permis_raw".

DROP TABLE IF EXISTS permis;

CREATE TABLE permis AS
SELECT DISTINCT
    NUMERO_PERMIS                          AS numero_permis,
    DATE(DATE_DELIVRANCE)                  AS date_delivrance,
    STRFTIME('%Y', DATE_DELIVRANCE)        AS annee,
    STRFTIME('%Y-%m', DATE_DELIVRANCE)     AS mois,
    TRIM(TYPE_PERMIS)                      AS type_permis,
    TRIM(DOMAINE)                          AS domaine,
    TRIM(RAISON)                           AS raison,
    CASE
        WHEN ARRONDISSEMENT LIKE 'Saint-Augustin%'   THEN 'Hors arrondissements'
        WHEN ARRONDISSEMENT LIKE '%Ancienne-Lorette' THEN 'Hors arrondissements'
        WHEN ARRONDISSEMENT = 'Wendake'              THEN 'Hors arrondissements'
        ELSE TRIM(ARRONDISSEMENT)
    END                                    AS arrondissement,
    ADRESSE_TRAVAUX                        AS adresse_travaux,
    LOTS_IMPACTES                          AS lots_impactes,
    LONGITUDE                              AS longitude,
    LATITUDE                               AS latitude
FROM permis_raw;