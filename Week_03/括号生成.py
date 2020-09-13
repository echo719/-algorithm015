

#khsc
left,right=0,0
res=''
n=3
result=[]
def generate(n):
    left, right = 0, 0
    res=''
    while left<n:
        res+="("
        left+=1
    while right<n:
        res+=")"
        right+=1

    return res
# print(generate(n))


##








#
#
#
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         if n == 0:
#             return []
#         stack = [('(', 1, 0)]
#         ans = []
#         while stack:
#             cur_ans, n_left, n_right = stack.pop()
#             if len(cur_ans) == 2 * n:
#                 ans.append(cur_ans)
#                 continue
#             if n_left < n:
#                 stack.append((cur_ans + '(', n_left + 1, n_right))
#             if n_right < n_left:
#                 stack.append((cur_ans + ')', n_left, n_right + 1))
#         return ans















class Generator(object):
    def genera(self,n):
        if n<=0:
            return []
        result=[]
        stack=[('(',1,0)]
        while stack:
            print("74 stack=",stack)
            res,left,right=stack.pop()
            if len(res)==2*n:
                result.append(res)
                print("=="*4)
                continue
            if left<n:
                stack.append((res+"(",left+1,right))
            if right<left:
                stack.append((res+")",left,right+1))
        return result

    def genera2(self, n):
        if n <= 0:
            return []
        result = []
        stack = [('(', 1, 0)]
        while stack:
            print("74 stack=", stack)
            res, left, right = stack.pop()
            if len(res) == 2 * n:
                result.append(res)
                print("==" * 4)
                continue
            stack.append((res + "(", left + 1, right))
            stack.append((res + ")", left, right + 1))

        new_result=[]
        for res  in result:
            if self.validres(res):
                new_result.append(res)
        print("newresult=",new_result)
        return new_result



    def validres(self,res):
        stack=["x"]
        for i in res:
            if not stack:
                return False
            if i=="(":
                stack.append(i)
            else:
                stack.pop()
        print("stack=",stack)
        return len(stack)==1



gen=Generator()
# print(gen.genera(3))
# print(gen.genera1(3))
print(gen.genera2(3))
#
# result=['((((()', '((((((']
# for res in result:
#     print(gen.validres(res))
























































