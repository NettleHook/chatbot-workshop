"""
Hypothesis testing:

Professor believes that students who attend the class
synchronously have higher grades than students who attend asynchronously.

H0: Asynchronous learner grades ≥ synchronous learner grades
HA: Asynchronous learner grades < synchronous learner grades
"""
import matplotlib.pyplot as plt

synchronous = [94. , 84.9, 82.6, 69.5, 80.1, 79.6, 81.4, 77.8, 81.7, 78.8,
               73.2, 87.9, 87.9, 93.5, 82.3, 79.3, 78.3, 71.6, 88.6, 74.6, 74.1, 80.6]
asynchronous = [77.1, 71.7, 91. , 72.2, 74.8, 85.1, 67.6,
                69.9, 75.3, 71.7, 65.7, 72.6, 71.5, 78.2]
alpha = 0.05

"""
Assumption checks:
Normally distributed:synchronous-yes, asynchronous-maybe?
Equal variance:?
observations are independent: yes
"""
"""
plt.hist(x=synchronous)
plt.show()
plt.hist(x=asynchronous)
plt.show()
"""

"""
additionally, data is not-paired, and we're only having two groups
independent t-test?
In the instruction/examples we're following:
    https://towardsdatascience.com/hypothesis-testing-with-python-step-by-step-hands-on-tutorial-with-practical-examples-e805975ea96e
they use more hypothesis testing to check for normal distribution and variance. Determine that both datasets are normally distributed, and that the variances are the same.
ergo, yes parametric
"""
from scipy.stats import ttest_ind

ttest, p_val = ttest_ind(synchronous, asynchronous, alternative='greater')
if p_val < alpha:
    print('Reject null hypothesis')
else:
    print("Fail to reject null hypothesis")
