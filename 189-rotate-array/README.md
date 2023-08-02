# 189. Rotate Array

## Medium



Given an array, rotate the array to the right by `k` steps, where `k` is non-negative.

&#x20;

**Example 1:**

<pre><code>Input: nums = [1,2,3,4,5,6,7], k = 3
<strong>Output:
</strong> [5,6,7,1,2,3,4]
<strong>Explanation:
</strong>rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
</code></pre>

**Example 2:**

<pre><code>Input: nums = [-1,-100,3,99], k = 2
<strong>Output:
</strong> [3,99,-1,-100]
<strong>Explanation:
</strong> 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 105`
* `-231 <= nums[i] <= 231 - 1`
* `0 <= k <= 105`

&#x20;

**Follow up:**

* Try to come up with as many solutions as you can. There are at least **three** different ways to solve this problem.
* Could you do it in-place with `O(1)` extra space?
