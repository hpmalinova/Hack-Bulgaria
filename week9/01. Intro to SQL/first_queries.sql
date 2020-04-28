-- Напишете заявка, която извежда адреса на студио ‘MGM’
SELECT address 
    FROM STUDIO
    WHERE name = 'MGM';

-- Напишете заявка, която извежда рождената дата на актрисата Kim Basinger
SELECT birthdate
    FROM MOVIESTAR
    WHERE name = 'Kim Basinger';

-- Напишете заявка, която извежда имената на всички продуценти на филми 
-- с нетни активи (networth) над 10 000 000 долара
SELECT name
    FROM MOVIEEXEC
    WHERE networth > 10000000;

-- Напишете заявка, която извежда имената на всички актьори, 
-- които са мъже или живеят на Prefect Rd.
SELECT name 
    FROM MOVIESTAR
    WHERE gender = 'M' OR address = 'Prefect Rd.';

-- Добавате нова филмова звезда 'Zahari Baharov', 
-- с адрес и рожденна дата по ваш избор.
INSERT INTO MOVIESTAR
    VALUES ('Zahari Baharov', 'Sofia, ul. Neznaina 22', 'M', '1980-08-12');

-- Изтрийте всички студия, които имат в адреса си числото 5.
DELETE FROM STUDIO
    WHERE address LIKE '%5%';

-- Променете студио да бъде "Fox" на тези филми, които в имената си имат 'star.
UPDATE MOVIE
    SET studioname = 'Fox'
    WHERE title LIKE '%star%';