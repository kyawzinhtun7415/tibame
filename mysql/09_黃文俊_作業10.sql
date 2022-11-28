-- 1. 顯示所有員工之姓名，部門編號，薪資及該部門最低薪資(以JOIN衍生資料表方式撰寫SQL)。
SELECT 
	e1.ename, e1.deptno, e1.sal, e2.minsal
FROM 
	emp e1 JOIN 
    (SELECT MIN(sal) "minsal", deptno FROM emp GROUP BY deptno) e2 
    ON e1.deptno = e2.deptno;


-- 2. 顯示所有員工之姓名，部門編號，薪資及該部門最低薪資(以CTE方式撰寫SQL)。
WITH e2 AS (
	SELECT MIN(sal) "minsal", deptno 
    FROM emp 
    GROUP BY deptno
)
SELECT 
	ename, deptno, sal, minsal
FROM
	emp JOIN e2 USING (deptno);
    
    
-- 3. 顯示所有員工之姓名，部門編號，薪資及該部門最低薪資(以Window Function 方式撰寫SQL)。
SELECT 
	ename, deptno, sal, 
    MIN(sal) OVER 
    (PARTITION BY deptno) "minsal"
FROM emp;


-- 4. 顯示員工的姓名，進公司日期，檢討薪資的日期(指在進公司工作六個月後的第一個星期一)，將該欄命 名為 REVIEW。
-- with CTE
WITH CTE1(ename, hiredate, hd6m, hd6mWD) AS (
SELECT ename, hiredate, ADDDATE(hiredate, INTERVAL 6 MONTH), WEEKDAY(ADDDATE(hiredate, INTERVAL 6 MONTH))
FROM emp
),
CTE2(ename, hiredate, hd6m, hd6mADay) AS (
SELECT ename, hiredate, hd6m, MOD(7-hd6MWD, 7)
FROM CTE1
)
SELECT ename, hiredate, ADDDATE(hd6m, INTERVAL hd6mADay DAY)'REVIEW' 
FROM CTE2;


-- 5. 顯示員工的編號，姓名，部門編號，主管及等級 (無主管等級為1，其上有一層主管等級為2，以此類推)。
WITH RECURSIVE employee_levels AS
(
	SELECT empno, ename, deptno, mgr, 1 "Level"
		FROM emp
		WHERE mgr IS NULL
    UNION ALL
    SELECT e.empno, e.ename, e.deptno, e.mgr, Level + 1 
		FROM employee_levels el JOIN emp e
			ON el.empno = e.mgr
)
SELECT * FROM employee_levels ORDER BY Level;


-- 6. 顯示員工的編號，姓名，部門編號，薪資及薪資於全公司之排名(有同名則往後會跳過名次)。
SELECT empno, ename, deptno, sal, 
	RANK() OVER (ORDER BY sal DESC) Salary_Rank
FROM emp;


-- 7. 顯示員工的編號，姓名，部門編號，薪資及薪資於該部門之排名(有同名則往後不會跳過名次)。
SELECT empno, ename, deptno, sal,
	RANK() OVER (PARTITION BY deptno
				ORDER BY sal DESC) "Salary_Rank"
FROM emp;


-- 8. 顯示所有訂單之編號，訂單日期，訂單金額及累計至此訂單之總銷售額。
SELECT ordid, orderdate, total, 
	SUM(total) OVER W running_total
FROM ord
WINDOW W AS (ORDER BY orderdate
            ROWS UNBOUNDED PRECEDING)
ORDER BY orderdate;
			
            
-- 9. 顯示所有訂單之編號，訂單日期，訂單金額及以年度劃分累計至此訂單之總銷售額。
SELECT ordid, orderdate, total, 
	SUM(total) OVER W running_total
FROM ord
WINDOW W AS (PARTITION BY YEAR(orderdate)
			ORDER BY orderdate
            ROWS UNBOUNDED PRECEDING)
ORDER BY orderdate;


-- 10.顯示所有訂單之編號，訂單日期及本筆訂單距上筆訂單已經過了多少天。
SELECT ordid, orderdate, 
	DATEDIFF(orderdate, LAG(orderdate) OVER W) Previous_Order_Days
FROM ord
WINDOW W AS (ORDER BY orderdate) 
ORDER BY orderdate;