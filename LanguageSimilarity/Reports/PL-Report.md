# Result

| Algorithm | Min diff | Max diff | Avg diff |
|-----------|----------|----------|----------|
| gestalt pattern matching with ast | 0.00 | 71.95 | 21.11 |
| jaccard similarity with ast | 0.00 | 73.00 | 22.85 |
| sequence matching with ast | 0.00 | 93.00 | 38.11 |
| tree edit distance | 0.00 | 77.62 | 26.57 |
| codebert model cos similarity | 0.00 | 100.00 | 37.21 |
| codet5 description similarity | 0.42 | 78.53 | 27.08 |
| fine tuned codebert | 10.00 | 66.00 | 45.71 |

# Examples
## simple
### 1.
**a)** def sum(a, b): return a + b

**b)** def add(x, y): return x + y

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 100.00% | 100.00% | 0.00 |
| jaccard similarity with ast | 100.00% | 100.00% | 0.00 |
| sequence matching with ast | 100.00% | 100.00% | 0.00 |
| tree edit distance | 100.00% | 100.00% | 0.00 |
| codebert model cos similarity | 100.00% | 100.00% | 0.00 |
| codet5 description similarity | 32.28% | 100.00% | 67.72 |
| fine tuned codebert | 47.00% | 100.00% | 53.00 |

---

### 2.
**a)** if x == True: return 1

**b)** if x: return 1

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 72.73% | 97.00% | 24.27 |
| jaccard similarity with ast | 57.14% | 97.00% | 39.86 |
| sequence matching with ast | 14.29% | 97.00% | 82.71 |
| tree edit distance | 62.50% | 97.00% | 34.50 |
| codebert model cos similarity | 100.00% | 97.00% | 3.00 |
| codet5 description similarity | 96.58% | 97.00% | 0.42 |
| fine tuned codebert | 47.00% | 97.00% | 50.00 |

---

### 3.
**a)** print('Hello')

**b)** x = 5 * 7

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 18.18% | 0.00% | 18.18 |
| jaccard similarity with ast | 10.00% | 0.00% | 10.00 |
| sequence matching with ast | 0.00% | 0.00% | 0.00 |
| tree edit distance | 14.29% | 0.00% | 14.29 |
| codebert model cos similarity | 99.00% | 0.00% | 99.00 |
| codet5 description similarity | 7.98% | 0.00% | 7.98 |
| fine tuned codebert | 38.00% | 0.00% | 38.00 |

---

### 4.
**a)** x = 5
y = x - 3
z = y * 4

**b)** x = 5
y = x * 4
z = y - 3

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 77.78% | 40.00% | 37.78 |
| jaccard similarity with ast | 100.00% | 40.00% | 60.00 |
| sequence matching with ast | 77.78% | 40.00% | 37.78 |
| tree edit distance | 62.50% | 40.00% | 22.50 |
| codebert model cos similarity | 100.00% | 40.00% | 60.00 |
| codet5 description similarity | 99.99% | 40.00% | 59.99 |
| fine tuned codebert | 50.00% | 40.00% | 10.00 |

---

## similar, with certain differences
### 1.
**a)** def sum(a, b): return a + b

**b)** def add(x, y): return x + y

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 100.00% | 98.00% | 2.00 |
| jaccard similarity with ast | 100.00% | 98.00% | 2.00 |
| sequence matching with ast | 100.00% | 98.00% | 2.00 |
| tree edit distance | 100.00% | 98.00% | 2.00 |
| codebert model cos similarity | 100.00% | 98.00% | 2.00 |
| codet5 description similarity | 32.28% | 98.00% | 65.72 |
| fine tuned codebert | 47.00% | 98.00% | 51.00 |

---

### 2.
**a)** for i in range(5): print(i)

**b)** i = 0
while i < 5:
  print(i)
  i += 1

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 57.14% | 95.00% | 37.86 |
| jaccard similarity with ast | 35.71% | 95.00% | 59.29 |
| sequence matching with ast | 11.11% | 95.00% | 83.89 |
| tree edit distance | 41.18% | 95.00% | 53.82 |
| codebert model cos similarity | 97.00% | 95.00% | 2.00 |
| codet5 description similarity | 41.59% | 95.00% | 53.41 |
| fine tuned codebert | 33.00% | 95.00% | 62.00 |

