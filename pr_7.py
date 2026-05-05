# Import libraries
import pandas as pd
import numpy as np
from scipy import stats
# Create sample data (marks of two groups)
group_A = [45, 50, 55, 60, 65]
group_B = [30, 35, 40, 45, 50]
# Convert to arrays
A = np.array(group_A)
B = np.array(group_B)
# Perform independent t-test
t_stat, p_value = stats.ttest_ind(A, B)
# Print results
print("Group A Mean:", np.mean(A))
print("Group B Mean:", np.mean(B))
print("T-Statistic:", t_stat)
print("P-Value:", p_value)
# Decision
alpha = 0.05
if p_value < alpha:
    print("Reject Null Hypothesis (Significant Difference)")
else:
    print("Fail to Reject Null Hypothesis (No Significant Difference)")

#Pr_7.2

import numpy as np
from scipy.stats import chi2_contingency
# Contingency table
data = np.array([[10, 20, 30],
[6, 9, 17]])
chi2, p, dof, expected = chi2_contingency(data)
print("Chi-square value:", chi2)
print("P-value:", p)
print("Degrees of freedom:", dof)
print("Expected Frequencies:\n", expected)
# Decision
alpha = 0.05
if p < alpha:
    print("Reject H0 (Variables are related)")
else:
    print("Fail to Reject H0 (Variables are independent)")

#Pr_7.3

from scipy.stats import f_oneway
# Data
group_A = [45, 50, 55]
group_B = [60, 65, 70]
group_C = [30, 35, 40]
# Perform ANOVA
f_stat, p_value = f_oneway(group_A, group_B, group_C)
print("F-Statistic:", f_stat)
print("P-value:", p_value)
# Decision
alpha = 0.05
if p_value < alpha:
    print("Reject H0 (Means are different)")
else:
    print("Fail to Reject H0 (Means are equal")
