# 124. Binary Tree Maximum Path Sum

## Hard



A **path** in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence **at most once**. Note that the path does not need to pass through the root.

The **path sum** of a path is the sum of the node's values in the path.

Given the `root` of a binary tree, return _the maximum **path sum** of any **non-empty** path_.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg)

<pre><code>Input: root = [1,2,3]
<strong>Output:
</strong> 6
<strong>Explanation:
</strong> The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg)

<pre><code>Input: root = [-10,9,20,null,null,15,7]
<strong>Output:
</strong> 42
<strong>Explanation:
</strong> The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
</code></pre>

&#x20;

**Constraints:**

* The number of nodes in the tree is in the range `[1, 3 * 104]`.
* `-1000 <= Node.val <= 1000`
