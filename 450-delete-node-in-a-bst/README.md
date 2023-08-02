# 450. Delete Node in a BST

## Medium



Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return _the **root node reference** (possibly updated) of the BST_.

Basically, the deletion can be divided into two stages:

1. Search for a node to remove.
2. If the node is found, delete the node.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/04/del\_node\_1.jpg)

<pre><code>Input: root = [5,3,6,2,4,null,7], key = 3
<strong>Output:
</strong> [5,4,6,2,null,null,7]
<strong>Explanation:
</strong> Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
</code></pre>

**Example 2:**

<pre><code>Input: root = [5,3,6,2,4,null,7], key = 0
<strong>Output:
</strong> [5,3,6,2,4,null,7]
<strong>Explanation:
</strong> The tree does not contain a node with value = 0.
</code></pre>

**Example 3:**

<pre><code>Input: root = [], key = 0
<strong>Output:
</strong> []
</code></pre>

&#x20;

**Constraints:**

* The number of nodes in the tree is in the range `[0, 104]`.
* `-105 <= Node.val <= 105`
* Each node has a **unique** value.
* `root` is a valid binary search tree.
* `-105 <= key <= 105`

&#x20;

**Follow up:** Could you solve it with time complexity `O(height of tree)`?
