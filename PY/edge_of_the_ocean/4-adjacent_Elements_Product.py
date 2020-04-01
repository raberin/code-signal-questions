"""
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.
"""


def adjacentElementsProduct(inputArray):
    result = []
    # Loop and push product of adjacent indices
    for i in range(len(inputArray) - 1):
        num = inputArray[i] * inputArray[i + 1]
        result.append(num)
    # Return biggest product
    return max(result)
