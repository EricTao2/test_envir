import bisect
import queue
import string

from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
import collections
from collections import Counter
import math
import operator
import re
import sys
import time
from typing import List
from sklearn.preprocessing import StandardScaler

class Case:
    def __init__(self):
        return
    
    def sovle(self, s, n, k):
        count = 0
        for i in range(n//2):
            if s[i] == s[-i-1]:
                count += 1
        return abs(count - k)
    
    def io_case(self):
        t = int(input())
        for i in range(1, t+1):
            n, k = [int(i) for i in input().split()]
            s = input()
            result = self.sovle(s, n, k)
            print('Case #' + str(i) +': ' + str(result))

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def create_nodes(self, ls):
        if not ls:
            return None
        ls1 = [TreeNode(ls[0])]
        result = ls1[0]
        pre = None
        has_left = False
        next_node = True
        for i in range(1, len(ls)):
            node = TreeNode(ls[i])
            if next_node and ls1:
                pre = ls1.pop(0)
                next_node = False
            if ls[i] != None:
                ls1.append(node)
            if not has_left:
                if pre and ls[i] != None:
                    pre.left = node
                has_left = True
            else:
                if pre and ls[i] != None:
                    pre.right = node
                has_left = False
                next_node = True
        return result


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def create_nodes(self, ls):
        head = ListNode()
        node = head
        for x in ls:
            node.next = ListNode(x)
            node = node.next
        return head.next


class Node:
    def __init__(self, x: int = 0, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
    
    def create_nodes(self, ls):
        head = Node()
        node = head
        temp = []
        for x in ls:
            node.next = Node(x[0])
            node = node.next
            temp.append(node)
        for i in range(len(ls)):
            if ls[i][1]:
                temp[i].random = temp[ls[i][1]]
        return head.next



class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        return
        
        
        
    
y = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
a = ListNode(2, ListNode(0))
b = ListNode(-4, a)
a.next.next = b
x = ListNode(3, a)
tree = TreeNode()
node = ListNode()
node1 = Node()
root = tree.create_nodes([3,5,1,6,2,0,8,None,None,7,4])
root1 = tree.create_nodes([2,1,4,None,None,3])
head = node.create_nodes([5,2,6,3,9,1,7,3,8,4])
head1 = node1.create_nodes([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])


def main():
    obj = Solution()
    import json
    # file = open('C:/Users/TJX/Desktop/123.txt')
    # infoList = file.read()
    # arg = json.loads(infoList)
    result = obj.groupTransactions(['bin', 'can', 'bin', 'bin'])
    print(result)
    
if __name__ == '__main__':
    main()