---

### 3.
**a)** if x == True: return 1

**b)** if x: return 1

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 72.73% | 97.00% | 24.27 |
| jaccard similarity with ast | 57.14% | 97.00% | 39.86 |
| sequence matching with ast | 14.29% | 97.00% | 82.71 |
| tree edit distance | 62.50% | 97.00% | 34.50 |
| codebert model cos similarity | 100.00% | 97.00% | 3.00 |
| codet5 description similarity | 96.58% | 97.00% | 0.42 |
| fine tuned codebert | 47.00% | 97.00% | 50.00 |

---

### 4.
**a)** items = [x for x in range(10)]

**b)** items = list(range(10))

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 63.16% | 96.00% | 32.84 |
| jaccard similarity with ast | 71.43% | 96.00% | 24.57 |
| sequence matching with ast | 45.45% | 96.00% | 50.55 |
| tree edit distance | 70.00% | 96.00% | 26.00 |
| codebert model cos similarity | 99.00% | 96.00% | 3.00 |
| codet5 description similarity | 44.46% | 96.00% | 51.54 |
| fine tuned codebert | 43.00% | 96.00% | 53.00 |

---

### 5.
**a)** print('Hello, ' + name)

**b)** print(f'Hello, {name}')

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 71.43% | 98.00% | 26.57 |
| jaccard similarity with ast | 50.00% | 98.00% | 48.00 |
| sequence matching with ast | 71.43% | 98.00% | 26.57 |
| tree edit distance | 62.50% | 98.00% | 35.50 |
| codebert model cos similarity | 99.00% | 98.00% | 1.00 |
| codet5 description similarity | 100.00% | 98.00% | 2.00 |
| fine tuned codebert | 45.00% | 98.00% | 53.00 |

---

### 6.
**a)** def square(x): return x * x

**b)** def sq(x): return pow(x, 2)

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 75.00% | 92.00% | 17.00 |
| jaccard similarity with ast | 55.56% | 92.00% | 36.44 |
| sequence matching with ast | 62.50% | 92.00% | 29.50 |
| tree edit distance | 66.67% | 92.00% | 25.33 |
| codebert model cos similarity | 100.00% | 92.00% | 8.00 |
| codet5 description similarity | 100.00% | 92.00% | 8.00 |
| fine tuned codebert | 40.00% | 92.00% | 52.00 |

---

### 7.
**a)** a, b = b, a

**b)** temp = a
a = b
b = temp

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 63.64% | 95.00% | 31.36 |
| jaccard similarity with ast | 75.00% | 95.00% | 20.00 |
| sequence matching with ast | 25.00% | 95.00% | 70.00 |
| tree edit distance | 40.00% | 95.00% | 55.00 |
| codebert model cos similarity | 99.00% | 95.00% | 4.00 |
| codet5 description similarity | 47.46% | 95.00% | 47.54 |
| fine tuned codebert | 40.00% | 95.00% | 55.00 |

---

### 8.
**a)** return len(s)

**b)** count = 0
for _ in s:
  count += 1
return count

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 21.05% | 93.00% | 71.95 |
| jaccard similarity with ast | 20.00% | 93.00% | 73.00 |
| sequence matching with ast | 0.00% | 93.00% | 93.00 |
| tree edit distance | 15.38% | 93.00% | 77.62 |
| codebert model cos similarity | 98.00% | 93.00% | 5.00 |
| codet5 description similarity | 19.21% | 93.00% | 73.79 |
| fine tuned codebert | 40.00% | 93.00% | 53.00 |

---

### 9.
**a)** try: f()
except: pass

**b)** try:
  f()
except Exception:
  pass

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 92.31% | 90.00% | 2.31 |
| jaccard similarity with ast | 100.00% | 90.00% | 10.00 |
| sequence matching with ast | 71.43% | 90.00% | 18.57 |
| tree edit distance | 87.50% | 90.00% | 2.50 |
| codebert model cos similarity | 100.00% | 90.00% | 10.00 |
| codet5 description similarity | 11.47% | 90.00% | 78.53 |
| fine tuned codebert | 47.00% | 90.00% | 43.00 |

