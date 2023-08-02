# 142. Linked List Cycle II

## Medium



Given the `head` of a linked list, return _the node where the cycle begins. If there is no cycle, return_ `null`.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to (**0-indexed**). It is `-1` if there is no cycle. **Note that** `pos` **is not passed as a parameter**.

**Do not modify** the linked list.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

<pre><code>Input: head = [3,2,0,-4], pos = 1
<strong>Output:
</strong> tail connects to node index 1
<strong>Explanation:
</strong> There is a cycle in the linked list, where tail connects to the second node.
</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist\_test2.png)

<pre><code>Input: head = [1,2], pos = 0
<strong>Output:
</strong> tail connects to node index 0
<strong>Explanation:
</strong> There is a cycle in the linked list, where tail connects to the first node.
</code></pre>

**Example 3:**

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist\_test3.png)

<pre><code>Input: head = [1], pos = -1
<strong>Output:
</strong> no cycle
<strong>Explanation:
</strong> There is no cycle in the linked list.
</code></pre>

&#x20;

**Constraints:**

* The number of the nodes in the list is in the range `[0, 104]`.
* `-105 <= Node.val <= 105`
* `pos` is `-1` or a **valid index** in the linked-list.

&#x20;

**Follow up:** Can you solve it using `O(1)` (i.e. constant) memory?
