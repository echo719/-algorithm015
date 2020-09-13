# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
#
# 示例:
#
# 输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]


class Zh(object):
    def __init__(self):
        pass
    def zuhe2(self,n,k):
        result=[]
        nums=[i for i in range(1,n+1)]

        res=nums[:k]
        print("res=",res)
        result.append(res)

        changeidx=-1

        while changeidx>-k:
            res2=self.changeonde(changeidx,k,n,res)
            result.append(res2)
            changeidx-=1
        return result
    def changeonde(self,changeidx,k,n,res):
        for j in range(k+1,n+1):
            del res[changeidx]
            res.append(j)
            return res

zh=Zh()
print(zh.zuhe2(4,2))