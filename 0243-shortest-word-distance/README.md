# 243. Shortest Word Distance

## Easy



Given an array of strings `wordsDict` and two different strings that already exist in the array `word1` and `word2`, return _the shortest distance between these two words in the list_.

&#x20;

**Example 1:**

<pre><code>Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
<strong>Output:
</strong> 3
</code></pre>

**Example 2:**

<pre><code>Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
<strong>Output:
</strong> 1
</code></pre>

&#x20;

**Constraints:**

* `2 <= wordsDict.length <= 3 * 104`
* `1 <= wordsDict[i].length <= 10`
* `wordsDict[i]` consists of lowercase English letters.
* `word1` and `word2` are in `wordsDict`.
* `word1 != word2`
