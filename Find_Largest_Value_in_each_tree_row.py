# Time Complexity : O(N)
# Space Complexity : O(N)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach
# Using BFS. Initialize a queue and iterate over the queue until it is empty
# Then initialize max_value to -inf for each level and iterate over the size of the queue for each level
# Pop the node from the queue and check if node has left and right child and append it to queue
# Check if max_value is less than node value then assign node value to max_value. That will be the max value for each level
# After each level iteration append the max_value to res


from collections import deque
class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        res = []
        if not root:
            return res
        queue = deque([root])
        while queue:
            size = len(queue)
            max_value = float('-inf')
            for i in range(size):
                node = queue.popleft()
                if max_value < node.val:
                    max_value = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(max_value)
        return res
#BFS

class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        self.result = []
        if not root:
            return self.result

        self.helper(root, 0)
        return self.result
    
    def helper(self, root, level):
        if not root:
            return
        if level == len(self.result):
            self.result.append(root.val)
        if root.val > self.result[level]:
            self.result[level] = root.val

        self.helper(root.left, level+1)
        self.helper(root.right, level+1)

        