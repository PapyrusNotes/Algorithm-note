----------------------
-- Written in MySQL --
----------------------

-------------------------------------------------------------------------------
-- SELECT QUERY ---------------------------------------------------------------
-------------------------------------------------------------------------------
-- https://programmers.co.kr/learn/courses/30/lessons/59034
SELECT *
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC

-- https://programmers.co.kr/learn/courses/30/lessons/59035
SELECT NAME, DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC

-- https://programmers.co.kr/learn/courses/30/lessons/59036
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'

-- https://programmers.co.kr/learn/courses/30/lessons/59037
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged'

-- https://programmers.co.kr/learn/courses/30/lessons/59403
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC

-- https://programmers.co.kr/learn/courses/30/lessons/59404
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME ASC, DATETIME DESC
-- 원리 조사하기

-- https://programmers.co.kr/learn/courses/30/lessons/59405
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME ASC
LIMIT 1
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------


-------------------------------------------------------------------------------
--SUM, MAX, MIN QUERY ---------------------------------------------------------
-------------------------------------------------------------------------------
-- https://programmers.co.kr/learn/courses/30/lessons/59415
SELECT MAX(DATETIME)
FROM ANIMAL_INS

-- https://programmers.co.kr/learn/courses/30/lessons/59038
SELECT MIN(DATETIME)
FROM ANIMAL_INS

-- https://programmers.co.kr/learn/courses/30/lessons/59406
SELECT COUNT(ANIMAL_ID) count
FROM ANIMAL_INS

-- https://programmers.co.kr/learn/courses/30/lessons/59408
SELECT COUNT (DISTINCT NAME) count
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------


-------------------------------------------------------------------------------
-- GROUP_BY QUERY -------------------------------------------------------------
-------------------------------------------------------------------------------
-- https://programmers.co.kr/learn/courses/30/lessons/59040
SELECT ANIMAL_TYPE, COUNT (*) count
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
HAVING ANIMAL_TYPE IN ('Cat','Dog')
ORDER BY ANIMAL_TYPE ASC

-- https://programmers.co.kr/learn/courses/30/lessons/59041
SELECT NAME, COUNT (*) count
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(NAME) >= 2
ORDER BY NAME

-- https://programmers.co.kr/learn/courses/30/lessons/59412
SELECT OPEN_HOUR as HOUR, COUNT (*) as COUNT
FROM (
SELECT HOUR(DATETIME) AS OPEN_HOUR
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) BETWEEN 9 AND 20
) AS DAY_RECORD
GROUP BY OPEN_HOUR
ORDER BY OPEN_HOUR ASC -- 복습

-- https://programmers.co.kr/learn/courses/30/lessons/59413
-- 코드를 입력하세요
/*SELECT OPEN_HOUR as HOUR, COUNT (*) as COUNT
FROM (
SELECT HOUR(DATETIME) AS OPEN_HOUR
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) BETWEEN 0 AND 23
) AS DAY_RECORD
GROUP BY OPEN_HOUR
ORDER BY OPEN_HOUR ASC*/
CREATE TABLE OUT_FREQ(HOUR INT PRIMARY KEY, COUNT INT);

SELECT HOUR(DATETIME) AS OPEN_HOUR
FROM ANIMAL_OUTS
GROUP BY HOUR(DATETIME)
ORDER BY OPEN_HOUR

DECLARE h INT DEFAULT 0;
WHILE (h < 24) DO
    IF h not in OPEN_HOUR
        INSERT INTO OUT_FREQ VALUES(h,0)
    ELSE
        INSERT INTO OUT_FREQ VALUES(h,)