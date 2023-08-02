# 1644. Lowest Common Ancestor of a Binary Tree II

## Medium



Given the `root` of a binary tree, return _the lowest common ancestor (LCA) of two given nodes,_ `p` _and_ `q`. If either node `p` or `q` **does not exist** in the tree, return `null`. All values of the nodes in the tree are **unique**.

According to the [**definition of LCA on Wikipedia**](https://en.wikipedia.org/wiki/Lowest\_common\_ancestor): "The lowest common ancestor of two nodes `p` and `q` in a binary tree `T` is the lowest node that has both `p` and `q` as **descendants** (where we allow **a node to be a descendant of itself**)". A **descendant** of a node `x` is a node `y` that is on the path from node `x` to some leaf node.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

<pre><code>Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
<strong>Output:
</strong> 3
<strong>Explanation:
</strong> The LCA of nodes 5 and 1 is 3.
</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

<pre><code>Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
<strong>Output:
</strong> 5
<strong>Explanation:
</strong> The LCA of nodes 5 and 4 is 5. A node can be a descendant of itself according to the definition of LCA.
</code></pre>

**Example 3:**

![](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

<pre><code>Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10
<strong>Output:
</strong> null
<strong>Explanation:
</strong> Node 10 does not exist in the tree, so return null.
</code></pre>

&#x20;

**Constraints:**

* The number of nodes in the tree is in the range `[1, 104]`.
* `-109 <= Node.val <= 109`
* All `Node.val` are **unique**.
* `p != q`

&#x20;

**Follow up:** Can you find the LCA traversing the tree, without checking nodes existence?
