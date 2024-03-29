# 18. 4Sum

## Medium



Given an array `nums` of `n` integers, return _an array of all the **unique** quadruplets_ `[nums[a], nums[b], nums[c], nums[d]]` such that:

* `0 <= a, b, c, d < n`
* `a`, `b`, `c`, and `d` are **distinct**.
* `nums[a] + nums[b] + nums[c] + nums[d] == target`

You may return the answer in **any order**.

&#x20;

**Example 1:**

<pre><code>Input: nums = [1,0,-1,0,-2,2], target = 0
<strong>Output:
</strong> [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
</code></pre>

**Example 2:**

<pre><code>Input: nums = [2,2,2,2,2], target = 8
<strong>Output:
</strong> [[2,2,2,2]]
</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 200`
* `-109 <= nums[i] <= 109`
* `-109 <= target <= 109`
