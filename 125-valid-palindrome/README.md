# 125. Valid Palindrome

## Easy



A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` _if it is a **palindrome**, or_ `false` _otherwise_.

&#x20;

**Example 1:**

<pre><code>Input: s = "A man, a plan, a canal: Panama"
<strong>Output:
</strong> true
<strong>Explanation:
</strong> "amanaplanacanalpanama" is a palindrome.
</code></pre>

**Example 2:**

<pre><code>Input: s = "race a car"
<strong>Output:
</strong> false
<strong>Explanation:
</strong> "raceacar" is not a palindrome.
</code></pre>

**Example 3:**

<pre><code>Input: s = " "
<strong>Output:
</strong> true
<strong>Explanation:
</strong> s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
</code></pre>

&#x20;

**Constraints:**

* `1 <= s.length <= 2 * 105`
* `s` consists only of printable ASCII characters.
