# 205. Isomorphic Strings

## Easy



Given two strings `s` and `t`, _determine if they are isomorphic_.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

&#x20;

**Example 1:**

<pre><code><strong>Input: s = "egg", t = "add"
</strong><strong>Output: true
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: s = "foo", t = "bar"
</strong><strong>Output: false
</strong></code></pre>

**Example 3:**

<pre><code><strong>Input: s = "paper", t = "title"
</strong><strong>Output: true
</strong></code></pre>

&#x20;

**Constraints:**

* `1 <= s.length <= 5 * 104`
* `t.length == s.length`
* `s` and `t` consist of any valid ascii character.
