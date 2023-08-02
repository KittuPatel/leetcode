# 108. Convert Sorted Array to Binary Search Tree

## Easy



Given an integer array `nums` where the elements are sorted in **ascending order**, convert _it to a **height-balanced** binary search tree_.

A **height-balanced** binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg)

<pre><code>Input: nums = [-10,-3,0,5,9]
<strong>Output:
</strong> [0,-3,9,-10,null,5]
<strong>Explanation:
</strong> [0,-10,5,null,-3,null,9] is also accepted:
</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/18/btree.jpg)

<pre><code>Input: nums = [1,3]
<strong>Output:
</strong> [3,1]
<strong>Explanation:
</strong> [1,null,3] and [3,1] are both height-balanced BSTs.
</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 104`
* `-104 <= nums[i] <= 104`
* `nums` is sorted in a **strictly increasing** order.
