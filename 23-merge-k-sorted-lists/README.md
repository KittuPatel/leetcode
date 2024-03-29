# 23. Merge k Sorted Lists

## Hard



You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

_Merge all the linked-lists into one sorted linked-list and return it._

&#x20;

**Example 1:**

<pre><code>Input: lists = [[1,4,5],[1,3,4],[2,6]]
<strong>Output:
</strong> [1,1,2,3,4,4,5,6]
<strong>Explanation:
</strong> The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
</code></pre>

**Example 2:**

<pre><code>Input: lists = []
<strong>Output:
</strong> []
</code></pre>

**Example 3:**

<pre><code>Input: lists = [[]]
<strong>Output:
</strong> []
</code></pre>

&#x20;

**Constraints:**

* `k == lists.length`
* `0 <= k <= 104`
* `0 <= lists[i].length <= 500`
* `-104 <= lists[i][j] <= 104`
* `lists[i]` is sorted in **ascending order**.
* The sum of `lists[i].length` will not exceed `104`.
