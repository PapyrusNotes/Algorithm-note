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
-- 임시 테이블 개념 복습
WITH RECURSIVE TMP AS(
    SELECT 0 AS NUM
    UNION ALL
    SELECT NUM+1 FROM TMP
    WHERE NUM<23
)

SELECT TMP.NUM AS HOUR, COUNT(ANIMAL_OUTS.ANIMAL_ID) AS COUNT
FROM TMP
LEFT JOIN ANIMAL_OUTS
ON TMP.NUM = HOUR(ANIMAL_OUTS.DATETIME)
GROUP BY HOUR
ORDER BY HOUR ASC