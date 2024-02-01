# Tutorials
| Title                       | Description                       | Tutorial                                | Code | 
|-----------------------------|-----------------------------------|-----------------------------------------|------|
| Recursion                   | Recursion. Why is recursion hard? | [Youtube](https://youtu.be/vGattE85Gw0) | TBD  |
| Validate Binary Search Tree | Return value is boolean           | [Youtube](https://youtu.be/49Cl2l8oKLY) | TBD  |
| Lowest Common Ancestor      | Return value is tree node         | [Youtube](https://youtu.be/jcbNZbnRJxY) | TBD  |
| Merge Sort                  | Return value is array             | [Youtube](https://youtu.be/jBKZsMlfdP4) | TBD  |
| Reverse Linked List         | Return value is list node         | [Youtube](https://youtu.be/V9_dK5uEJnE) | TBD  |


# 1. Why is recursion hard?
Recursion is hard because you are not familiar with handling return value. You may have heard of "Divide and Conquer". People may already know how to **divide** it but they do not how to **conquer**. To master recursion, you need to master **conquer** as well.

# 2. Divide & Conquer
## 2-1. Divide
Let's solve one simple problem, "Pre Order Traversal"
```python
'''
   tree   1
         / \
        2   3

   print   : 1, 2, 3
'''
def preorder(root):
    print(root.val)
    preorder(root.left)
    preorder(root.right)

```
Isn't it simple? Print current node's value and move onto the next and right.

Let's solve one more problem. "Maximum Depth of Binary Tree"
```python
'''
   tree1  1
         / \
        2   3
         \
          4

   height is 3 !!!

   tree2  1
         / \
        2   3
         \   \
          4   5
               \
                6
   

   height is 4 !!!
'''
class Solution:
    def __init__(self):
        self.maxi = 0

    def sol(self, root, depth):
        if root:
            self.maxi = max(self.maxi, depth)
            self.sol(root.left, depth+1)
            self.sol(root.right, depth+1)

    def max_depth(self, root):
        self.sol(root, 1)
        return self.maxi
```
Most of people solve the problem like the above. Save current height onto the global variable.
However, can you solve without global variable?

## 2-2. Conquer
Divide is simple. To master the recursion, you need to master conquer.
Conquer is like a dominoes game. To success on dominoes game,
First, you should touch the first dominoes.

<img width="504" alt="image" src="https://github.com/yoongon/dsa/assets/38376255/e2a9bbe0-c467-4b97-8245-361fc6df1750">

Second, the relation between domino tiles should be closed enough to be collapsed

<img width="478" alt="image" src="https://github.com/yoongon/dsa/assets/38376255/56782b26-df51-4453-8426-a87f70a93fce">

Success !!!

<img width="549" alt="image" src="https://github.com/yoongon/dsa/assets/38376255/03a5a2be-54b9-4f8b-b192-37906f0c2201">



Conquer on Recursion is same.
First, focus on base cases.
Second, make a relation.
That's all! If you keep this two in mind, then you can solve all recursion problems.
Let's solve with the real problem.

# 3. Problems
## 3-1. Maximum Depth of Binary Tree
### Base Cases
Let's find out the base cases. Base case is the case you don't need
```python
if root is None:
   return 0
```
### Relation
Forget about the relation and focus on handling return values.
```python
l = self.max_depth(root.left)
r = self.max_depth(root.right)
return 1 + max(l, r)
```

### Hypothesis
Based on the above code, make an initial code, hypothesis.
```python
if root is None:
   return 0
l = self.max_depth(root.left)
r = self.max_depth(root.right)
return 1 + max(l, r)
```
### Test
Test your hypothesis by sketching it.
```python
"""
   tree1  1
         / \
        2   3
         \
          4

       r(1) R2
     /     \
   r(2)R2   r(3) R1
     \
     r(4)R1
    /  \
   R0  Ro
"""
```
### Finalize code
```python
class Solution:
    def max_depth(self, root) -> int:
        if root is None:
            return 0
        l = self.max_depth(root.left)
        r = self.max_depth(root.right)
        return 1 + max(l, r)
```

## 3.2 Validate Binary Search Tree
### Base Case
Let's find out the base cases. Base case is the case you don't need
```python
if not root:
   return True
if not (left_limit < root.val < right_limit):
   return True
```
### Relation
Forget about the relation and focus on handling return values.
```python
l = self.check(root.left, left_limit, root.val)
r = self.check(root.left, left_limit, root.val)
if l and r:
    return True
return False
```
### Hypothesis
Based on the above code, make an initial code, hypothesis.
```python
if not root:
    return True
if not (left_limit < root.val < right_limit):
   return True
l = self.check(root.left, left_limit, root.val)
r = self.check(root.left, left_limit, root.val)
if l and r:
    return True
return False
```

### Test
Test your hypothesis by sketching it.
```python
"""
        2
     /    \
    1     4
         / \
        3   5
        
      r(2, ll=-inf, rr=inf) L3
     /                          \
    r(1, ll=-inf, rr=2)          r(4, ll=-inf, rr=2)     
      /                  \
r(None, ll=-inf, rr=1) RT ....  
"""
```

### Finalize code
```python
class Solution:
    def check(self, root, left_limit, right_limit):
        if not root:
            return True

        return left_limit < root.val < right_limit \
            and self.check(root.left, left_limit, root.val) \
            and self.check(root.right, root.val, right_limit)

    def is_valid_bst(self, root) -> bool:
        return self.check(root, -math.inf, math.inf)
```
## 3.3 More Problems
please watch the tutorial videos