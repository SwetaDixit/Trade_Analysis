-- Monthly, quarterly, and yearly volume for items that have 10 million+ in volume over the past year?

SELECT 
    YEAR(`Candle Close Time`) AS Year,
    QUARTER(`Candle Close Time`) AS Quarter,
    MONTH(`Candle Close Time`) AS Month,
    SUM(`USD Volume`) AS Monthly_Volume
FROM 
    btc
WHERE 
    `Candle Close Time` >= DATE_SUB(NOW(), INTERVAL 1 YEAR)
GROUP BY 
    YEAR(`Candle Close Time`), QUARTER(`Candle Close Time`), MONTH(`Candle Close Time`)
HAVING 
    SUM(`USD Volume`) >= 10000000;
