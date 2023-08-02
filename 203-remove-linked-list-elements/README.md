# 203. Remove Linked List Elements

## Easy



Given the `head` of a linked list and an integer `val`, remove all the nodes of the linked list that has `Node.val == val`, and return _the new head_.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/06/removelinked-list.jpg)

<pre><code>Input: head = [1,2,6,3,4,5,6], val = 6
<strong>Output:
</strong> [1,2,3,4,5]
</code></pre>

**Example 2:**

<pre><code>Input: head = [], val = 1
<strong>Output:
</strong> []
</code></pre>

**Example 3:**

<pre><code>Input: head = [7,7,7,7], val = 7
<strong>Output:
</strong> []
</code></pre>

&#x20;

**Constraints:**

* The number of nodes in the list is in the range `[0, 104]`.
* `1 <= Node.val <= 50`
* `0 <= val <= 50`
