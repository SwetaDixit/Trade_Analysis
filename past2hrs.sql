-- What is the high/low price/volume in the past 2 hours?

SELECT 
    MAX(`High Price`) AS High_Price_2_Hours,
    MIN(`Low Price`) AS Low_Price_2_Hours,
    SUM(`USD Volume`) AS Total_Volume_2_Hours
FROM 
    btc
WHERE 
    `Candle Close Time` >= DATE_SUB('2024-05-06 7:00:00', INTERVAL 2 HOUR);

