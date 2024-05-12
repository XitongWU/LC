# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pathp:list[TreeNode] = [root]
        pathq:list[TreeNode] = [root]
        
        def searchPath(node:TreeNode, target:int, path:list[TreeNode]) -> bool:
            if node.val == target:
                return True
            if not node.left and not node.right:
                return False

            if node.left:
                path.append(node.left)
                if searchPath(node.left, target, path):
                    return True
                else:
                    path.pop()
                    
            if node.right:
                path.append(node.right)
                if searchPath(node.right, target, path):
                    return True
                else:
                    path.pop()
                            
        searchPath(root, p.val, pathp)
        searchPath(root, q.val, pathq)
        
        for i in range(0, min(len(pathq), len(pathp))):
            if pathp[i] != pathq[i]:
                return pathp[i-1]
        # return pathp[i]
        if len(pathq) <= len(pathp):
            return pathq.pop()
        else:
            return pathp.pop()
            
        
        pass