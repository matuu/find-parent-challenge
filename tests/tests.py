import pytest

from cli import FileNode, find_parent, resolve_path


@pytest.fixture
def root():
    """
    root
    |__a
       |__c
          |__y
       |__d
          |__ z
    |__b
       |__x
    """
    root = FileNode("root")
    node_a, node_b, node_c, node_d, node_x, node_y, node_z = tuple(FileNode(x) for x in "abcdxyz")
    root.add_child(node_a)
    root.add_child(node_b)
    node_a.add_child(node_c)
    node_a.add_child(node_d)
    node_b.add_child(node_x)
    node_c.add_child(node_y)
    node_d.add_child(node_z)
    return root


def test_resolve_path_from_root(root):
    node_a = root.children[0]
    node_d = node_a.children[1]
    node_z = node_d.children[0]

    assert resolve_path(root, node_z) == [root, node_a, node_d, node_z]


def test_resolve_path_from_node(root):
    node_a = root.children[0]
    node_c = node_a.children[0]
    node_y = node_c.children[0]

    assert resolve_path(node_a, node_y) == [node_a, node_c, node_y]


def test_example_structure():
    """
    root ->
        a ->
            c
            d
        b
    """
    root = FileNode("root")
    node_a, node_b, node_c, node_d = tuple(FileNode(x) for x in "abcd")

    root.add_child(node_a)
    root.add_child(node_b)
    node_a.add_child(node_c)
    node_a.add_child(node_d)

    assert find_parent(root, node_a, node_b) == root
    assert find_parent(root, node_c, node_d) == node_a


def test_four_levels_structure(root):
    node_a = root.children[0]
    node_b = root.children[1]
    node_c = node_a.children[0]
    node_d = node_a.children[1]
    node_y = node_c.children[0]
    node_x = node_b.children[0]
    node_z = node_d.children[0]
    assert find_parent(root, node_a, node_c) == node_a
    assert find_parent(root, node_c, node_y) == node_c
    assert find_parent(root, node_d, node_c) == find_parent(root, node_c, node_d) == node_a
    assert find_parent(root, node_x, node_y) == root
    assert find_parent(root, node_z, node_y) == node_a


def test_not_exist_node(root):
    node_a = root.children[0]
    node_j = FileNode("j")

    assert find_parent(root, node_a, node_j) is None
