-- 1 Top 5 Funds by AUM

SELECT *
FROM aum
ORDER BY aum_crores DESC
LIMIT 5;


-- 2 Average NAV Per Fund

SELECT

amfi_code,

AVG(nav)

FROM nav_history

GROUP BY amfi_code;


-- 3 Average NAV Per Month

SELECT

strftime('%Y-%m',date)

AS month,

AVG(nav)

FROM nav_history

GROUP BY month;


-- 4 Transactions By State

SELECT

state,

COUNT(*)

FROM transactions

GROUP BY state;


-- 5 Expense Ratio Less Than 1

SELECT *

FROM performance

WHERE expense_ratio_pct <1;


-- 6 Total Transactions Per Fund

SELECT

amfi_code,

COUNT(*)

FROM transactions

GROUP BY amfi_code;


-- 7 Highest Return Funds

SELECT *

FROM performance

ORDER BY return_5yr_pct DESC

LIMIT 10;


-- 8 Count Funds By Category

SELECT

category,

COUNT(*)

FROM fund_master

GROUP BY category;


-- 9 Average Expense Ratio

SELECT

AVG(expense_ratio_pct)

FROM performance;


-- 10 Total AUM

SELECT

SUM(aum_crores)

FROM aum;