# 149. Max Points on a Line

## Hard



Given an array of `points` where `points[i] = [xi, yi]` represents a point on the **X-Y** plane, return _the maximum number of points that lie on the same straight line_.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/25/plane1.jpg)

<pre><code>Input: points = [[1,1],[2,2],[3,3]]
<strong>Output:
</strong> 3
</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/25/plane2.jpg)

<pre><code>Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
<strong>Output:
</strong> 4
</code></pre>

&#x20;

**Constraints:**

* `1 <= points.length <= 300`
* `points[i].length == 2`
* `-104 <= xi, yi <= 104`
* All the `points` are **unique**.
