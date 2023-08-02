# 606. Construct String from Binary Tree

## Easy



Given the `root` of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/05/03/cons1-tree.jpg)

<pre><code>Input: root = [1,2,3,4]
<strong>Output:
</strong> "1(2(4))(3)"
<strong>Explanation:
</strong> Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"
</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/05/03/cons2-tree.jpg)

<pre><code>Input: root = [1,2,3,null,4]
<strong>Output:
</strong> "1(2()(4))(3)"
<strong>Explanation:
</strong> Almost the same as the first example, except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
</code></pre>

&#x20;

**Constraints:**

* The number of nodes in the tree is in the range `[1, 104]`.
* `-1000 <= Node.val <= 1000`
