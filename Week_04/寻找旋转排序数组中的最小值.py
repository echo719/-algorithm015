# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
# 请找出其中最小的元素。
# 你可以假设数组中不存在重复元素。
#
# 示例 1:
# 输入: [3,4,5,1,2]
# 输出: 1
# 示例 2:
# 输入: [4,5,6,7,0,1,2]
# 输出: 0

def findmin(nums):
    left,right=0,len(nums)-1

    while left<right:
        mid=(left+right)//2
        if nums[mid]>nums[right]:#右边是包含最小值的？无序的。向右突进
            left=mid+1  #为什么left=mid  就会超出时间限制呢？？？
        elif nums[mid]<nums[right]:#右边有序，左边无序；向左推进
            right=mid
    return nums[left]




class Solution:
    def findMin(self, nums: List[int]) -> int:
        left , right = 0 , len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else: right = mid
        return nums[left]

