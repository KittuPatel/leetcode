# 953. Verifying an Alien Dictionary

## Easy



In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different `order`. The `order` of the alphabet is some permutation of lowercase letters.

Given a sequence of `words` written in the alien language, and the `order` of the alphabet, return `true` if and only if the given `words` are sorted lexicographically in this alien language.

&#x20;

**Example 1:**

<pre><code>Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
<strong>Output:
</strong> true
<strong>Explanation: 
</strong>As 'h' comes before 'l' in this language, then the sequence is sorted.
</code></pre>

**Example 2:**

<pre><code>Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
<strong>Output:
</strong> false
<strong>Explanation: 
</strong>As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
</code></pre>

**Example 3:**

<pre><code>Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
<strong>Output:
</strong> false
<strong>Explanation: 
</strong>The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
</code></pre>

&#x20;

**Constraints:**

* `1 <= words.length <= 100`
* `1 <= words[i].length <= 20`
* `order.length == 26`
* All characters in `words[i]` and `order` are English lowercase letters.
