import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import colorsys
import sys


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Функція для додавання вузлів та їх ребер"""
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, color_map=None):
    """Функція для відображення дерева"""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    if color_map is None:
        color_map = {node.id: node.color for node in tree.nodes(data=True)}
    colors = [color_map.get(node, "skyblue") for node in tree.nodes]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def generate_color_gradient(n):
    """Генерує градієнт кольорів від темного до світлого"""
    colors = []
    for i in range(n):
        hue = 0.6  # синій колір у моделі HSV
        saturation = 0.8  # насиченість
        value = 0.3 + (0.7 * i / (n - 1))  # змінюємо яскравість
        rgb = colorsys.hsv_to_rgb(hue, saturation, value)
        hex_color = '#%02x%02x%02x' % (int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))
        colors.append(hex_color)
    return colors


def bfs_traversal(root):
    """Обхід в ширину (BFS)"""
    queue = deque([root])
    visited_order = []
    while queue:
        node = queue.popleft()
        visited_order.append(node)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return visited_order


def dfs_traversal(root):
    """Обхід в глибину (DFS)"""
    stack = [root]
    visited_order = []    
    while stack:
        node = stack.pop()
        visited_order.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return visited_order


def visualize_traversal(root, traversal_type="bfs"):
    """Функція для візуалізації"""
    if traversal_type == "bfs":
        order = bfs_traversal(root)
    elif traversal_type == "dfs":
        order = dfs_traversal(root)
    else:
        raise ValueError("Invalid traversal type. Use 'bfs' or 'dfs'.")
    # Генерація кольорової послідовності для вузлів
    colors = generate_color_gradient(len(order))
    color_map = {node.id: color for node, color in zip(order, colors)}
    # Візуалізація дерева з кольоровою картою
    draw_tree(root, color_map)


# Main
if __name__ == '__main__':
    try:
        # Створення дерева
        root = Node(0)
        root.left = Node(4)
        root.left.left = Node(5)
        root.left.right = Node(10)
        root.right = Node(1)
        root.right.left = Node(3)
        print("Обхід в ширину (BFS):")
        visualize_traversal(root, traversal_type="bfs")
        print("Обхід в глибину (DFS):")
        visualize_traversal(root, traversal_type="dfs")
    except (ValueError) as e:
        print(f'Something went wrong, {e}')
        sys.exit(0)
