CREATE TEMP TABLE TmpTbl
(
    section_no numeric(9,0) NOT NULL,
    user_tgt_cd varying(2) NOT NULL,
    section_nm character varying(1000) NULL
);

INSERT INTO TmpTbl
SELECT
CASE
FROM

