# AVL Tree Implementation in Python

This is a clean implementation of an AVL Tree in Python. It was developed as part of a university assignment and includes core functionality like insertion, deletion, and balancing, along with advanced features like split and join.

## What's Included

- `AVLTree.py`: The main implementation file. It includes the `AVLTree` class and `AVLNode` class with all required methods.
- `info.txt`: Contains names and student IDs.
- `AVLTree_*.pdf`: Documentation file that explains the logic, time complexity, and includes experimental results.

## Features

- `insert(k, v)`: Inserts a key-value pair and returns how many rotations were done.
- `delete(node)`: Deletes the given node and returns the number of rotations.
- `search(k)`: Searches for a key and returns the node (or `None`).
- `avl_to_array()`: Returns a sorted list of key-value pairs.
- `size()`: Returns the number of nodes in the tree.
- `split(node)`: Splits the tree into two trees around the given node.
- `join(tree, k, v)`: Joins another tree with this one using a new node.
- `get_root()`: Returns the root node of the AVL tree.

## Notes

- Every real node has two virtual children (leaves).
- No external libraries or built-in data structures are used.
- Time complexity is optimal for all operations.

## Running the Code
This code is meant to be imported and used programmatically. It does not include a main function or user interface.

## Testing and Performance
The implementation was tested under various input sizes. `split` and `join` operations were analyzed both experimentally and theoretically.

---

Written for the Data Structures course at Tel Aviv University.

