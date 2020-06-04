# given a binary tree, check if it is a BST
# BST properties:
# 1- All left node keys are less than the current node
# 2- All right node keys are greater than the current node
# 3- All children trees are BST's

tree = []
tree_vals = []

def inorder(tree):
  if tree != None:
    inorder(tree.getLeftChild())
    tree_vals.append(tree.getRootVal())
    inorder(tree.getRightChild())

def check(tree_vals):
  return tree_vals == sorted(tree_vals)

inorder(tree)
check(tree_vals)