---

### 10.
**a)** with open('file.txt') as f: data = f.read()

**b)** f = open('file.txt')
data = f.read()
f.close()

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 62.07% | 91.00% | 28.93 |
| jaccard similarity with ast | 66.67% | 91.00% | 24.33 |
| sequence matching with ast | 0.00% | 91.00% | 91.00 |
| tree edit distance | 46.67% | 91.00% | 44.33 |
| codebert model cos similarity | 100.00% | 91.00% | 9.00 |
| codet5 description similarity | 79.79% | 91.00% | 11.21 |
| fine tuned codebert | 42.00% | 91.00% | 49.00 |

---

## completely different
### 1.
**a)** print('Hello')

**b)** x = 5 * 7

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 18.18% | 0.00% | 18.18 |
| jaccard similarity with ast | 10.00% | 0.00% | 10.00 |
| sequence matching with ast | 0.00% | 0.00% | 0.00 |
| tree edit distance | 14.29% | 0.00% | 14.29 |
| codebert model cos similarity | 99.00% | 0.00% | 99.00 |
| codet5 description similarity | 7.98% | 0.00% | 7.98 |
| fine tuned codebert | 38.00% | 0.00% | 38.00 |

---

### 2.
**a)** def foo(): return True

**b)** if x == 10: print(x)

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 0.00% | 0.00% | 0.00 |
| jaccard similarity with ast | 0.00% | 0.00% | 0.00 |
| sequence matching with ast | 0.00% | 0.00% | 0.00 |
| tree edit distance | 10.00% | 0.00% | 10.00 |
| codebert model cos similarity | 99.00% | 0.00% | 99.00 |
| codet5 description similarity | 42.02% | 0.00% | 42.02 |
| fine tuned codebert | 41.00% | 0.00% | 41.00 |

---

### 3.
**a)** a = [1,2,3]

**b)** import math

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 0.00% | 0.00% | 0.00 |
| jaccard similarity with ast | 0.00% | 0.00% | 0.00 |
| sequence matching with ast | 0.00% | 0.00% | 0.00 |
| tree edit distance | 14.29% | 0.00% | 14.29 |
| codebert model cos similarity | 99.00% | 0.00% | 99.00 |
| codet5 description similarity | 27.68% | 0.00% | 27.68 |
| fine tuned codebert | 40.00% | 0.00% | 40.00 |

---

### 4.
**a)** while True: pass

**b)** try: x = 1/0
except: pass

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 15.38% | 0.00% | 15.38 |
| jaccard similarity with ast | 8.33% | 0.00% | 8.33 |
| sequence matching with ast | 0.00% | 0.00% | 0.00 |
| tree edit distance | 20.00% | 0.00% | 20.00 |
| codebert model cos similarity | 99.00% | 0.00% | 99.00 |
| codet5 description similarity | 31.36% | 0.00% | 31.36 |
| fine tuned codebert | 36.00% | 0.00% | 36.00 |

---

### 5.
**a)** print(sum([1,2,3]))

**b)** open('file.txt')

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 46.15% | 0.00% | 46.15 |
| jaccard similarity with ast | 37.50% | 0.00% | 37.50 |
| sequence matching with ast | 33.33% | 0.00% | 33.33 |
| tree edit distance | 40.00% | 0.00% | 40.00 |
| codebert model cos similarity | 99.00% | 0.00% | 99.00 |
| codet5 description similarity | 6.10% | 0.00% | 6.10 |
| fine tuned codebert | 38.00% | 0.00% | 38.00 |

---

### 6.
**a)** x = x + 1

**b)** print('Done')

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 18.18% | 5.00% | 13.18 |
| jaccard similarity with ast | 11.11% | 5.00% | 6.11 |
| sequence matching with ast | 0.00% | 5.00% | 5.00 |
| tree edit distance | 28.57% | 5.00% | 23.57 |
| codebert model cos similarity | 99.00% | 5.00% | 94.00 |
| codet5 description similarity | 22.39% | 5.00% | 17.39 |
| fine tuned codebert | 41.00% | 5.00% | 36.00 |

