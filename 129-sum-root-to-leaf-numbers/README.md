# 129. Sum Root to Leaf Numbers

## Medium



You are given the `root` of a binary tree containing digits from `0` to `9` only.

Each root-to-leaf path in the tree represents a number.

* For example, the root-to-leaf path `1 -> 2 -> 3` represents the number `123`.

Return _the total sum of all root-to-leaf numbers_. Test cases are generated so that the answer will fit in a **32-bit** integer.

A **leaf** node is a node with no children.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/num1tree.jpg)

<pre><code>Input: root = [1,2,3]
<strong>Output:
</strong> 25
<strong>Explanation:
</strong>The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/19/num2tree.jpg)

<pre><code>Input: root = [4,9,0,5,1]
<strong>Output:
</strong> 1026
<strong>Explanation:
</strong>The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
</code></pre>

&#x20;

**Constraints:**

* The number of nodes in the tree is in the range `[1, 1000]`.
* `0 <= Node.val <= 9`
* The depth of the tree will not exceed `10`.
