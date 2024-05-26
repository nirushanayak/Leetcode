# Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

 

# Example 1:

# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4),
# pop() -> 4,
# push(5),
# pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
# Example 2:

# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.
 

# Constraints:

# 1 <= pushed.length <= 1000
# 0 <= pushed[i] <= 1000
# All the elements of pushed are unique.
# popped.length == pushed.length
# popped is a permutation of pushed.

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        p1,p2=0,0
        if len(pushed)!=len(popped):
            return False
        while p1<len(pushed) and p2<len(pushed):
            while stack and stack[-1]==popped[p2]:
                stack.pop()
                p2=p2+1
            stack.append(pushed[p1])
            p1=p1+1
        while p2<len(popped) and stack and stack[-1]==popped[p2]:
            stack.pop()
            p2=p2+1
        if stack:
            return False
        return True


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        p1=0
        for n in pushed:
            stack.append(n)
            while stack and p1<len(popped) and stack[-1]==popped[p1]:
                stack.pop()
                p1=p1+1
        return not stack
        