# 572. Subtree of Another Tree

## Easy



Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot` and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg)

<pre><code>Input: root = [3,4,5,1,2], subRoot = [4,1,2]
<strong>Output:
</strong> true
</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg)

<pre><code>Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
<strong>Output:
</strong> false
</code></pre>

&#x20;

**Constraints:**

* The number of nodes in the `root` tree is in the range `[1, 2000]`.
* The number of nodes in the `subRoot` tree is in the range `[1, 1000]`.
* `-104 <= root.val <= 104`
* `-104 <= subRoot.val <= 104`
