# 1929. Concatenation of Array

## Easy



Given an integer array `nums` of length `n`, you want to create an array `ans` of length `2n` where `ans[i] == nums[i]` and `ans[i + n] == nums[i]` for `0 <= i < n` (**0-indexed**).

Specifically, `ans` is the **concatenation** of two `nums` arrays.

Return _the array_ `ans`.

&#x20;

**Example 1:**

<pre><code><strong>Input: nums = [1,2,1]
</strong><strong>Output: [1,2,1,1,2,1]
</strong><strong>Explanation: The array ans is formed as follows:
</strong>- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
</code></pre>

**Example 2:**

<pre><code><strong>Input: nums = [1,3,2,1]
</strong><strong>Output: [1,3,2,1,1,3,2,1]
</strong><strong>Explanation: The array ans is formed as follows:
</strong>- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
</code></pre>

&#x20;

**Constraints:**

* `n == nums.length`
* `1 <= n <= 1000`
* `1 <= nums[i] <= 1000`
