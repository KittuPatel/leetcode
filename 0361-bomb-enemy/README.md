# 361. Bomb Enemy

## Medium



Given an `m x n` matrix `grid` where each cell is either a wall `'W'`, an enemy `'E'` or empty `'0'`, return _the maximum enemies you can kill using one bomb_. You can only place the bomb in an empty cell.

The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since it is too strong to be destroyed.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/27/bomb1-grid.jpg)

<pre><code>Input: grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
<strong>Output:
</strong> 3
</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/27/bomb2-grid.jpg)

<pre><code>Input: grid = [["W","W","W"],["0","0","0"],["E","E","E"]]
<strong>Output:
</strong> 1
</code></pre>

&#x20;

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 500`
* `grid[i][j]` is either `'W'`, `'E'`, or `'0'`.
