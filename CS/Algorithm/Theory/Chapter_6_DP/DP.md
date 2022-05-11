
# 动态规划
## what it is
Dynamic Programming: 通过将原问题分解为相对简单的子问题的方式求解复杂问题的方法。
往往适用于<font color="purple">有重叠子问题和最优子结构性质的问题。</font>

```mermaid
graph LR;
复杂问题 --拆分--> 子问题 --memo--> 保存子问题答案 --反推--> 解决复杂问题
```
## 核心思想
1. 拆分子问题
2. memo
## 例子
    青蛙跳台阶问题：一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法
    f(n) = f(n-1) + f(n-2)
### 暴力递归
```python
class Solution:
    def numWays(self, n):
        if n == 0:
            return 1
        if n <= 2:
            return n
        return self.numWays(n-1) + self.numWays(n-2)
# O(2^n)
```
### 备忘录
```python
f_dict = {}
class Solution:
    def numWays(self, n):
        if n == 0:
            return 1
        if n <= 2:
            return n
        if f_dict.get(n, None):
            return f_dict[n]
        f_dict[n] = self.numWays(n-1) + self.numWays(n-2)
        return f_dict[n]%1000000007
```
### 动态规划
    状态转移方程：f(n) = f(n-1) + f(n-2)
    最优子结构：f(n)、f(n-1)、f(n-2)
    边界：f(1) = 1, f(2) = 2
    重叠子问题：f(10) = f(9) + f(8), f(9) = f(8) + f(7) => f(8)为重叠子问题
```python
class Solution:
    def numWays(self, n):
        l, g = 0, 1
        for i in range(n):
            l, g = g, l+g
        return g%1000000007
```
## 解题套路
### 应用范围
### 解题思路
1. 穷举分析
2. 确定边界
3. 规律 => 最优子结构
4. 状态转移方程
## leetcode