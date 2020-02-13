# coding: utf-8

#leetcode 349: https://leetcode.com/problems/intersection-of-two-arrays/description/
# description: 查找给定的两个list中相同的元素，返回无重复列表

class IntersectionOfTwoArrays:
    # 思路1：num1 元素存入哈希表，再将num2遍历查找。
    # 为什么不将列表去重后查找？因为 a in list 的方式 比 a in dict 的方式更加耗时。
    def inter(self, num1:List[int], num2: List[int]):
        visited, result = {}, []
        for n in num1:
            visited[n] = n
            
        for n in num2:
            if n in visited:
                result.append(n)
                visited.pop(n)
                
        return result
        
    #思路2：利用python的集合计算
    def inter2(self, num1:List[int], num2: List[int]):
        return set(num1)& set(num2)
        
        #集合配合逻辑运算在python中非常好用。
        # eg:
        # set(list1) & set(list2) 可以得到两个列表的交集，即相同元素
        # set(list1) & set(list2) 可以得到两个列表的并集，即全部元素