# 941. Valid Mountain Array

## Easy



Given an array of integers `arr`, return _`true` if and only if it is a valid mountain array_.

Recall that arr is a mountain array if and only if:

* `arr.length >= 3`
* There exists some `i` with `0 < i < arr.length - 1` such that:
  * `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]`
  * `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

![](https://assets.leetcode.com/uploads/2019/10/20/hint\_valid\_mountain\_array.png)

&#x20;

**Example 1:**

<pre><code>Input: arr = [2,1]
<strong>Output:
</strong> false
</code></pre>

**Example 2:**

<pre><code>Input: arr = [3,5,5]
<strong>Output:
</strong> false
</code></pre>

**Example 3:**

<pre><code>Input: arr = [0,3,2,1]
<strong>Output:
</strong> true
</code></pre>

&#x20;

**Constraints:**

* `1 <= arr.length <= 104`
* `0 <= arr[i] <= 104`
