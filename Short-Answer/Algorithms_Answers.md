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

    Answer: O(nlog(n))


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


