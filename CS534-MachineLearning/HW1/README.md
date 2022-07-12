- Introduction
- Solution Part 0
- Solution Part 1
- Solution Part 3



# Introduction: 


In this assignment, we are trying to fit a linear model to the large data of variables which have shown to be important when pricing a house. The initial  dataset has been divided into training and validation sets 60% to 40%, where the weights are learned in the training set and validated in the test set. The data consists of numerical, categorical, and nominal data. While normalization helps to bring them in the same range, it would not make sense for some, like date or grade etc. therefore feature engineering is required to better form the dataset. This assignment shows that the initial dataset should be investigated first in a way that the relationship with the target value is apparent, normalization helps a lot, smaller learning rates take longer to train but rarely diverge and batch gradient decent method is good when dataset fits into memory in one place. 
Part0) 

a) Because there is no logical correlation between ID and the target, price. Any correlation would be random and the very large values would make it longer to learn from features that matter the most. 

b) If we assume the price always increases or decreases as years increase, then we can consider the year as numerical variable. At the same time, we can also consider it a categorical variable, e.g. each for year variable =1 else =0 to illustrate election effect. We can add the economic growth as ordinal (GDP) such as ‘bad’, ‘normal’, ‘good’. House prices differ based on seasons and months, therefore, considering the month as categorical variable would be helpful. To avoid complexity, we could divide by season.  Specific days have not been known to affect the housing price much as opposed to stock market due to much less volume of trades, therefore, to avoid complex models we may try omitting this variable.  

