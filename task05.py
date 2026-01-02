import uuid
import heapq
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="#00008b"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


# =========================
# Tree visualization
# =========================

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is None:
        return

    graph.add_node(
        node.id,
        color=node.color,
        label=node.val
    )

    if node.left:
        graph.add_edge(node.id, node.left.id)
        left_x = x - 1 / 2 ** layer
        pos[node.left.id] = (left_x, y - 1)
        add_edges(graph, node.left, pos, left_x, y - 1, layer + 1)

    if node.right:
        graph.add_edge(node.id, node.right.id)
        right_x = x + 1 / 2 ** layer
        pos[node.right.id] = (right_x, y - 1)
        add_edges(graph, node.right, pos, right_x, y - 1, layer + 1)


def draw_tree_live(root, title, ax):
    ax.clear()

    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(tree, root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        node_color=colors,
        node_size=1500,   # smaller nodes
        arrows=False,
        ax=ax
    )

    ax.set_title(title)
    plt.pause(0.5)


# =========================
# Heap → Tree
# =========================

def build_heap_tree(heap, index=0):
    if index >= len(heap):
        return None

    node = Node(heap[index])
    node.left = build_heap_tree(heap, 2 * index + 1)
    node.right = build_heap_tree(heap, 2 * index + 2)

    return node


# =========================
# Color utility (blue shades)
# =========================

def generate_blue_color(step, total_steps):
    ratio = step / max(total_steps - 1, 1)

    dark_blue = (0, 0, 139)        # #00008B
    light_blue = (173, 216, 230)   # #ADD8E6

    r = int(dark_blue[0] + (light_blue[0] - dark_blue[0]) * ratio)
    g = int(dark_blue[1] + (light_blue[1] - dark_blue[1]) * ratio)
    b = int(dark_blue[2] + (light_blue[2] - dark_blue[2]) * ratio)

    return f"#{r:02x}{g:02x}{b:02x}"


def reset_colors(root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.color = "#00008b"
            stack.append(node.left)
            stack.append(node.right)


# =========================
# DFS (stack, no recursion)
# =========================

def dfs_visualization(root):
    reset_colors(root)

    plt.ion()
    fig, ax = plt.subplots(figsize=(8, 5))

    stack = [root]
    visited = []

    while stack:
        node = stack.pop()
        if node:
            visited.append(node)
            stack.append(node.right)
            stack.append(node.left)

    for i, node in enumerate(visited):
        node.color = generate_blue_color(i, len(visited))
        draw_tree_live(root, "DFS Traversal", ax)

    plt.ioff()
    plt.show()


# =========================
# BFS (queue, no recursion)
# =========================

def bfs_visualization(root):
    reset_colors(root)

    plt.ion()
    fig, ax = plt.subplots(figsize=(8, 5))

    queue = deque([root])
    visited = []

    while queue:
        node = queue.popleft()
        if node:
            visited.append(node)
            queue.append(node.left)
            queue.append(node.right)

    for i, node in enumerate(visited):
        node.color = generate_blue_color(i, len(visited))
        draw_tree_live(root, "BFS Traversal", ax)

    plt.ioff()
    plt.show()


# =========================
# Example
# =========================

if __name__ == "__main__":
    array = [9, 5, 6, 2, 3, 8, 1, 7]
    heapq.heapify(array)

    root = build_heap_tree(array)

    dfs_visualization(root)
    bfs_visualization(root)
