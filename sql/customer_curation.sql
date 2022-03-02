-- Written in Postgresql
-- 1.
INSERT INTO {TABLE_NAME}
({COLUMNS}) VALUES ({PLACE_HOLDERS})
ON CONFLICT (psnl_mbr_id, target_psnl_mbr_id)
DO UPDATE SET {update} = excluded.{update}

-- 2.
INSERT INTO {TABLE_NAME}
({COLUMNS}) VALUES ({PLACE_HOLDERS})
ON CONFLICT (psnl_mbr_id, target_psnl_mbr_id)
DO UPDATE SET {update} = excluded.{update}

-- 3.
DELETE
FROM {TABLE_NAME}
WHERE (updated_at :: DATE < CURRENT_DATE or order_cd != '{order_cd}')
AND EXISTS (
		SELECT 1
		FROM {TABLE_NAME}
		WHERE updated_at::DATE = CURRENT_DATE and order_cd = '{order_cd}');
		)

--4.
SELECT COUNT(*)
FROM {TABLE_NAME}
WHERE updated at::DATE < CURRENT_DATE;

--5.
BEGIN;
DELETE FROM ofdown.otb_dlf_ceny_mgt;
We INSERT INTO ofdown.otb_dlf_ceny_mgt
({columns}) VALUES {result};

UPDATE ofdown.otb_dlf_ceny_mgt
SET exps_yn = '1';

COMMIT;

--6. Upserting
INSERT INTO table_name(column_list) VALUES(value_list)
ON CONFLICT target action;