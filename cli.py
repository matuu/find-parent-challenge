"""
Challenge exercise

We are building a command line tool to navigate the file system. We want to add a command that given two file paths,
can find the first parent folder that contains both paths.

So for example:

```bash
findParent "a/b/c" "a/b/d"
-> "/a/b"
```

Because filesystems might have aliases, we cannot use the file path to find the parent folder at a
glance. (i.e. /var might be pointing to /a/b). We need to find the parent folder by navigating the filesystem.

**Challenge**

Given an input that represents a filesystem, and two files, find the closest folder that contains both file paths.
"""


class FileNode:
    def __init__(self, name: str):
        self.children: list[FileNode] = []
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def add_child(self, node: "FileNode"):
        self.children.append(node)


def resolve_path(parent: FileNode, node: FileNode) -> list[FileNode]:
    """
    Resolves the path from parent to child.
    Using a recursive function, iterates over the tree structure, comparing the given node
    (as a parameter) with each node.
    When the desired node is found, it is returned, keeping the entire path to it.
    The result is the entire path between the first parent and the node.
    """
    if parent == node:
        return [node]

    for child in parent.children:
        result = resolve_path(child, node)
        if result:
            return [parent] + result
    return []


def find_parent(file_system: FileNode, node_1: FileNode, node_2: FileNode) -> FileNode | None:
    """
    Find the closest parent to both nodes in the file system.
    None is returned if some node do not exist in the file system.

    This function uses the resolve_path to retrieve the entire path from node_1 to node_2.
    Then, it iterates over the both path, node by node, until some of this is different.
    The result is the last common node.
    """
    path_to_node_1 = resolve_path(file_system, node_1)
    path_to_node_2 = resolve_path(file_system, node_2)
    shared_nodes = []
    for step_1, step_2 in zip(path_to_node_1, path_to_node_2):
        if step_1 == step_2:
            shared_nodes.append(step_1)
        else:
            break
    return shared_nodes[-1] if len(shared_nodes) > 0 else None
