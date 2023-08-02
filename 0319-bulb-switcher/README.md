# 319. Bulb Switcher

## Medium



There are `n` bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the `ith` round, you toggle every `i` bulb. For the `nth` round, you only toggle the last bulb.

Return _the number of bulbs that are on after `n` rounds_.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/05/bulb.jpg)

<pre><code>Input: n = 3
<strong>Output:
</strong> 1
<strong>Explanation:
</strong> At first, the three bulbs are [off, off, off].
After the first round, the three bulbs are [on, on, on].
After the second round, the three bulbs are [on, off, on].
After the third round, the three bulbs are [on, off, off]. 
So you should return 1 because there is only one bulb is on.
</code></pre>

**Example 2:**

<pre><code>Input: n = 0
<strong>Output:
</strong> 0
</code></pre>

**Example 3:**

<pre><code>Input: n = 1
<strong>Output:
</strong> 1
</code></pre>

&#x20;

**Constraints:**

* `0 <= n <= 109`
