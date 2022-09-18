-- 1
SELECT * 
FROM dept;

-- 2
SELECT empno, ename, job, hiredate
FROM emp;

-- 3
SELECT DISTINCT job
FROM emp;

-- 4
SELECT empno "Emp#", ename "Employee", job "Job", hiredate "Hire Date"
FROM emp;

-- 5
SELECT concat(ename, ', ', job) "Employee and Title"
FROM emp;