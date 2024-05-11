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
    
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        if root is None:
            return None
        self.res_lst = []
        def preDFS(node:TreeNode):
            if node is None:
                return None
            self.res_lst.append(node.val)
            preDFS(node.left)
            preDFS(node.right)
        preDFS(root)
        return self.res_lst

    def postorderTraversal(self, root: TreeNode) -> list[int]:
        if root is None:
            return None
        self.res_lst = []
        def postDFS(node:TreeNode):
            if node is None:
                return None
            postDFS(node.left)
            postDFS(node.right)
            self.res_lst.append(node.val)
            
        postDFS(root)
        return self.res_lst
            
        
        
        