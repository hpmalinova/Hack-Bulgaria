-- Напишете заявка, която за всеки кораб извежда името му, 
-- държавата, броя оръдия и годината на пускане (launched).
SELECT s.name AS 'Ship name', c.country, c.numguns, s.launched 
    FROM ships s 
    JOIN classes c 
        ON c.class=s.class;  

-- Повторете горната заявка като този път включите в резултата и класовете, 
-- които нямат кораби, но съществуват кораби със същото име като тяхното.


-- Напишете заявка, която извежда имената на корабите, участвали в битка от 1942г.
SELECT ship AS 'Ship name' 
    FROM OUTCOMES o
    JOIN BATTLES b
        ON o.battle=b.name
    WHERE strftime('%Y', b.date) 
        IN ('1942');

-- За всяка страна изведете имената на корабите, които никога не са участвали в битка.
SELECT c.country, s.name
    FROM classes c
    JOIN ships s on c.class=s.class
    WHERE s.name in (SELECT s.name
                        FROM ships s
                        WHERE s.name 
                            NOT IN (SELECT ship 
                                        FROM OUTCOMES))
    ORDER BY c.country, s.name;