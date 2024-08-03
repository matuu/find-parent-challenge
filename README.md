# Find parent challenge

Read [challenge.md](challenge.md)

Check [tests.py](tests%2Ftests.py) to see how it works.

Here an example (the same of the challenge give):

```python
"""
root ->
    a ->
        c
        d
    b
"""
from cli import FileNode, find_parent

root = FileNode("root")
node_a, node_b, node_c, node_d = tuple(FileNode(x) for x in "abcd")

root.add_child(node_a)
root.add_child(node_b)
node_a.add_child(node_c)
node_a.add_child(node_d)

assert find_parent(root, node_a, node_b) == root
assert find_parent(root, node_c, node_d) == node_a
```

