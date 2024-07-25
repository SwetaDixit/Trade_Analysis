-- What is the volume for a given timeframe?

SELECT 
    SUM(`USD Volume`) AS Total_Volume
FROM 
    btc
WHERE 
    `Candle Close Time` BETWEEN '2024-05-05 00:00:00' AND '2024-05-06 23:59:59';


