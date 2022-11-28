-- 1. 顯示系統目前的日期並將表頭命名為”系統日期”
-- 。
SELECT CURDATE() "系統日期";

-- 2. 顯示所有員工之員工編號,姓名,薪資及將薪資增加15%並且以整數表示，並將表頭命名為”New Salary”。
SELECT empno, ename, sal, ROUND(sal + sal * 0.15) 'New Salary'
FROM emp;

-- 3. 接續第二題，增加一個資料項表頭命名為Increase (將New Salary 減掉 salary 的值)。
SELECT empno, ename, sal, ROUND(sal + sal * 0.15) 'New Salary', ROUND((sal + sal * 0.15) - sal) 'Increase' 
FROM emp;
-- 4. 顯示員工的姓名,進公司日期,檢討薪資的日期(指在進公司工作六個月後的第一個星期一)，將該欄命名
-- 為 REVIEW，並自訂日期格式為：Sunday, the Seventh of September。(星期幾， 幾月幾日)。
SELECT ename, hiredate,
	CASE WEEKDAY(ADDDATE(hiredate, INTERVAL 6 Month))
		WHEN 1 THEN DATE_FORMAT(ADDDATE(ADDDATE(hiredate, INTERVAL 6 DAY), INTERVAL 6 Month),' %W ,the %D of %M, %Y')
		WHEN 2 THEN DATE_FORMAT(ADDDATE(ADDDATE(hiredate, INTERVAL 5 DAY), INTERVAL 6 Month),' %W ,the %D of %M, %Y')
		WHEN 3 THEN DATE_FORMAT(ADDDATE(ADDDATE(hiredate, INTERVAL 4 DAY), INTERVAL 6 Month),' %W ,the %D of %M, %Y')
		WHEN 4 THEN DATE_FORMAT(ADDDATE(ADDDATE(hiredate, INTERVAL 3 DAY), INTERVAL 6 Month),' %W ,the %D of %M, %Y')
		WHEN 5 THEN DATE_FORMAT(ADDDATE(ADDDATE(hiredate, INTERVAL 2 DAY), INTERVAL 6 Month),' %W ,the %D of %M, %Y')
		WHEN 6 THEN DATE_FORMAT(ADDDATE(ADDDATE(hiredate, INTERVAL 1 DAY), INTERVAL 6 Month),' %W ,the %D of %M, %Y')
		ELSE DATE_FORMAT(ADDDATE(hiredate, INTERVAL 6 Month),' %W ,the %D of %M, %Y')
	END REVIEW
FROM emp;

-- Best Answer
SELECT ename, hiredate, DATE_FORMAT(ADDDATE(ADDDATE(hiredate, INTERVAL 6 Month), INTERVAL MOD(7 - WEEKDAY(hiredate), 7) DAY), '%W ,the %D of %M, %Y') "REVIEW"
FROM emp;

-- with CTE
WITH CTE1(ename, hiredate, hd6m, hd6mWD) AS (
SELECT ename, hiredate, ADDDATE(hiredate, INTERVAL 6 MONTH), WEEKDAY(ADDDATE(hiredate, INTERVAL 6 MONTH))
FROM emp
),
CTE2(ename, hiredate, hd6m, hd6mADay) AS (
SELECT ename, hiredate, hd6m, MOD(7-hd6MWD, 7)
FROM CTE1
)
SELECT ename, hiredate, DATE_FORMAT(ADDDATE(hd6m, INTERVAL hd6mADay DAY), '%W, the %D of %M') 'REVIEW' 
FROM CTE2;



-- 5. 顯示每位員工的姓名，資料項(MONTHS_WORKED):計算到今天為止工作了幾個月(將月數四捨五入到
-- 整數)
SELECT ename, ROUND((DATEDIFF(CURDATE(), hiredate) / 365) * 12) 'MONTHS_WORKED'
FROM emp;
-- 6. 顯示如下格式：<員工姓名> earns <薪水> monthly but wants <3倍的薪水>.並將表頭顯示為Dream
-- Salaries。
SELECT concat(ename, ' earns ', sal, ' monthly but wants ', sal * 3) "Dream Salaries"
FROM emp;

-- 7. 顯示所有員工之姓名和薪資，設定薪資長度為15個字元並且在左邊加上$符號，將表頭命名為SALARY。
SELECT ename, LPAD(sal, 15, '$') "SALARY" 
FROM emp;

-- 8. 顯示員工之姓名,進公司日期，資料項(DAY):顯示員工被雇用的那天為星期幾，並以星期一作為一週的
-- 起始日,依星期排序。
SELECT ename, hiredate, WEEKDAY(hiredate) + 1 Day
FROM emp
ORDER BY WEEKDAY(hiredate);

-- 9. 顯示員工的姓名和名為COMM的欄位:顯示佣金額，如果該員工沒有賺取佣金則顯示"No Commission."。
SELECT ename, IFNULL(comm, 'No Commission.') "Comm"
FROM emp;

-- 10.顯示資料項命名為 EMPLOYEE_AND_THEIR_SALARIES 的資料來顯示所有員工之名字和薪資，且用
-- 星號來表示他們的薪資，每一個星號表示100元，並以薪資由高到低來顯示。
SELECT CONCAT(ename, ' ', REPEAT('*', ROUND( sal / 100))) EMPLOYEE_AND_THEIR_SALARIES
FROM emp
ORDER BY REPEAT('*', ROUND( sal / 100)) DESC;