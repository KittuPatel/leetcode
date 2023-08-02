# 156. Binary Tree Upside Down

## Medium



Given the `root` of a binary tree, turn the tree upside down and return _the new root_.

You can turn a binary tree upside down with the following steps:

1. The original left child becomes the new root.
2. The original root becomes the new right child.
3. The original right child becomes the new left child.

![](https://assets.leetcode.com/uploads/2020/08/29/main.jpg)

The mentioned steps are done level by level. It is **guaranteed** that every right node has a sibling (a left node with the same parent) and has no children.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/08/29/updown.jpg)

<pre><code>Input: root = [1,2,3,4,5]
<strong>Output:
</strong> [4,5,2,null,null,3,1]
</code></pre>

**Example 2:**

<pre><code>Input: root = []
<strong>Output:
</strong> []
</code></pre>

**Example 3:**

<pre><code>Input: root = [1]
<strong>Output:
</strong> [1]
</code></pre>

&#x20;

**Constraints:**

* The number of nodes in the tree will be in the range `[0, 10]`.
* `1 <= Node.val <= 10`
* Every right node in the tree has a sibling (a left node that shares the same parent).
* Every right node in the tree has no children.
