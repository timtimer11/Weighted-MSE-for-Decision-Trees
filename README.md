# Overview
The script contains functions to calculate the Mean Squared Error (MSE) and Weighted MSE (WMSE) of vectors. These metrics are commonly used in evaluating the performance of machine learning models, particularly in decision tree algorithms for determining optimal splits.

# Explanation
The Weighted Mean Squared Error (WMSE) is used to evaluate the quality of splits in decision trees. It calculates the average MSE of two partitions, weighted by the number of elements in each partition. A lower WMSE indicates a better split.

This is the general MSE formula:
![MSE_General](https://github.com/timtimer11/Weighted-MSE-for-Decision-Trees/blob/main/MSE.png)

This is the weighted MSE formula:
![MSE_weighted](https://github.com/timtimer11/Weighted-MSE-for-Decision-Trees/blob/main/MSE_weighted.png)

left, right - the values of the nodes on the left and right after the tree split.
N - number of elements in split

## Acknowledgement:
Special thanks to karpov.courses for the formulas.
