"""
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

Example

For statues = [6, 2, 3, 8], the output should be
makeArrayConsecutive2(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7. 
"""


# O(n)
def make_array_consecutive_2(statues):
    max_num = max(statues)
    min_num = min(statues)
    arr = []
    # Loop through min -> max inclusive creating answer arr
    for i in range(min_num, max_num + 1):
        arr.append(i)
    # Difference of answer arr with input
    return len(arr) - len(statues)
