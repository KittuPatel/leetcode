# 653. Two Sum IV - Input is a BST

## Easy



Given the `root` of a Binary Search Tree and a target number `k`, return _`true` if there exist two elements in the BST such that their sum is equal to the given target_.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/21/sum\_tree\_1.jpg)

<pre><code>Input: root = [5,3,6,2,4,null,7], k = 9
<strong>Output:
</strong> true
</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/09/21/sum\_tree\_2.jpg)

<pre><code>Input: root = [5,3,6,2,4,null,7], k = 28
<strong>Output:
</strong> false
</code></pre>

&#x20;

**Constraints:**

* The number of nodes in the tree is in the range `[1, 104]`.
* `-104 <= Node.val <= 104`
* `root` is guaranteed to be a **valid** binary search tree.
* `-105 <= k <= 105`
