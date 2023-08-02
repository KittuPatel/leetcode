# 1598. Crawler Log Folder

## Easy



The Leetcode file system keeps a log each time some user performs a _change folder_ operation.

The operations are described below:

* `"../"` : Move to the parent folder of the current folder. (If you are already in the main folder, **remain in the same folder**).
* `"./"` : Remain in the same folder.
* `"x/"` : Move to the child folder named `x` (This folder is **guaranteed to always exist**).

You are given a list of strings `logs` where `logs[i]` is the operation performed by the user at the `ith` step.

The file system starts in the main folder, then the operations in `logs` are performed.

Return _the minimum number of operations needed to go back to the main folder after the change folder operations._

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/09/sample\_11\_1957.png)

<pre><code>Input: logs = ["d1/","d2/","../","d21/","./"]
<strong>Output:
</strong> 2
<strong>Explanation: 
</strong>Use this change folder operation "../" 2 times and go back to the main folder.
</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/09/09/sample\_22\_1957.png)

<pre><code>Input: logs = ["d1/","d2/","./","d3/","../","d31/"]
<strong>Output:
</strong> 3
</code></pre>

**Example 3:**

<pre><code>Input: logs = ["d1/","../","../","../"]
<strong>Output:
</strong> 0
</code></pre>

&#x20;

**Constraints:**

* `1 <= logs.length <= 103`
* `2 <= logs[i].length <= 10`
* `logs[i]` contains lowercase English letters, digits, `'.'`, and `'/'`.
* `logs[i]` follows the format described in the statement.
* Folder names consist of lowercase English letters and digits.
