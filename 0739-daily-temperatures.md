# 739. Daily Temperatures

## Medium

***

Given an array of integers `temperatures` represents the daily temperatures, return _an array_ `answer` _such that_ `answer[i]` _is the number of days you have to wait after the_ `ith` _day to get a warmer temperature_. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

&#x20;

**Example 1:**

<pre><code><strong>Input: temperatures = [73,74,75,71,69,72,76,73]
</strong><strong>Output: [1,1,4,2,1,1,0,0]
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: temperatures = [30,40,50,60]
</strong><strong>Output: [1,1,1,0]
</strong></code></pre>

**Example 3:**

<pre><code><strong>Input: temperatures = [30,60,90]
</strong><strong>Output: [1,1,0]
</strong></code></pre>

&#x20;

**Constraints:**

* `1 <= temperatures.length <= 105`
* `30 <= temperatures[i] <= 100`
