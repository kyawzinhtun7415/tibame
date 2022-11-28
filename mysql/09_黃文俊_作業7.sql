-- 1. 將下列的資料新增至MY_EMP 資料表中,不要列舉欄位。
INSERT INTO 
	my_emp 
VALUES 
	(1, 'Patel', 'Ralph', 'rpatel', 795);
    

-- 2. 使用列舉欄位方式,將下列的資料新增至 MY_EMP資料表中。
INSERT INTO
	my_emp (id, last_name, first_name, userid, salary) 
VALUES
	(2, 'Dancs', 'Betty', 'bdancs', 860);
    

-- 3. 將下列的資料新增至 MY_EMP資料表中。
INSERT INTO
	my_emp
VALUES
	(3, 'Biri', 'Ben', 'bbiri', 1100),
    (4, 'Newman', 'Chad', 'cnewman', 750);
    

-- 4. 將員工編號為3的名字(last name)更改為 Drexler 。
UPDATE 
	my_emp
SET 
	last_name = 'Drexler'
WHERE
	id = 3;
    

-- 5. 將薪資低於900元的所有員工薪資調整為1000元。
UPDATE
	my_emp
SET
	salary = 1000
WHERE
	salary <= 900;
    
    
-- 6. 刪除 Betty Dancs 的資料。
DELETE FROM
	my_emp
WHERE
	userid = 'bdancs';
    

-- 7. 啟動一個資料庫交易
-- 將所有員工的薪資調升10%
-- 設定一個交易儲存點
-- 刪除所有MY_EMP資料表中的資料
-- 確認資料已被你刪光了
-- 放棄刪除資料的動作
-- 確認交易
BEGIN;
	UPDATE my_emp
    SET salary = salary * 1.1;
    
	SAVEPOINT A;
    
    DELETE FROM my_emp;
	SELECT * FROM my_emp;
    
	ROLLBACK to A;
COMMIT;
        