---

### 7.
**a)** x = input()

**b)** def bar(): pass

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 0.00% | 0.00% | 0.00 |
| jaccard similarity with ast | 0.00% | 0.00% | 0.00 |
| sequence matching with ast | 0.00% | 0.00% | 0.00 |
| tree edit distance | 20.00% | 0.00% | 20.00 |
| codebert model cos similarity | 100.00% | 0.00% | 100.00 |
| codet5 description similarity | 5.90% | 0.00% | 5.90 |
| fine tuned codebert | 44.00% | 0.00% | 44.00 |

---

### 8.
**a)** for i in range(10): print(i)

**b)** a = {'key': 'value'}

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 25.00% | 0.00% | 25.00 |
| jaccard similarity with ast | 20.00% | 0.00% | 20.00 |
| sequence matching with ast | 20.00% | 0.00% | 20.00 |
| tree edit distance | 20.00% | 0.00% | 20.00 |
| codebert model cos similarity | 98.00% | 0.00% | 98.00 |
| codet5 description similarity | 21.53% | 0.00% | 21.53 |
| fine tuned codebert | 36.00% | 0.00% | 36.00 |

---

### 9.
**a)** raise ValueError('error')

**b)** x = [None]*10

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 16.67% | 0.00% | 16.67 |
| jaccard similarity with ast | 9.09% | 0.00% | 9.09 |
| sequence matching with ast | 0.00% | 0.00% | 0.00 |
| tree edit distance | 12.50% | 0.00% | 12.50 |
| codebert model cos similarity | 99.00% | 0.00% | 99.00 |
| codet5 description similarity | 10.59% | 0.00% | 10.59 |
| fine tuned codebert | 34.00% | 0.00% | 34.00 |

---

### 10.
**a)** def double(n): return n*2

**b)** sorted(['z','a'])

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 14.29% | 10.00% | 4.29 |
| jaccard similarity with ast | 7.69% | 10.00% | 2.31 |
| sequence matching with ast | 0.00% | 10.00% | 10.00 |
| tree edit distance | 11.11% | 10.00% | 1.11 |
| codebert model cos similarity | 99.00% | 10.00% | 89.00 |
| codet5 description similarity | 37.62% | 10.00% | 27.62 |
| fine tuned codebert | 42.00% | 10.00% | 32.00 |

---

## different, but with a common meaning
### 1.
**a)** def greet(): print('Hi')

**b)** def greet(): print('Hello')

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 83.33% | 90.00% | 6.67 |
| jaccard similarity with ast | 71.43% | 90.00% | 18.57 |
| sequence matching with ast | 83.33% | 90.00% | 6.67 |
| tree edit distance | 85.71% | 90.00% | 4.29 |
| codebert model cos similarity | 100.00% | 90.00% | 10.00 |
| codet5 description similarity | 71.28% | 90.00% | 18.72 |
| fine tuned codebert | 49.00% | 90.00% | 41.00 |

---

### 2.
**a)** if not x: return False

**b)** if x == False: return False

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 61.54% | 90.00% | 28.46 |
| jaccard similarity with ast | 50.00% | 90.00% | 40.00 |
| sequence matching with ast | 14.29% | 90.00% | 75.71 |
| tree edit distance | 50.00% | 90.00% | 40.00 |
| codebert model cos similarity | 100.00% | 90.00% | 10.00 |
| codet5 description similarity | 92.23% | 90.00% | 2.23 |
| fine tuned codebert | 46.00% | 90.00% | 44.00 |

---

### 3.
**a)** return True if x > 0 else False

**b)** if x > 0:
  return True
else:
  return False

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 70.59% | 85.00% | 14.41 |
| jaccard similarity with ast | 77.78% | 85.00% | 7.22 |
| sequence matching with ast | 11.11% | 85.00% | 73.89 |
| tree edit distance | 60.00% | 85.00% | 25.00 |
| codebert model cos similarity | 99.00% | 85.00% | 14.00 |
| codet5 description similarity | 79.27% | 85.00% | 5.73 |
| fine tuned codebert | 46.00% | 85.00% | 39.00 |

---

### 4.
**a)** data = json.loads(s)

