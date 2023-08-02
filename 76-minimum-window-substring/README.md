# 76. Minimum Window Substring

## Hard



Given two strings `s` and `t` of lengths `m` and `n` respectively, return _the **minimum window substring** of_ `s` _such that every character in_ `t` _(**including duplicates**) is included in the window. If there is no such substring, return the empty string_ `""`_._

The testcases will be generated such that the answer is **unique**.

A **substring** is a contiguous sequence of characters within the string.

&#x20;

**Example 1:**

<pre><code>Input: s = "ADOBECODEBANC", t = "ABC"
<strong>Output:
</strong> "BANC"
<strong>Explanation:
</strong> The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
</code></pre>

**Example 2:**

<pre><code>Input: s = "a", t = "a"
<strong>Output:
</strong> "a"
<strong>Explanation:
</strong> The entire string s is the minimum window.
</code></pre>

**Example 3:**

<pre><code>Input: s = "a", t = "aa"
<strong>Output:
</strong> ""
<strong>Explanation:
</strong> Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
</code></pre>

&#x20;

**Constraints:**

* `m == s.length`
* `n == t.length`
* `1 <= m, n <= 105`
* `s` and `t` consist of uppercase and lowercase English letters.

&#x20;

**Follow up:** Could you find an algorithm that runs in `O(m + n)` time?
