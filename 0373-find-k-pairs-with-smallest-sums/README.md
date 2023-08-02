# 373. Find K Pairs with Smallest Sums

## Medium



You are given two integer arrays `nums1` and `nums2` sorted in **ascending order** and an integer `k`.

Define a pair `(u, v)` which consists of one element from the first array and one element from the second array.

Return _the_ `k` _pairs_ `(u1, v1), (u2, v2), ..., (uk, vk)` _with the smallest sums_.

&#x20;

**Example 1:**

<pre><code>Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
<strong>Output:
</strong> [[1,2],[1,4],[1,6]]
<strong>Explanation:
</strong> The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
</code></pre>

**Example 2:**

<pre><code>Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
<strong>Output:
</strong> [[1,1],[1,1]]
<strong>Explanation:
</strong> The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
</code></pre>

**Example 3:**

<pre><code>Input: nums1 = [1,2], nums2 = [3], k = 3
<strong>Output:
</strong> [[1,3],[2,3]]
<strong>Explanation:
</strong> All possible pairs are returned from the sequence: [1,3],[2,3]
</code></pre>

&#x20;

**Constraints:**

* `1 <= nums1.length, nums2.length <= 105`
* `-109 <= nums1[i], nums2[i] <= 109`
* `nums1` and `nums2` both are sorted in **ascending order**.
* `1 <= k <= 104`
