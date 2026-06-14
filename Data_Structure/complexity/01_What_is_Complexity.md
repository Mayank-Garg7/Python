# What is Time Complexity?

Time Complexity tells us:

> How the running time of an algorithm grows as the input size grows.

Not actual seconds.

Bad way:

```python
start = time.time()
```

Good way:

```python
How many operations are performed?
```

Example:

```python
for i in range(n):
    print(i)
```

If:

```text
n = 10     -> 10 operations
n = 100    -> 100 operations
n = 1000   -> 1000 operations
```

Growth is proportional to n.

Therefore:

```text
O(n)
```

---


# What is Space Complexity?

Space Complexity tells us:

> How much extra memory an algorithm needs.

Example:

```python
arr = [1,2,3,4,5]
```

Memory grows with input size.

```text
n elements
=> O(n) space
```

---