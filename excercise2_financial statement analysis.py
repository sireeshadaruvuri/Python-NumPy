from typing import Any, Union

import numpy as np
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]
#profit for each month - (total revenue-expenses)
#a = np.array(revenue)
pr = []
for i in range(0, len(revenue)):
    pr.append(revenue[i] - expenses[i])
print(pr)
pra = [round(i*0.3,2) for i in pr]
print(pra)
praf = []
for i in range(0, len(pra)):
    praf.append(pr[i]- pra[i])
print(praf)
pr_margin = list([])
for i in range(0, len(pr)):
    pr_margin.append(praf[i]/revenue[i])
print(pr_margin)
pr_margin = [round((i*100),2) for i in pr_margin]
print(pr_margin)
mean = sum(praf) / len(praf)
print(mean)
"""
ca = max(praf)
print(ca)
cd = min(praf)
print(cd)
"""
good_months = list([])
for i in (range(0, len(praf))):
    good_months.append(praf[i] > mean)
print(good_months)
bad_months = list([])
for i in (range(0, len(praf))):
    bad_months.append(praf[i] < mean)
print(bad_months)
#best month
best_month = list([])
for i in (range(0, len(praf))):
    best_month.append(praf[i] == max(praf))
print(best_month)
#worst month
worst_month = list([])
for i in (range(0, len(praf))):
    worst_month.append(praf[i] == min(praf))
print(worst_month)
revenue_1000 = [round((i/1000),2) for i in revenue]
expenses_1000 = [round((i/1000),2) for i in expenses]
pr_1000 = [round((i/1000),2) for i in pr]
praf_1000 = [round((i/1000),2) for i in praf]

print(revenue_1000)
print(expenses_1000)
print(pr_1000)
print(praf_1000)
revenue_1 = [int(i) for i in revenue_1000]
expenses_1 = [int(i) for i in expenses_1000]
pr_1 = [int(i) for i in pr_1000]
praf_1 = [int(i) for i in praf_1000]
print(revenue_1)
print(expenses_1)
print(pr_1)
print(praf_1)
print("profit is ")
print(pr_1)
print("best month is")
print(best_month)