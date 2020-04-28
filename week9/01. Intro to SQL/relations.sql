-- Напишете заявка, която извежда имената на 
-- актьорите мъже участвали в ‘Terms of Endearment’
SELECT DISTINCT m.name
    FROM MOVIESTAR m
    JOIN STARSIN s 
        ON m.name = s.starname
    where m.gender = 'M' AND s.movietitle = 'Terms of Endearment';

-- Напишете заявка, която извежда имената на актьорите,
-- участвали във филми, продуцирани от ‘MGM’през 1995 г.
SELECT s.starname
    FROM STARSIN s
    JOIN MOVIE m
        ON s.movietitle = m.title
    WHERE m.year = 1995 AND m.studioname = 'MGM';

-- Добавете колона "име на президент" на таблицата Студио
-- и съответно и задайте стойности.
-- Напишете заявка, която извежда името на президента на ‘MGM’
ALTER TABLE STUDIO
ADD COLUMN president_name VARCHAR(30);

UPDATE STUDIO
    SET president_name = 'MGM Beast'
    WHERE name = 'MGM';
    
UPDATE STUDIO
    SET president_name = 'USA Beast'
    WHERE name = 'USA Entertainm.';
    
SELECT president_name
    FROM STUDIO
    WHERE name = 'MGM'

