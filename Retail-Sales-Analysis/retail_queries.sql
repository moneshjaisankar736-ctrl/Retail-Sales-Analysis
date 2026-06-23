SELECT SUM(Sales) AS Total_Sales
FROM RetailSales;

SELECT SUM(Profit) AS Total_Profit
FROM RetailSales;

SELECT Category, SUM(Sales) AS Sales
FROM RetailSales
GROUP BY Category;

SELECT Region, SUM(Sales) AS Sales
FROM RetailSales
GROUP BY Region;

SELECT Product, SUM(Sales) AS Sales
FROM RetailSales
GROUP BY Product
ORDER BY Sales DESC;