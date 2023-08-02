# 337. House Robber III

## Medium



The thief has found himself a new place for his thievery again. There is only one entrance to this area, called `root`.

Besides the `root`, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if **two directly-linked houses were broken into on the same night**.

Given the `root` of the binary tree, return _the maximum amount of money the thief can rob **without alerting the police**_.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/10/rob1-tree.jpg)

<pre><code>Input: root = [3,2,3,null,3,null,1]
<strong>Output:
</strong> 7
<strong>Explanation:
</strong> Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/10/rob2-tree.jpg)

<pre><code>Input: root = [3,4,5,1,3,null,1]
<strong>Output:
</strong> 9
<strong>Explanation:
</strong> Maximum amount of money the thief can rob = 4 + 5 = 9.
</code></pre>

&#x20;

**Constraints:**

* The number of nodes in the tree is in the range `[1, 104]`.
* `0 <= Node.val <= 104`
