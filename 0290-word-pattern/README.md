# 290. Word Pattern

## Easy



Given a `pattern` and a string `s`, find if `s` follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in `pattern` and a non-empty word in `s`.

&#x20;

**Example 1:**

<pre><code><strong>Input: pattern = "abba", s = "dog cat cat dog"
</strong><strong>Output: true
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: pattern = "abba", s = "dog cat cat fish"
</strong><strong>Output: false
</strong></code></pre>

**Example 3:**

<pre><code><strong>Input: pattern = "aaaa", s = "dog cat cat dog"
</strong><strong>Output: false
</strong></code></pre>

&#x20;

**Constraints:**

* `1 <= pattern.length <= 300`
* `pattern` contains only lower-case English letters.
* `1 <= s.length <= 3000`
* `s` contains only lowercase English letters and spaces `' '`.
* `s` **does not contain** any leading or trailing spaces.
* All the words in `s` are separated by a **single space**.
