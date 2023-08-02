# 272. Closest Binary Search Tree Value II

## Hard



Given the `root` of a binary search tree, a `target` value, and an integer `k`, return _the_ `k` _values in the BST that are closest to the_ `target`. You may return the answer in **any order**.

You are **guaranteed** to have only one unique set of `k` values in the BST that are closest to the `target`.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/12/closest1-1-tree.jpg)

<pre><code>Input: root = [4,2,5,1,3], target = 3.714286, k = 2
<strong>Output:
</strong> [4,3]
</code></pre>

**Example 2:**

<pre><code>Input: root = [1], target = 0.000000, k = 1
<strong>Output:
</strong> [1]
</code></pre>

&#x20;

**Constraints:**

* The number of nodes in the tree is `n`.
* `1 <= k <= n <= 104`.
* `0 <= Node.val <= 109`
* `-109 <= target <= 109`

&#x20;

**Follow up:** Assume that the BST is balanced. Could you solve it in less than `O(n)` runtime (where `n = total nodes`)?
