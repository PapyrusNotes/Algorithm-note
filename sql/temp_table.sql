CREATE TEMP TABLE TmpTbl
(
    section_no numeric(9,0) NOT NULL,
    user_tgt_cd varying(2) NOT NULL,
    section_main_nm character varying(100) NULL

);

INSERT INTO TmpTbl
SELECT section_no, user_tgt_cd, section_main_nm
CASE
FROM

