#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
```python
    a = 0
    while (a < n * n * n): # n^3
    a = a + n * n # a increase by n^2 + a
```
    The loop iterates n^3 times, but the counter(a) is increamented by n^2.
    Therefore n^3 / n^2 = n

    Answer: O(n)

b)
```python
    sum = 0
    for i in range(n): # n
      j = 1             
      while j < n:      # log n
        j *= 2          
        sum += 1        
```
    For loop iterates n times, while loop iterates log n times
    Therefore n * log n

    Answer: O(n log n)


c)
```python
    def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1) # n = 2 + bunnyEars(n-1)
```
    The argument of the function linearly decreasely (n-1).

    Answer: O(n)

## Exercise II
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.


Given n floors, get referent to the start of n floors and end to the n floors

Drop the egg at n/2th floor and observe the result

If the egg breaks, 

    Drop the egg at n/2 - 1 th floor and observe the result

    If the egg does not break, then n/2th floor is the floor f

    If the egg breaks, only consider bottom half of the floors. end = n/2

If the egg does not break, only consider top half of the floors. start = n/2

repeat this process recursively until floor f is found.


complexity: O(log n)

