"""
宽度优先搜索算法 open表 + closed表实现
@author : qiyubing
@date : 2020-05-26
"""
from collections import deque


class Node:
    def __init__(self, name):
        self.name = name

    # 节点名称
    name: str
    # 相邻节点
    adj_nodes = []
    # 上一节点
    pre_node = None

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return str(self)


# 初始化图节点信息
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
A.adj_nodes = [B, C]
B.adj_nodes = [A, D]
C.adj_nodes = [A]
D.adj_nodes = [B]
E.adj_nodes = [B]

open_list = deque()
open_list.append(A)
closed_list = list()
target = E

while len(open_list) != 0:
    current_node = open_list.popleft()
    print('当前节点：' + str(current_node))

    if current_node == target:
        print("搜索结束，找到目标节点" + str(current_node))
        break

    # 当前节点加入closed
    closed_list.append(current_node)
    print('将节点' + str(current_node) + '加入closed表')

    # 扩展当前节点的相邻节点加入open
    adj_nodes = []
    for node in current_node.adj_nodes:
        if node not in closed_list:
            node.pre_node = current_node
            adj_nodes.append(node)
    if len(adj_nodes) > 0:
        print('将节点' + str(adj_nodes) + '加入open表')
    open_list.extend(adj_nodes)
else:
    print("搜索结束，未找到节点")
    exit()

# 根据pre_node信息，找出搜索路径
path = []
print_now = target
while print_now != None:
    path.append(print_now)
    print_now = print_now.pre_node
path.reverse()
print("最终的有效路径为：" + str(path))
