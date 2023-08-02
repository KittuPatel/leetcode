# 360. Sort Transformed Array

## Medium



Given a **sorted** integer array `nums` and three integers `a`, `b` and `c`, apply a quadratic function of the form `f(x) = ax2 + bx + c` to each element `nums[i]` in the array, and return _the array in a sorted order_.

&#x20;

**Example 1:**

<pre><code>Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
<strong>Output:
</strong> [3,9,15,33]
</code></pre>

**Example 2:**

<pre><code>Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
<strong>Output:
</strong> [-23,-5,1,7]
</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 200`
* `-100 <= nums[i], a, b, c <= 100`
* `nums` is sorted in **ascending** order.

&#x20;

**Follow up:** Could you solve it in `O(n)` time?
