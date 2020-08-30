nums=[1,2,7,6,3,3,0]
def twosums(nums):
    #时间复杂度o(n),空间复杂度o(n)
    if not nums:
        return
    target=9
    dic={}
    for i,num in enumerate(nums):
        dic[num]=i
    nums=sorted(nums)
    print('排序后=',nums)
    print("dic=",dic)
    i=0
    j=len(nums)-1
    result=[]
    while i<j:
        if nums[i]+nums[j]<target:
            i+=1
        elif nums[i]+nums[j]>target:
            j-=1
        else:
            print("i,j=",nums[i],'\t',nums[j])
            a=dic[nums[i]]
            b=dic[nums[j]]
            if [a,b] not in result:
                result.append([a,b])
            i+=1 #这里有漏洞.接连2个j 是相同的，则有个j会被跳过了..。。
    return result

print("result=",twosums(nums))



# nums=[1,2,7,6,3,3,0,-1,-9]
#
# dic={}
# for i,num in enumerate(nums):
#     dic[num]=i
# nums=sorted(nums)
# ans=[]
# #枚举a
# for first in range(len(nums)):
#     #需要和上一次枚举的数不相同
#     if first>0 and nums[first]==nums[first-1]:
#         continue
#
#     #c对应的指针初始指向数组的最右端
#     third=len(nums)-1
#     target=-nums[first]
#
#     #枚举b
#     for second in range(first+1,len(nums)):
#         #需要和上次枚举的数不相同
#         if second>first+1 and nums[second]==nums[second-1]:
#             continue
#
#         #需要保证b的指针在c的指针的左侧
#         while second<third and nums[second]+nums[third]>target:
#             third-=1
#
#             #如果指针重合，随着b后续的增加
#             #就不会满足a+b+c=0 并且b<c的了，可以退出循环
#             if second==third:
#                 break
#             if nums[second]+nums[third]==target:
#                 ans.append([nums[first],nums[second]])
#
# return ans

        

