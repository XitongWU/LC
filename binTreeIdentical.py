class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    depth = 0
    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        def DFS(nodeP, nodeQ) -> bool:
            if nodeP is None and nodeQ is None:
                return True
            elif nodeQ is None or nodeP is None:
                return False
            else:
                if nodeP.val != nodeQ.val:
                    return False
                
                is_same = DFS(nodeP.left, nodeQ.left)
                if not is_same:
                    return False
                
                is_same = is_same and DFS(nodeP.right, nodeQ.right)
                if not is_same:
                    return False

                return is_same
            
        return(DFS(p, q))
        
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def DFS(nodeP, nodeQ) -> bool:
            if nodeP is None and nodeQ is None:
                return True
            elif nodeQ is None or nodeP is None:
                return False
            else:
                if nodeP.val != nodeQ.val:
                    return False
                
                is_same = DFS(nodeP.left, nodeQ.right)
                if not is_same:
                    return False
                
                is_same = is_same and DFS(nodeP.right, nodeQ.left)
                if not is_same:
                    return False

                return is_same
            
        return(DFS(root.left, root.right))
        
    def maxDepth(self, root: TreeNode) -> int:
        
        def DFS_depth(node, cur_depth):
            if node.left is None and node.right is None:
                if self.depth < cur_depth:
                    self.depth = cur_depth
                return

            if node.left is not None:
                DFS_depth(node.left, cur_depth+1)
            if node.right is not None:
                DFS_depth(node.right, cur_depth+1)
        
        if root is None:
            return 0
        DFS_depth(root, 1)
        return self.depth
    
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        
        if nums == []:
            return None
        
        # mid = len(nums) // 2
        # root = TreeNode(val=nums[mid])
        
        def DFS(node:TreeNode, sub_nums):
            # if len(sub_nums) == 0:
            #     return
            left = 0
            right = len(sub_nums)
            mid = (left + right) // 2
            
            node.val = sub_nums[mid]
            sub_L = sub_nums[0:mid]
            sub_R = sub_nums[mid+1: ]
            if len(sub_L) != 0:
                leaf = TreeNode()
                node.left = leaf
                DFS(node.left, sub_L)
            if len(sub_R) != 0:
                leaf = TreeNode()
                node.right = leaf
                DFS(node.right, sub_R)

            return
        
        root = TreeNode()
        DFS(root, nums)
        return root
    
    
    def isBalanced(self, root: TreeNode) -> bool:
        
        def getHeight(node:TreeNode) -> int:
            if node is None:
                return 0
            
            return max(getHeight(node.left), getHeight(node.right)) + 1
        
        def checkBalance(node:TreeNode) -> bool:
            if node is None:
                return True
            
            if abs(getHeight(node.left) - getHeight(node.right)) > 1:
                return False

            return checkBalance(node.left) and checkBalance(node.right)
        
        if root is None:
            return True
        return checkBalance(root)
    
    min_dep = 2**31 - 1
    def minDepth(self, root: TreeNode) -> int:
        
        
        def getMinDepth(node:TreeNode, cur_depth:int)->None:
            if node.left is None and node.right is None:
                if cur_depth < self.min_dep:
                    self.min_dep = cur_depth
                return

            if node.left:
                getMinDepth(node.left, cur_depth + 1)
            if node.right: 
                getMinDepth(node.right, cur_depth + 1)
            
        if root is None:
            return 0
        getMinDepth(root, 1)
        return self.min_dep
    
    sum_exist = False
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # sum = 0
        self.sum_exist = False
        def getSum(node:TreeNode, cur_sum:int) -> bool:
            if cur_sum == targetSum and node.left is None and node.right is None:
                self.sum_exist = True
                return

            if self.sum_exist is True:
                return
            
            # if node.left is None and node.right is None:
            #     return 
            
            if node.left:
                getSum(node.left, cur_sum + node.left.val)
            if node.right:
                getSum(node.right, cur_sum + node.right.val)
        
        if root is None:
            return False
        # if root.left is None and root.right is None:
        #     if root.val != targetSum:
        #         return False
        #     return True
        getSum(root, root.val)
        return self.sum_exist
        
        
        pass
    
    # nums = [-10,-3,0,5,9]