**b)** data = json.loads(str(s))

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 87.50% | 80.00% | 7.50 |
| jaccard similarity with ast | 100.00% | 80.00% | 20.00 |
| sequence matching with ast | 66.67% | 80.00% | 13.33 |
| tree edit distance | 77.78% | 80.00% | 2.22 |
| codebert model cos similarity | 99.00% | 80.00% | 19.00 |
| codet5 description similarity | 90.43% | 80.00% | 10.43 |
| fine tuned codebert | 26.00% | 80.00% | 54.00 |

---

### 5.
**a)** x = [i for i in range(10) if i%2==0]

**b)** x = list(filter(lambda i: i%2==0, range(10)))

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 63.16% | 90.00% | 26.84 |
| jaccard similarity with ast | 68.75% | 90.00% | 21.25 |
| sequence matching with ast | 25.00% | 90.00% | 65.00 |
| tree edit distance | 55.00% | 90.00% | 35.00 |
| codebert model cos similarity | 98.00% | 90.00% | 8.00 |
| codet5 description similarity | 93.19% | 90.00% | 3.19 |
| fine tuned codebert | 39.00% | 90.00% | 51.00 |

---

### 6.
**a)** for line in open('file.txt'):
  print(line)

**b)** with open('file.txt') as f:
  for line in f:
    print(line)

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 64.00% | 95.00% | 31.00 |
| jaccard similarity with ast | 75.00% | 95.00% | 20.00 |
| sequence matching with ast | 6.67% | 95.00% | 88.33 |
| tree edit distance | 50.00% | 95.00% | 45.00 |
| codebert model cos similarity | 100.00% | 95.00% | 5.00 |
| codet5 description similarity | 57.41% | 95.00% | 37.59 |
| fine tuned codebert | 29.00% | 95.00% | 66.00 |

---

### 7.
**a)** def identity(x): return x

**b)** def echo(x): return x

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 100.00% | 96.00% | 4.00 |
| jaccard similarity with ast | 100.00% | 96.00% | 4.00 |
| sequence matching with ast | 100.00% | 96.00% | 4.00 |
| tree edit distance | 100.00% | 96.00% | 4.00 |
| codebert model cos similarity | 100.00% | 96.00% | 4.00 |
| codet5 description similarity | 24.13% | 96.00% | 71.87 |
| fine tuned codebert | 48.00% | 96.00% | 48.00 |

---

### 8.
**a)** result = a if a > b else b

**b)** if a > b:
  result = a
else:
  result = b

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 52.17% | 98.00% | 45.83 |
| jaccard similarity with ast | 71.43% | 98.00% | 26.57 |
| sequence matching with ast | 7.69% | 98.00% | 90.31 |
| tree edit distance | 41.67% | 98.00% | 56.33 |
| codebert model cos similarity | 99.00% | 98.00% | 1.00 |
| codet5 description similarity | 67.55% | 98.00% | 30.45 |
| fine tuned codebert | 43.00% | 98.00% | 55.00 |

---

### 9.
**a)** total += price

**b)** total = total + price

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 66.67% | 95.00% | 28.33 |
| jaccard similarity with ast | 50.00% | 95.00% | 45.00 |
| sequence matching with ast | 42.86% | 95.00% | 52.14 |
| tree edit distance | 57.14% | 95.00% | 37.86 |
| codebert model cos similarity | 100.00% | 95.00% | 5.00 |
| codet5 description similarity | 100.00% | 95.00% | 5.00 |
| fine tuned codebert | 45.00% | 95.00% | 50.00 |

---

### 10.
**a)** if x in [1,2,3]: print(x)

**b)** if x == 1 or x == 2 or x == 3: print(x)

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching with ast | 64.52% | 95.00% | 30.48 |
| jaccard similarity with ast | 61.54% | 95.00% | 33.46 |
| sequence matching with ast | 5.26% | 95.00% | 89.74 |
| tree edit distance | 45.00% | 95.00% | 50.00 |
| codebert model cos similarity | 100.00% | 95.00% | 5.00 |
| codet5 description similarity | 85.81% | 95.00% | 9.19 |
| fine tuned codebert | 36.00% | 95.00% | 59.00 |

---

