class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    self.leftLevel = 0
    self.rightLevel = 0
  
def prettyPrint():
  # First tree
  #        4
  #    1      2
  #  3 
  # root = TreeNode(4)
  # one = TreeNode(1)
  # two = TreeNode(2)
  # three = TreeNode(3)
  # root.left = one
  # root.right = two
  # one.left = three

  # Second Tree
  #        5
  #    1       2
  #  3       6   7 
  three = TreeNode(3)
  six = TreeNode(6)
  seven = TreeNode(7)
  one = TreeNode(1, three, None)
  two = TreeNode(2, six, seven)
  root = TreeNode(5, one, two)

  def fillItemCount(node, level):
    if not node: return level-1
    maxi = max(fillItemCount(node.left, level+1), fillItemCount(node.right, level+1))
    node.leftLevel = maxi
    node.rightLevel = maxi
    return max(node.leftLevel, node.rightLevel)
  fillItemCount(root, 0)

  print(one.leftLevel) # 2
  print(root.leftLevel) # 2
  print(root.rightLevel) # 1
  print(six.leftLevel) # 2

  ans = []
  def formPretty(node, level):
    if not node: return
    if level >= len(ans):
      ans.append([])
    leftLevel = node.leftLevel - level
    rightLevel = node.rightLevel - level
    ans[level] += [" "]*(2**leftLevel-1) + [str(node.val)] + [" "]*level +[" "]*(2**rightLevel-1)
    formPretty(node.left, level+1)
    formPretty(node.right, level+1)
    return 
  formPretty(root, 0)

  for each in ans:
    print("".join(each))
  print(ans)
prettyPrint()