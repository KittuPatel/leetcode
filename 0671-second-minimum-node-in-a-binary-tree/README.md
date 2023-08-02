# 671. Second Minimum Node In a Binary Tree

## Easy



Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly `two` or `zero` sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property `root.val = min(root.left.val, root.right.val)` always holds.

Given such a binary tree, you need to output the **second minimum** value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

&#x20;

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/15/smbt1.jpg)

<pre><code>Input: root = [2,2,5,null,null,5,7]
<strong>Output:
</strong> 5
<strong>Explanation:
</strong> The smallest value is 2, the second smallest value is 5.
</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/15/smbt2.jpg)

<pre><code>Input: root = [2,2,2]
<strong>Output:
</strong> -1
<strong>Explanation:
</strong> The smallest value is 2, but there isn't any second smallest value.
</code></pre>

&#x20;

**Constraints:**

* The number of nodes in the tree is in the range `[1, 25]`.
* `1 <= Node.val <= 231 - 1`
* `root.val == min(root.left.val, root.right.val)` for each internal node of the tree.
