# Complexity Ranking

Best → Worst

```text
O(1)
O(log n)
O(√n)
O(n)
O(n log n)
O(n²)
O(n³)
O(2ⁿ)
O(n!)
```

Memorize this.

Every interview expects this.

---

# O(1) Constant Time

```python
arr = [10,20,30]

print(arr[0])
```

No matter:

```text
n = 10
n = 1000
n = 1000000
```

Only one operation.

```text
O(1)
```

---

# O(log n)

Example:

Binary Search

```python
low = 0
high = n - 1

while low <= high:
    mid = (low + high) // 2
```

Each iteration removes half the data.

```text
1000
500
250
125
62
31
15
7
3
1
```

Only about:

```text
log₂(n)
```

steps.

Complexity:

```text
O(log n)
```

---

# O(n)

```python
for i in range(n):
    print(i)
```

One pass through data.

```text
n operations
```

Complexity:

```text
O(n)
```

---

# O(n²)

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

Operations:

```text
n × n
```

Complexity:

```text
O(n²)
```

---

# O(n³)

```python
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i,j,k)
```

Complexity:

```text
O(n³)
```

---

# O(2ⁿ)

Example:

Recursive Fibonacci

```python
def fib(n):
    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)
```

Calls explode exponentially.

```text
O(2ⁿ)
```

Very bad.

---

# O(n!)

Example:

Generate all permutations.

```python
from itertools import permutations
```

Number of permutations:

```text
n!
```

Complexity:

```text
O(n!)
```

Extremely expensive.

---
