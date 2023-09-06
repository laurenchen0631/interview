SELECT 
    'bull' as word,
    SUM(content LIKE '% bull %') AS count
FROM Files

UNION 

SELECT 
    'bear' as word,
    SUM(content LIKE '% bear %') AS count
FROM Files
