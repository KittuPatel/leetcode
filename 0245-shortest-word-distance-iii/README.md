# 245. Shortest Word Distance III

## Medium



Given an array of strings `wordsDict` and two strings that already exist in the array `word1` and `word2`, return _the shortest distance between these two words in the list_.

**Note** that `word1` and `word2` may be the same. It is guaranteed that they represent **two individual words** in the list.

&#x20;

**Example 1:**

<pre><code>Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
<strong>Output:
</strong> 1
</code></pre>

**Example 2:**

<pre><code>Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "makes"
<strong>Output:
</strong> 3
</code></pre>

&#x20;

**Constraints:**

* `1 <= wordsDict.length <= 105`
* `1 <= wordsDict[i].length <= 10`
* `wordsDict[i]` consists of lowercase English letters.
* `word1` and `word2` are in `wordsDict`.
