-- Напишете заявка, която извежда средната скорост на компютрите
SELECT AVG(speed) AS 'Average speed' 
    FROM pc;

-- Напишете заявка, която извежда средния размер на екраните на лаптопите за всеки производител.
SELECT p.maker AS 'Maker', AVG(screen) AS 'Average screen'
    FROM laptop l 
    JOIN product p 
        ON p.model = l.model 
    GROUP BY p.maker;

-- Напишете заявка, която извежда средната скорост на лаптопите с цена над 1000.
SELECT AVG(SPEED) AS 'Average speed' 
    FROM laptop 
    WHERE price > 1000;

-- Напишете заявка, която извежда средната цена на компютрите според различните им hd.
SELECT hd AS 'HD', AVG(price) AS 'Average price' 
    FROM pc 
    GROUP BY hd;

-- Напишете заявка, която извежда средната цена на компютрите за всяка скорост по-голяма от 500.
SELECT AVG(price) AS 'Average price' 
    FROM pc 
    WHERE speed > 500;

-- Напишете заявка, която извежда средната цена на компютрите произведени от производител ‘A’.
SELECT AVG(p.price) AS 'Average price' 
    FROM pc p 
    JOIN product pr 
        ON p.model=pr.model 
    WHERE pr.maker='A'; 

-- Напишете заявка, която извежда средната цена на компютрите и лаптопите за производител ‘B’
SELECT AVG(price) AS 'Average price'
    FROM (SELECT p.price   
            FROM pc p  
            JOIN product pr  
                ON p.model=pr.model  
            WHERE pr.maker='B'  
          UNION ALL 
          SELECT l.price  
            FROM laptop l  
            JOIN product pr 
                ON l.model=pr.model 
            WHERE pr.maker='B') AS price;   

-- Напишете заявка, която извежда производителите, които са произвели поне по 3 различни модела компютъра. 
-- v1
 SELECT DISTINCT p1.maker AS 'Maker'
    FROM product p1 
    JOIN product p2 
        ON p2.type='PC' and p1.maker=p2.maker and p1.model != p2.model 
    JOIN product p3 
        ON p3.type='PC' and p3.maker=p1.maker and p3.model != p2.model and p3.model != p1.model
    WHERE p1.type='PC';

-- v2
SELECT maker AS 'Maker'
    FROM product 
    WHERE type='PC' 
    GROUP BY maker
    HAVING COUNT(model) >= 3;

-- Помислете каква заявка можете да напишете, за да сте сигурни в отговора, 
-- например, да изведете за всеки производител броя различни модели компютри.
SELECT maker AS 'Maker', COUNT(model) AS 'Count of different PC models'
    FROM product 
    WHERE type='PC' 
    GROUP BY maker;  

-- Напишете заявка, която извежда производителите на компютрите с най-висока цена.
SELECT DISTINCT maker AS 'Maker'
    FROM product 
    WHERE model IN (SELECT model 
                        FROM pc
                        WHERE price=(SELECT MAX(price) 
                                        FROM pc));

-- Напишете заявка, която извежда средния размер на диска на тези компютри 
-- произведени от производители, които произвеждат и принтери.
-- v1
SELECT AVG(hd) AS 'Average HD'
    FROM pc
    WHERE model in (SELECT DISTINCT p1.model 
                        FROM product p1
                        JOIN product p2 
                            ON p1.maker = p2.maker
                        WHERE p1.type='PC' AND p2.type='Printer');
-- v2
SELECT AVG(hd) AS 'Average HD'
    FROM product pr
    JOIN pc p 
        ON p.model=pr.model
    WHERE pr.maker IN (SELECT maker
                            FROM product
                            WHERE type='Printer');
