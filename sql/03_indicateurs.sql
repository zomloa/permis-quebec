-- Combien de permis sont délivrés chaque mois ?
SELECT
    mois,
    COUNT(*) AS nb_permis
FROM permis
GROUP BY mois
ORDER BY mois;


-- Quels types de permis dominent, et quelle part du total représentent-ils ?
SELECT
    COALESCE(type_permis, 'Type non précisé') AS type_permis,
    COUNT(*) AS nb_permis,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM permis), 1) AS part_pct
FROM permis
GROUP BY type_permis
ORDER BY nb_permis DESC;

-- Comment les permis se répartissent-ils entre les arrondissements, année par année ?
SELECT
    arrondissement,
    annee,
    COUNT(*) AS nb_permis
FROM permis
GROUP BY arrondissement, annee
ORDER BY arrondissement, annee;


-- De combien le nombre de permis varie-t-il d'un mois à l'autre ?
SELECT
    mois,
    nb_permis,
    LAG(nb_permis) OVER (ORDER BY mois) AS nb_mois_precedent,
    ROUND(
        100.0 * (nb_permis - LAG(nb_permis) OVER (ORDER BY mois))
        / LAG(nb_permis) OVER (ORDER BY mois), 1
    ) AS variation_pct
FROM (
    SELECT mois, COUNT(*) AS nb_permis
    FROM permis
    GROUP BY mois
)
ORDER BY mois;