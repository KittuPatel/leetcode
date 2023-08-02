# 567. Permutation in String

## Medium



Given two strings `s1` and `s2`, return `true` _if_ `s2` _contains a permutation of_ `s1`_, or_ `false` _otherwise_.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

&#x20;

**Example 1:**

<pre><code>Input: s1 = "ab", s2 = "eidbaooo"
<strong>Output:
</strong> true
<strong>Explanation:
</strong> s2 contains one permutation of s1 ("ba").
</code></pre>

**Example 2:**

<pre><code>Input: s1 = "ab", s2 = "eidboaoo"
<strong>Output:
</strong> false
</code></pre>

&#x20;

**Constraints:**

* `1 <= s1.length, s2.length <= 104`
* `s1` and `s2` consist of lowercase English letters.
