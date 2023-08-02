# 268. Missing Number

## Easy



Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return _the only number in the range that is missing from the array._

&#x20;

**Example 1:**

<pre><code>Input: nums = [3,0,1]
<strong>Output:
</strong> 2
<strong>Explanation:
</strong> n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
</code></pre>

**Example 2:**

<pre><code>Input: nums = [0,1]
<strong>Output:
</strong> 2
<strong>Explanation:
</strong> n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
</code></pre>

**Example 3:**

<pre><code>Input: nums = [9,6,4,2,3,5,7,0,1]
<strong>Output:
</strong> 8
<strong>Explanation:
</strong> n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
</code></pre>

&#x20;

**Constraints:**

* `n == nums.length`
* `1 <= n <= 104`
* `0 <= nums[i] <= n`
* All the numbers of `nums` are **unique**.

&#x20;

**Follow up:** Could you implement a solution using only `O(1)` extra space complexity and `O(n)` runtime complexity?
