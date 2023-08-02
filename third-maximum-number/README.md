# Third Maximum Number



Given an integer array `nums`, return _the **third distinct maximum** number in this array. If the third maximum does not exist, return the **maximum** number_.

&#x20;

**Example 1:**

<pre><code>Input: nums = [3,2,1]
<strong>Output:
</strong> 1
<strong>Explanation:
</strong>The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
</code></pre>

**Example 2:**

<pre><code>Input: nums = [1,2]
<strong>Output:
</strong> 2
<strong>Explanation:
</strong>The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
</code></pre>

**Example 3:**

<pre><code>Input: nums = [2,2,3,1]
<strong>Output:
</strong> 1
<strong>Explanation:
</strong>The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 104`
* `-231 <= nums[i] <= 231 - 1`

&#x20;

**Follow up:** Can you find an `O(n)` solution?
