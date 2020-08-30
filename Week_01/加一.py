
#题目：
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#

# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。



#1. 暴力解法：concat一起，加一再split。 时间复杂度，O（n）*2；空间复杂度o(n)*2
#2. 从后往前，遇到第一个非9，就结束。 是9就变0，前一位加一；
#相当于，只有部分数字进行了操作，且是就地操作吗？  好像不是！！  可以降低 时间复杂度  和空间复杂度  多少呢？
#一般情况下，本来是多少位，还是多少位；特殊情况下，如果每个位置都是9，就得将原数组增加一位了


#1. 暴力：
# def add_one(nums):
#     #int  编程str，才可以 join到一起，就已经是一个O(n)了！
#     s=int(''.join([str(i) for i in nums]))
#     # print(type(s),s)
#     s+=1
#     s=str(s)
#     # print('s=',type(s), s)
#     nums=[s[i] for i in range(len(s))]
#     #
#     # print(nums)
#     return nums
# print(add_one(nums))
#
# # #2.
# nums=[9,9,9]
# s=len(nums)
# def add_one(nums):
#     ##导致的是 每次 递归传入的 nums都在缩小，最后都不是那个长度了？？
#     print("==="*3)
#     if nums[-1]!=9:
#         nums[-1]+=1
#         print('0res=', nums)
#         return nums
#     else:
#         nums[-1]=0
#         print('1res=',nums)
#         print('=',nums[:-1])
#         if nums[:-1]:
#             nums=add_one(nums[:-1])
#     print("58 nums=",nums)
#     return nums



digits=[9,9,9]

def add_1(digits):
    for i in range(len(digits)-1,-1,-1):
        print(i)
        if digits[i]!=9:
            digits[i]+=1
            return digits
        else:
            digits[i]=0
    digits.insert(0,1)
    return digits

digits=add_1(digits)
print('res=',digits)








