# 912. Sort an Array

## Medium



Given an array of integers `nums`, sort the array in ascending order and return it.

You must solve the problem **without using any built-in** functions in `O(nlog(n))` time complexity and with the smallest space complexity possible.

&#x20;

**Example 1:**

<pre><code><strong>Input: nums = [5,2,3,1]
</strong><strong>Output: [1,2,3,5]
</strong><strong>Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: nums = [5,1,1,2,0,0]
</strong><strong>Output: [0,0,1,1,2,5]
</strong><strong>Explanation: Note that the values of nums are not necessairly unique.
</strong></code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 5 * 104`
* `-5 * 104 <= nums[i] <= 5 * 104`
