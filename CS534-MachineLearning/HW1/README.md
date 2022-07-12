- Introduction
- Solution Part 0
- Solution Part 1
- Solution Part 3



# Introduction: 


In this assignment, we are trying to fit a linear model to the large data of variables which have shown to be important when pricing a house. The initial  dataset has been divided into training and validation sets 60% to 40%, where the weights are learned in the training set and validated in the test set. The data consists of numerical, categorical, and nominal data. While normalization helps to bring them in the same range, it would not make sense for some, like date or grade etc. therefore feature engineering is required to better form the dataset. This assignment shows that the initial dataset should be investigated first in a way that the relationship with the target value is apparent, normalization helps a lot, smaller learning rates take longer to train but rarely diverge and batch gradient decent method is good when dataset fits into memory in one place.

