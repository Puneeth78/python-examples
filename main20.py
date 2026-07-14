# # # n=5
# # # for i in range(n):
# # #     for j in range(i,n):
# # #         if j==0 or j==i or j==n-1:
# # #             print("*",end=" ")
# # #         else:
# # #             print(" ",end=" ")
# # #     print()

# # # import math
# # # x=math.sqrt(9)
# # # y=int(x)
# # # print(y)

# # from math import sqrt,pi
# # print(sqrt(9))
# # print(sqrt(10))
# # print(pi)

# # '''_init_.py is a special file in python used to 
# # define the packages and initilize thier name space'''

# # def add(a,b):
# #     return a+b



# class Solution:
#     def singleNumber(self, nums):

#         nums.sort()
#         print(nums)

#         i = 0

#         while i < len(nums) - 1:

#             print("Checking:", nums[i], nums[i + 1])

#             if nums[i] != nums[i + 1]:
#                 return nums[i]

#             i += 2

#         return nums[-1]


# nums = [4,4,4,4,5,5,5,1]

# obj = Solution()
# print("Single Number =", obj.singleNumber(nums))

def merge_sort(arr):

    # Base Case
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):

    result = []
    i = j = 0

    # Compare elements from left and right
    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Driver Code
arr = [40, 30, 20, 10]

sorted_array = merge_sort(arr)

print("Sorted Array:", sorted_array)