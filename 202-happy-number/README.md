# 202. Happy Number

## Easy



Write an algorithm to determine if a number `n` is happy.

A **happy number** is a number defined by the following process:

* Starting with any positive integer, replace the number by the sum of the squares of its digits.
* Repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle** which does not include 1.
* Those numbers for which this process **ends in 1** are happy.

Return `true` _if_ `n` _is a happy number, and_ `false` _if not_.

&#x20;

**Example 1:**

<pre><code>Input: n = 19
<strong>Output:
</strong> true
<strong>Explanation:
</strong>12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
</code></pre>

**Example 2:**

<pre><code>Input: n = 2
<strong>Output:
</strong> false
</code></pre>

&#x20;

**Constraints:**

* `1 <= n <= 231 - 1`
