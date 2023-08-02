# 796. Rotate String

## Easy



Given two strings `s` and `goal`, return `true` _if and only if_ `s` _can become_ `goal` _after some number of **shifts** on_ `s`.

A **shift** on `s` consists of moving the leftmost character of `s` to the rightmost position.

* For example, if `s = "abcde"`, then it will be `"bcdea"` after one shift.

&#x20;

**Example 1:**

<pre><code>Input: s = "abcde", goal = "cdeab"
<strong>Output:
</strong> true
</code></pre>

**Example 2:**

<pre><code>Input: s = "abcde", goal = "abced"
<strong>Output:
</strong> false
</code></pre>

&#x20;

**Constraints:**

* `1 <= s.length, goal.length <= 100`
* `s` and `goal` consist of lowercase English letters.
