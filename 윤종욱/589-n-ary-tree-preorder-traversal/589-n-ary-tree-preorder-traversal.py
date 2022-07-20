"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        self.result = [root.val]
        self.search(root.children)
        return self.result
                
    def search(self, list_q):
        if list_q == None:
            return
        for q in list_q:
            self.result.append(q.val)
            self.search(q.children)
        
                