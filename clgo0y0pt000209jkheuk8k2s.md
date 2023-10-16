---
title: "Day 1 [Blind 75][LeetCode] Two Sum Problem: Using Hash Tables to Find Pairs of Integers That Add Up to a Target Value"
seoTitle: "Solving the Two-Sum Problem in Python: A Step-by-Step Guide."
seoDescription: "Learn how to solve the Two-Sum problem in Python with our step-by-step guide. Efficient, scalable, and perfect for software engineering interviews."
datePublished: Wed Apr 19 2023 18:25:38 GMT+0000 (Coordinated Universal Time)
cuid: clgo0y0pt000209jkheuk8k2s
slug: blind75-day1-two-sum-python
tags: python, python3, leetcode, technical-interview, leetcode-solution

---

# Problem 
Given an array of integers `num`  and an integer `target`, return indices of the two numbers such that they add up to `target`.
You may assume that each input would have exactly one solution and you may not use the same element twice.
You can assume that the given input array is not sorted.

# Problem definition and explanation.
The two-sum problem as it is widely called is a classic coding challenge that requires finding two integers in a given list that add up to a target value. The problem is often presented in different technical contexts, for example in algorithmic design, data structures, and optimization or even in the form of interview questions for most software engineering positions.

Now, to the main thing, this problem requires us to find two integers provided they are present in the given list that add up to a given target value. So for example if given `example_list`  and a `target_int` below: 
```python
example_list = [2, 3, 6, 9]
target_int = 9
```
You would be expected to come up with a code that returns the index location of  `3 ` and `6` since these are the integers that add up to the target integer, such that your return value is: 
`[1, 2]`

#  Intuition behind the solution
**layman's thought**

When I first approached the Two-Sum problem, my initial thought was to find a way to map each number in the input list to its corresponding index location. I realized that this could be achieved by creating a table or dictionary that stores each number as a key and its corresponding index as the value. Such that for the list below:

```python
example_list = [2, 3, 6, 9]
```
you would have a table similar to the one below:

| Elements | Index Location |
|----------|-----------------|
| 2        | 0               |
| 3        | 1               |
| 6       | 2               |
| 9       | 3               |

Next, I iterated over the input list and for each number, I calculated the difference between that number and the target integer. I then checked if this difference exists in the input list (excluding the current number being checked). If the difference was found in the list, I used the table or dictionary I created earlier to find the index location of the number that makes up the target sum. This gave me the indices of the two numbers that add up to the target value.

In summary, my solution involved creating a table or dictionary that maps each number to its corresponding index location in the input list, and then iterating over the list to find the difference between each number and the target integer. I then used the table or dictionary to find the location of the number that makes up the target sum.

**Pythonic thoughts**

The table can be presented in Python as a hash table or dictionary data structure that maps each integer in the input list to its corresponding index location. This will enable us to access the index location of any integer in constant time. To do this, I created a dictionary variable that will store the integers as keys and index location as values. In Python the index location and elements can be gotten using the `enumerate` method. This will return both the index location and element while iterating through a list: 

```python 
cache = {el: en for en, el in enumerate(input_list)}
```
Next, iterate over the input list and for each integer, calculate the difference between that integer and the target(given):
```python
    for en, int_1 in enumerate(input_list):
```
       
Next, check if the difference exists in the input list (excluding the current integer being checked). This is achieved by looking it up in the dictionary. This search operation takes constant time. 
```python 
            if (target_int - int_1) in input_list :
                    if cache[target_int - int_1] != en:
```

If this search operation is successful and the difference is found in the input list, use the dictionary to look up the index location of the integer that makes up the sum. 

```python 
                            return [cache[int_1], cache[target_int-int_1]]
```

If no match is found, i.e. no two integers add up to the target value, we return an empty list. 
```python 
    return []
```

# Putting it altogether - code
```python
def two_sum(input_list: list, target_int:int):
    # Create a hash table or dictionary that maps each integer to its index location
    cache = {el:en for en, el in enumerate(input_list)}

    # Iterate over the input list and check for the sum of two integers that equals the target value
    for en, int_1 in enumerate(input_list):
        if (target_int - int_1) in input_list:
            # Check that the two integers are not the same
            if cache[target_int - int_1] != en:
                # Return the indices of the two integers that add up to the target value
                return [cache[int_1], cache[target_int-int_1]]

    # Return an empty list if no two integers add up to the target value
    return []

```

# Testing
To test if the code works:
```python
# Example usage
list_1 = [2, 3, 6, 9]
print(two_sum(list_1, 9))  # Output: [1, 2]
```

# Time and Space Complexity
The time complexity of this solution is O(n), where n is the length of the input list, and the space complexity is also O(n) since we need to store each integer in the input list as a key in the dictionary.

# Use cases 
The two-sum problem is a common problem in computer science and is used in many real-world applications. For example, in financial applications, we can use the two-sum problem to find pairs of stocks that add up to a given target value. In image processing, we can use the two-sum problem to find pairs of pixels that add up to a given target colour.

# Conclusion 
In this blog post, we discussed the two-sum problem, the intuition behind solving it, and how to solve it using a dictionary/hash table. We saw that this problem has a time complexity of O(n) and a space complexity of O(n). We also discussed some use cases of the two-sum problem in real-world applications.