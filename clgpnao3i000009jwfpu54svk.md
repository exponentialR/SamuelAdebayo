---
title: "Day 2 [Blind 75][LeetCode] Maximizing Profit from Buying and Selling Stocks"
seoTitle: "Solving the Maximum Profit Stock Problem with One-Pass Approach"
seoDescription: "Learn to solve the maximum profit stock problem with a simple and efficient one-pass approach. A step-by-step guide with Python code implementation."
datePublished: Thu Apr 20 2023 21:39:06 GMT+0000 (Coordinated Universal Time)
cuid: clgpnao3i000009jwfpu54svk
slug: blind-75-day2-maximizing-profit-from-buying-and-selling-stocks
tags: python, python3, technical-interview, leetcode75, codinginterview

---

# Introduction
Welcome to Day 2 of the Blind 75 Challenge! Today I will be tackling the problem of finding the maximum profit by buying and selling stock once, a common problem in algorithm interviews and coding competitions. In this blogpost, I will explore a simple and efficient algorithm to solve this problem in Python, using only one pass/iteration through the array of stock prices.

# Problem
You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.
You want to maximize your profit by choosing a *single day* to buy one stock and choosing a *different day in the future* to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Problem Definition and Explanation 
In this question, we are given an array of stock prices, where each element in the array represents the price in a particular day, and the `ith` index location of a day of the stock price corresponds the the `ith` day. We are expected to find a solution that will provide the maximum profit. The maximum profit here is defined as the largest difference between the largest positive number between the selling price and the buying price. As it is we would want to maximize the profit by buying the stock on one day and selling it on a different day in the future. 

For example given the array below
```python
[1, 2, 3, 7, 4, 3]
```
The maximum profit would be `6`. Since the minimum price in the array is `1` and the maximum price is `7` (which comes at a later day).
Again, the task is to find the solution that gets the maximum profit from the array.

# Intuition behind the solution
**Naive solution**
One possible approach for finding the maximum profit by buying and selling stock is to first find the minimum and maximum values in the array and then calculate the difference between them. This can be implemented as follows:

```python
minimum_price = min(input_list)
maximum_[price = max(input_list)
```
Then get the maximum profit by finding the difference between the maximum price and minimum price. 
```python
maximum_profit = maximum price -minimum price
```
While finding the minimum and maximum values in the array and subtracting them to get the maximum profit might work in some cases, it is not a correct solution in all cases. This approach is not always correct as it fails to consider cases where buying the stock on a day preceding the selling day would result in a greater profit.

Consider the following example:
```python
[3, 2, 6, 5, 0, 3]
```

If we simply find the minimum value (0) and the maximum value (6), we would get a profit of 6 - 0 = 6, which is incorrect. The correct maximum profit that can be made in this case is 6 - 2 = 4, by buying the stock on day 2 (price 2) and selling it on day 3 (price 6). Since you can only buy on a day preceding the selling day. 
Therefore, finding the minimum and maximum values in the array and subtracting them is not a correct solution for this problem. Instead, we need to use an algorithm that finds the maximum profit that can be made by buying and selling the stock once. 

**Using One-Pass Algorithm** 

To overcome the limitations of the naive approach, a one-pass algorithm can be used. This algorithm processes each element of the data structure only once and keeps track of the minimum price seen so far and the maximum profit that can be made from selling the stock at the current price.

Here are the steps for implementing the one-pass algorithm:
1. First check if the list is empty. If empty return 0 as maximum profit.
```python
if not prices: 
    return 0
```
2. Initialize the minimum price to the first element in the array.
```python
maximum_profit = 0
```

3. Traverse through the array.
```python
for price in input_list:
```

4. Check if the current price is lower than the minimum price.
```python
    if price < minimum_price:
```

5. If it is, update the minimum price (since no profit can be made from a lower price.
```python
      minimum_price = price
```

6. Else calculate the profit that can be made by selling the stock at the current price. This is the difference between the current price and the minimum price so far.
```python
           else:
                  profit = price - minimum_price
```

7. Finally, compare the current profit with the maximum profit seen so far and update the profit if the current profit is greater.
```python
            if profit > maximum_profit_seen:
                maximum_profit_seen = profit
```

8. Return the maximum profit obtained.
```python
return maximum_profit_seen

Using this algorithm, we can find the maximum profit that can be made by buying and selling the stock once, taking into account the constraint that the buying day must precede the selling day.

# Putting it altogether - Code
```python
def maximum_profit_buy(input_list: list):
    # Check if the input list is empty
    if len (input_list) == 0:
        return 0

    # Initialize the minimum price and maximum profit seen so far
    minimum_price = input_list[0]
    maximum_profit_seen = 0

    # Traverse through the input list
    for price in input_list:
        # Update the minimum price seen so far
        if price < minimum_price:
            minimum_price = price
        else:
            # Calculate the profit that can be made by selling at the current price
            profit = price - minimum_price
            # Update the maximum profit seen so far if the current profit is greater
            if profit > maximum_profit_seen:
                maximum_profit_seen = profit

    # Return the maximum profit seen so far
    return maximum_profit_seen

```
# Testing 
Let's test the `maximum_profit_buy` function:
```python
print(maximum_profit_buy([7,6,4,3,1])) # Expected output: 0
print (maximum_profit_buy ([1, 2, 3, 7, 4, 3])) # Expected Output 6
```
The First test case represents the array `[7,6,4,3,1]`, where the stock price decreases every day. In this case, no profit can be made, so the expected output is `0`. For the second test case, we have an array `[1, 2, 3, 7, 4, 3]` and the maximum profit that can be made by buying stock on `day 1` `price 1` is and selling it on `day 4` `price 7` is 6 which is the expected output.

# Time and Space Complexity
The function has a time complexity of O(n), where n is the length if the input array. This is so since we need to iterate through the array only once. The space complexity is O(1) since we only use a constant amount of extra space to store the minimum price seen so far and the maximum profit.

# Use cases
The problem of finding the maximum profit by buying and selling a stock once is a common problem in coding interviews and competitions. It can also be used in finance and economics to analyze the performance of stocks and investments.

# Conclusion
In this blog post, we explored a simple and efficient algorithm to solve the problem of finding the maximum profit that can be made by buying and selling a stock once. By using the one-pass approach and keeping track of the minimum price seen so far and the maximum profit that can be made by selling the stock at the current price, we can solve this problem in O(n) time complexity, where n is the length of the input array.