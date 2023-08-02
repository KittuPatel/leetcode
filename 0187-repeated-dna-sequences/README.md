# 187. Repeated DNA Sequences

## Medium



The **DNA sequence** is composed of a series of nucleotides abbreviated as `'A'`, `'C'`, `'G'`, and `'T'`.

* For example, `"ACGAATTCCG"` is a **DNA sequence**.

When studying **DNA**, it is useful to identify repeated sequences within the DNA.

Given a string `s` that represents a **DNA sequence**, return all the **`10`-letter-long** sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in **any order**.

&#x20;

**Example 1:**

<pre><code>Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
<strong>Output:
</strong> ["AAAAACCCCC","CCCCCAAAAA"]
</code></pre>

**Example 2:**

<pre><code>Input: s = "AAAAAAAAAAAAA"
<strong>Output:
</strong> ["AAAAAAAAAA"]
</code></pre>

&#x20;

**Constraints:**

* `1 <= s.length <= 105`
* `s[i]` is either `'A'`, `'C'`, `'G'`, or `'T'`.
