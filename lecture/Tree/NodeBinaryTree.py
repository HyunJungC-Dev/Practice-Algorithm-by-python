class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, array):
        node_list = [Node(value, None, None) for value in array]
        for ind, node in enumerate(node_list):
            left = 2 * ind + 1
            right = 2 * ind + 2
            if left < len(node_list):
                node.left = node_list[left]
            if right < len(node_list):
                node.right = node_list[right]

        self.root = node_list[0]

    # node -> left-> right
    def preorder(self):
        stack = []
        if self.root is None:
            return None
        else:
            stack.append(self.root)  # root 노드에서 시작
            while stack:  # stack이 비어있지 않는 동안
                curr_node = stack.pop()
                print(curr_node.value, end=' ')
                if curr_node.right is not None:
                    stack.append(curr_node.right)
                if curr_node.left is not None:
                    stack.append(curr_node.left)
            print()
            return True

    # left->node->right
    def inorder(self):
        stack = []
        if self.root is None:
            return None
        else:
            curr_node = self.root

            while True:
                while curr_node is not None:
                    stack.append(curr_node)  # root node에서 시작해서
                    curr_node = curr_node.left  # 모든 가장 왼쪽 자식을 stack에 넣는다.
                curr_node = stack.pop()  # 가장 아래 왼쪽 자식부터 꺼내서
                print(curr_node.value, end=' ')  # 출력하고
                curr_node = curr_node.right  # 방금 꺼낸 자식의 오른쪽 자식부터 위를 반복한다.
                if curr_node is None and not stack:  # 스택도 비어있고, curr_node도 None이라서 더이사 stack에 들어갈 것이 없을 때
                    break  # while문을 나간다. = 종료한다. (스택만 비어있는 상태는 있을 수 있다.)

            print()

    # left-> right -> node

    def postorder(self):
        stack = []
        if self.root is None:
            return None
        else:
            curr_node = self.root
            while True:
                while curr_node is not None:
                    if curr_node.right is not None:
                        stack.append(curr_node.right)
                    stack.append(curr_node)
                    curr_node = curr_node.left
                curr_node = stack.pop()
                if curr_node.right is not None and stack and curr_node.right.value == stack[-1].value:
                    stack.pop()
                    stack.append(curr_node)
                    curr_node = curr_node.right
                else:
                    print(curr_node.value, end=' ')
                    curr_node = None
                if not stack:
                    break
            print()

    def bfs(self, value):
        queue = []
        if self.root is None:
            return False
        else:
            queue.append(self.root)
            while queue:
                curr_node = queue[0]
                queue = queue[1:]
                if curr_node.value == value:
                    return True
                if curr_node.left is not None:
                    queue.append(curr_node.left)
                if curr_node.right is not None:
                    queue.append(curr_node.right)

    def dfs(self, value):
        stack = []
        if self.root is None:
            return False
        else:
            stack.append(self.root)
            while stack:
                curr_node = stack.pop()
                if curr_node.value == value:
                    return True
                if curr_node.right is not None:
                    stack.append(curr_node.right)
                if curr_node.left is not None:
                    stack.append(curr_node.left)
            return False


arr = [n for n in range(1, 11)]
myBT = BinaryTree(arr)
myBT.preorder()
myBT.inorder()
myBT.postorder()
v = 2
if myBT.bfs(v) is True:
    print(v, "is in this Binary Tree")
else:
    print(v, "is not in this Binary Tree")
if myBT.dfs(v) is True:
    print(v, "is in this Binary Tree")
else:
    print(v, "is not in this Binary Tree")