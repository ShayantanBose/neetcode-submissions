class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # implementation intentionally omitted
        res = []
        q = collections.deque([root])

        while q:
            rigtSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rigtSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rigtSide:
                res.append(rigtSide.val)
        return res
