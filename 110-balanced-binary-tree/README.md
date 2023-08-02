# 110. Balanced Binary Tree

## Easy



Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

> a binary tree in which the left and right subtrees of _every_ node differ in height by no more than 1.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/06/balance\_1.jpg)

<pre><code>Input: root = [3,9,20,null,null,15,7]
<strong>Output:
</strong> true
</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/06/balance\_2.jpg)

<pre><code>Input: root = [1,2,2,3,3,null,null,4,4]
<strong>Output:
</strong> false
</code></pre>

**Example 3:**

<pre><code>Input: root = []
<strong>Output:
</strong> true
</code></pre>

&#x20;

**Constraints:**

* The number of nodes in the tree is in the range `[0, 5000]`.
* `-104 <= Node.val <= 104`
