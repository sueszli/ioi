from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    result = [-1, -1]

    # there are len(nums)*2 unique combinations as (i+j) == (j,i)
    # we have to subtract 1 since we're counting from 0
    checked = [False for i in range(len(nums) * 2)]

    for i in nums:
        for j in nums:
            if (checked[i+j] == False) and (i + j == target):
                print(f'{i} + {j} = {i+j}')
            checked[i+j] = True
    return result

if __name__ == "__main__":
    nums = [0,1,2,3,4,5,6,7,8,9]
    target = 10
    result = two_sum(nums, target)
    print(f'{nums} with target {target} --> {result}')
