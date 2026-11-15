-- Contrôle 1 : combien de lignes contient la table ?
SELECT COUNT(*) AS nb_lignes
FROM permis;

-- Contrôle 2 : combien de numéros de permis apparaissent plus d'une fois ?
SELECT COUNT(*) AS nb_numeros_en_double
FROM (
    SELECT numero_permis
    FROM permis
    WHERE numero_permis IS NOT NULL
    GROUP BY numero_permis
    HAVING COUNT(*) > 1
);

-- Contrôle 3 : y a-t-il des dates manquantes ou dans le futur ?
SELECT
    SUM(date_delivrance IS NULL)        AS dates_manquantes,
    SUM(date_delivrance > DATE('now'))  AS dates_futures,
    MIN(date_delivrance)                AS premiere_date,
    MAX(date_delivrance)                AS derniere_date
FROM permis;

-- Contrôle 4 : combien de valeurs vides par colonne ?
SELECT
    SUM(numero_permis IS NULL)  AS sans_numero,
    SUM(type_permis IS NULL)    AS sans_type,
    SUM(raison IS NULL)         AS sans_raison,
    SUM(lots_impactes IS NULL)  AS sans_lot
FROM permis;