--- What is the 52 week high and low for all the items traded in the past 3 months?

SELECT 
    MAX(`High Price`) AS Fifty_Two_Week_High,
    MIN(`Low Price`) AS Fifty_Two_Week_Low
FROM 
    btc
WHERE 
    `Candle Close Time` >= DATE_SUB(NOW(), INTERVAL 3 MONTH);


