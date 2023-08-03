SELECT 
    CONCAT(c.first_name, " ", c.last_name) AS customer,
    t.fails AS failures
FROM (
    SELECT 
        cus.id AS id,
        COUNT(*) AS fails
    FROM customers cus
    JOIN campaigns cam
        ON cus.id = cam.customer_id
    JOIN events e
        ON cam.id = e.campaign_id AND e.status = "failure"
    GROUP BY cus.id
    HAVING COUNT(*) > 3
) AS t
JOIN customers c ON t.id = c.id;