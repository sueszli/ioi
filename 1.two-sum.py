from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    result = [-1, -1]

    # there are len(nums)*2 unique combinations as (i+j) == (j+i)
    checked = [False for i in range(len(nums) * 2 - 1)]    

    for i in range(len(nums)):
        for j in range(len(nums)):
            if (checked[i+j] == False) and (nums[i] + nums[j] == target):
                return [i,j]
            checked[i+j] = True
    
    return result

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    result = two_sum(nums, target)
    print(f'{nums} with target {target} --> {result}')
