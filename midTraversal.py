class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    res_lst = []
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        self.res_lst = []
        self.DFS(root)
        return self.res_lst
        
    def DFS(self, node: TreeNode) -> None:
        if node == None:
            return
        
        self.DFS(node.left)
        self.res_lst.append(node.val)
        self.DFS(node.right)
        
        