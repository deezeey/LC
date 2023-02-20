from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 10.27 first try. neet code的DFS解法
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        
        def dfs(node):
            if not node:
                res.append("N")  #看并非所有的recursion base case都需要return。if else也可以写出recursion
            else:
                res.append(str(node.val))
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.i = 0  # <--------- 这里用self.i的原因是下面dfs function需要用到i，但我们并不想把它作为parameter pass进去，所以define it as a property of the class
        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()


# 参考了九章的BFS解法
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "N"

        res = []
        q = [root]

        while q: # <--- 最底下一层的下一层全是node None。会全部append N到res然后continue，但不会再append任何东西到q里了。这样q就有尽头
            node = q.pop(0)  # <--- 为什么这个BFS就不用for _ in len(q):呢，因为我们没有什么特别要在整层nodes都visit完了以后做的事情
            if not node:
                res.append("N")
                continue
            res.append(str(node.val))
            q.extend([node.left, node.right])

        return ",".join(res)

    def deserialize(self, data):  # <--- 这个deserialize only work for 上面那个bfs serialize，因为需要最底下有一整层 N
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "N":
            return None

        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        q = [root]
        isLeft = True
        cur_parent_index = 0

        for val in vals[1:]:
            if val != "N":
                node = TreeNode(int(val))
                if isLeft:
                    q[cur_parent_index].left = node
                else:
                    q[cur_parent_index].right = node
                q.append(node)
            if not isLeft:
                cur_parent_index += 1
            isLeft = not isLeft

        return root


# 11.15 复习自己写了个level order的serialize， deserialize 30min内没写出来，头疼懒得想了
# 第二天把deserialize写出来了，pass了51/52 cases然后TLE了，逻辑是通的但是最终发现我这个对与memory非常不友好
# [4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2] 这个case，可以去230 testcase里面画一下这个树
# 我的serialize出来是如下这样，none下面指数level insert更多的none，每层都记满格是非常不efficient的。用九章的deserialize也无法再还原。
# 4,
# -7,-3,
# N,N,-9,-3,
# N,N,N,N,9,-7,-4,N,
# N,N,N,N,N,N,N,N,6,N,-6,-6,N,N,N,N,
# N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,0,6,N,N,5,N,9,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,-1,-4,N,N,N,N,N,N,N,N,N,-2,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = deque([root])
        res = []
        while q:
            new_level = []
            for _ in range(len(q)):
                cur = q.popleft()
                res.append(str(cur.val) if cur else 'None')
                new_level.append(cur.left if cur and cur.left else None)
                new_level.append(cur.right if cur and cur.right else None)
            if any(new_level):
                q.extend(new_level)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        root = None if vals[0] == "N" else TreeNode(val = int(vals[0]))
        if len(vals) == 1:
            return root

        res = [root]
        i = 0
        incre_left, incre_right = 0, 1

        while True:
            cur_node = res[i]
            incre_left, incre_right = incre_right, incre_right + 1
            left_i, right_i = i + incre_left, i + incre_right

            if left_i >= len(vals):
                return root
            left_child_node = None if vals[left_i] == "N" else TreeNode(val = int(vals[left_i]))
            if cur_node:
                cur_node.left = left_child_node
            res.append(left_child_node)

            if right_i >= len(vals):
                return root
            right_child_node = None if vals[right_i] == "N" else TreeNode(val = int(vals[right_i]))
            if cur_node:
                cur_node.right = right_child_node
            res.append(right_child_node)
            i += 1


# 自己尝试默写了一下九章BFS的还原。看到问题了
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "N":
            return None

        vals = data.split(",")
        root = TreeNode(val = int(vals[0]))
        q = [root]
        i = 0
        is_left = True

        for value in vals[1:]:
            if value == "N":
                continue  # <--- 碰到N不能直接continue，因为我们还需要变换is_left和increment parent node的idx
            else:
                child = TreeNode(val = int(value))
            if is_left:
                q[i].left = child
            else:
                q[i].right = child
            q.append(child)
            if not is_left:
                i += 1
            is_left = not is_left
        
        return root

# 重写一遍， 这个function是对的但是对于我自己写的bfs serialize不work，因为我的serialize和九章的bfs也不一样
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "N":
            return None

        vals = data.split(",")
        root = TreeNode(val = int(vals[0]))
        q = [root]
        i = 0
        is_left = True

        for value in vals[1:]:
            print(i, [n.val for n in q])
            if value != "N":
                child = TreeNode(val = int(value))
                if is_left:
                    q[i].left = child
                else:
                    q[i].right = child
                q.append(child)
            if not is_left:
                i += 1
            is_left = not is_left
        
        return root

# 11.17 怕忘自己又默了一遍preorder traversal encode decode都是 T O(n) M O(n)
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # preorder traversal
        res = []

        def dfs(root):
            if not root:
                res.append("n")
            else:
                res.append(str(root.val))
                dfs(root.left)
                dfs(root.right)
            
        dfs(root)
        return ",".join(res)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "n":
            return None

        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "n":
                self.i += 1
                return None
            node = TreeNode(val = int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs() 

    
# 12.15 复习没写出来

# 1.7 复习花了一点时间自己写出来preorder的了
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(root):
            if not root:
                res.append("n")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            return

        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(",")
        i = 0

        def dfs():
            nonlocal i
            if arr[i] == "n":
                i += 1
                return None
            node = TreeNode(int(arr[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
