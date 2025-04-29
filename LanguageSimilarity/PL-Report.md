# Result

| Algorithm | Min diff | Max diff | Avg diff |
|-----------|----------|----------|----------|
| gestalt pattern matching | 0.00 | 63.00 | 22.52 |
| gestalt pattern matching from difflib | 0.00 | 66.33 | 23.98 |
| jaccard algorithm with stanza lematization | 0.00 | 59.67 | 20.31 |
| sklearn vectorizer | 0.00 | 95.00 | 24.74 |
| semantic similarity with spacy | 0.68 | 72.84 | 24.61 |
| sentence transformers tensor with codebert | 0.21 | 96.98 | 33.69 |

# Examples
## similar, with certain differences
### 1.
**a)** def sum(a, b): return a + b

**b)** def add(x, y): return x + y

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 77.78% | 98.00% | 20.22 |
| gestalt pattern matching from difflib | 74.07% | 98.00% | 23.93 |
| jaccard algorithm with stanza lematization | 73.68% | 98.00% | 24.32 |
| sklearn vectorizer | 50.31% | 98.00% | 47.69 |
| semantic similarity with spacy | 76.10% | 98.00% | 21.90 |
| sentence transformers tensor with codebert | 99.08% | 98.00% | 1.08 |

---

### 2.
**a)** for i in range(5): print(i)

**b)** i = 0
while i < 5:
  print(i)
  i += 1

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 52.31% | 95.00% | 42.69 |
| gestalt pattern matching from difflib | 46.15% | 95.00% | 48.85 |
| jaccard algorithm with stanza lematization | 45.83% | 95.00% | 49.17 |
| sklearn vectorizer | 22.03% | 95.00% | 72.97 |
| semantic similarity with spacy | 70.98% | 95.00% | 24.02 |
| sentence transformers tensor with codebert | 92.73% | 95.00% | 2.27 |

---

### 3.
**a)** if x == True: return 1

**b)** if x: return 1

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 77.78% | 97.00% | 19.22 |
| gestalt pattern matching from difflib | 77.78% | 97.00% | 19.22 |
| jaccard algorithm with stanza lematization | 84.62% | 97.00% | 12.38 |
| sklearn vectorizer | 70.93% | 97.00% | 26.07 |
| semantic similarity with spacy | 91.93% | 97.00% | 5.07 |
| sentence transformers tensor with codebert | 98.33% | 97.00% | 1.33 |

---

### 4.
**a)** items = [x for x in range(10)]

**b)** items = list(range(10))

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 67.92% | 96.00% | 28.08 |
| gestalt pattern matching from difflib | 67.92% | 96.00% | 28.08 |
| jaccard algorithm with stanza lematization | 71.43% | 96.00% | 24.57 |
| sklearn vectorizer | 51.01% | 96.00% | 44.99 |
| semantic similarity with spacy | 80.03% | 96.00% | 15.97 |
| sentence transformers tensor with codebert | 97.60% | 96.00% | 1.60 |

---

### 5.
**a)** print('Hello, ' + name)

**b)** print(f'Hello, {name}')

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 86.96% | 98.00% | 11.04 |
| gestalt pattern matching from difflib | 82.61% | 98.00% | 15.39 |
| jaccard algorithm with stanza lematization | 80.00% | 98.00% | 18.00 |
| sklearn vectorizer | 100.00% | 98.00% | 2.00 |
| semantic similarity with spacy | 86.83% | 98.00% | 11.17 |
| sentence transformers tensor with codebert | 97.74% | 98.00% | 0.26 |

---

### 6.
**a)** def square(x): return x * x

**b)** def sq(x): return pow(x, 2)

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 74.07% | 92.00% | 17.93 |
| gestalt pattern matching from difflib | 74.07% | 92.00% | 17.93 |
| jaccard algorithm with stanza lematization | 66.67% | 92.00% | 25.33 |
| sklearn vectorizer | 41.12% | 92.00% | 50.88 |
| semantic similarity with spacy | 67.02% | 92.00% | 24.98 |
| sentence transformers tensor with codebert | 96.79% | 92.00% | 4.79 |

---

### 7.
**a)** a, b = b, a

**b)** temp = a
a = b
b = temp

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 52.94% | 95.00% | 42.06 |
| gestalt pattern matching from difflib | 35.29% | 95.00% | 59.71 |
| jaccard algorithm with stanza lematization | 40.00% | 95.00% | 55.00 |
| sklearn vectorizer | 0.00% | 95.00% | 95.00 |
| semantic similarity with spacy | 79.58% | 95.00% | 15.42 |
| sentence transformers tensor with codebert | 94.79% | 95.00% | 0.21 |

---

### 8.
**a)** return len(s)

**b)** count = 0
for _ in s:
  count += 1
return count

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 30.00% | 93.00% | 63.00 |
| gestalt pattern matching from difflib | 26.67% | 93.00% | 66.33 |
| jaccard algorithm with stanza lematization | 33.33% | 93.00% | 59.67 |
| sklearn vectorizer | 12.16% | 93.00% | 80.84 |
| semantic similarity with spacy | 65.39% | 93.00% | 27.61 |
| sentence transformers tensor with codebert | 94.11% | 93.00% | 1.11 |

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
| gestalt pattern matching | 75.00% | 90.00% | 15.00 |
| gestalt pattern matching from difflib | 75.00% | 90.00% | 15.00 |
| jaccard algorithm with stanza lematization | 78.95% | 90.00% | 11.05 |
| sklearn vectorizer | 77.65% | 90.00% | 12.35 |
| semantic similarity with spacy | 98.87% | 90.00% | 8.87 |
| sentence transformers tensor with codebert | 98.63% | 90.00% | 8.63 |

---

### 10.
**a)** with open('file.txt') as f: data = f.read()

**b)** f = open('file.txt')
data = f.read()
f.close()

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 78.65% | 91.00% | 12.35 |
| gestalt pattern matching from difflib | 71.91% | 91.00% | 19.09 |
| jaccard algorithm with stanza lematization | 79.17% | 91.00% | 11.83 |
| sklearn vectorizer | 63.28% | 91.00% | 27.72 |
| semantic similarity with spacy | 94.80% | 91.00% | 3.80 |
| sentence transformers tensor with codebert | 98.96% | 91.00% | 7.96 |

---

## completely different
### 1.
**a)** print('Hello')

**b)** x = 5 * 7

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 0.00% | 0.00% | 0.00 |
| gestalt pattern matching from difflib | 0.00% | 0.00% | 0.00 |
| jaccard algorithm with stanza lematization | 0.00% | 0.00% | 0.00 |
| sklearn vectorizer | 0.00% | 0.00% | 0.00 |
| semantic similarity with spacy | 50.48% | 0.00% | 50.48 |
| sentence transformers tensor with codebert | 93.41% | 0.00% | 93.41 |

---

### 2.
**a)** def foo(): return True

**b)** if x == 10: print(x)

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 47.62% | 0.00% | 47.62 |
| gestalt pattern matching from difflib | 28.57% | 0.00% | 28.57 |
| jaccard algorithm with stanza lematization | 42.11% | 0.00% | 42.11 |
| sklearn vectorizer | 0.00% | 0.00% | 0.00 |
| semantic similarity with spacy | 61.04% | 0.00% | 61.04 |
| sentence transformers tensor with codebert | 95.08% | 0.00% | 95.08 |

---

### 3.
**a)** a = [1,2,3]

**b)** import math

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 18.18% | 0.00% | 18.18 |
| gestalt pattern matching from difflib | 9.09% | 0.00% | 9.09 |
| jaccard algorithm with stanza lematization | 12.50% | 0.00% | 12.50 |
| sklearn vectorizer | 0.00% | 0.00% | 0.00 |
| semantic similarity with spacy | 27.07% | 0.00% | 27.07 |
| sentence transformers tensor with codebert | 87.01% | 0.00% | 87.01 |

---

### 4.
**a)** while True: pass

**b)** try: x = 1/0
except: pass

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 48.78% | 0.00% | 48.78 |
| gestalt pattern matching from difflib | 39.02% | 0.00% | 39.02 |
| jaccard algorithm with stanza lematization | 31.82% | 0.00% | 31.82 |
| sklearn vectorizer | 20.20% | 0.00% | 20.20 |
| semantic similarity with spacy | 71.18% | 0.00% | 71.18 |
| sentence transformers tensor with codebert | 94.40% | 0.00% | 94.40 |

---

### 5.
**a)** print(sum([1,2,3]))

**b)** open('file.txt')

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 34.29% | 0.00% | 34.29 |
| gestalt pattern matching from difflib | 22.86% | 0.00% | 22.86 |
| jaccard algorithm with stanza lematization | 26.09% | 0.00% | 26.09 |
| sklearn vectorizer | 0.00% | 0.00% | 0.00 |
| semantic similarity with spacy | 72.84% | 0.00% | 72.84 |
| sentence transformers tensor with codebert | 94.63% | 0.00% | 94.63 |

---

### 6.
**a)** x = x + 1

**b)** print('Done')

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 0.00% | 5.00% | 5.00 |
| gestalt pattern matching from difflib | 0.00% | 5.00% | 5.00 |
| jaccard algorithm with stanza lematization | 0.00% | 5.00% | 5.00 |
| sklearn vectorizer | 0.00% | 5.00% | 5.00 |
| semantic similarity with spacy | 44.22% | 5.00% | 39.22 |
| sentence transformers tensor with codebert | 91.45% | 5.00% | 86.45 |

---

### 7.
**a)** x = input()

**b)** def bar(): pass

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 38.46% | 0.00% | 38.46 |
| gestalt pattern matching from difflib | 23.08% | 0.00% | 23.08 |
| jaccard algorithm with stanza lematization | 22.22% | 0.00% | 22.22 |
| sklearn vectorizer | 0.00% | 0.00% | 0.00 |
| semantic similarity with spacy | 60.25% | 0.00% | 60.25 |
| sentence transformers tensor with codebert | 96.98% | 0.00% | 96.98 |

---

### 8.
**a)** for i in range(10): print(i)

**b)** a = {'key': 'value'}

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 25.00% | 0.00% | 25.00 |
| gestalt pattern matching from difflib | 20.83% | 0.00% | 20.83 |
| jaccard algorithm with stanza lematization | 16.00% | 0.00% | 16.00 |
| sklearn vectorizer | 0.00% | 0.00% | 0.00 |
| semantic similarity with spacy | 50.77% | 0.00% | 50.77 |
| sentence transformers tensor with codebert | 93.78% | 0.00% | 93.78 |

---

### 9.
**a)** raise ValueError('error')

**b)** x = [None]*10

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 15.79% | 0.00% | 15.79 |
| gestalt pattern matching from difflib | 5.26% | 0.00% | 5.26 |
| jaccard algorithm with stanza lematization | 13.04% | 0.00% | 13.04 |
| sklearn vectorizer | 0.00% | 0.00% | 0.00 |
| semantic similarity with spacy | 44.61% | 0.00% | 44.61 |
| sentence transformers tensor with codebert | 95.61% | 0.00% | 95.61 |

---

### 10.
**a)** def double(n): return n*2

**b)** sorted(['z','a'])

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 33.33% | 10.00% | 23.33 |
| gestalt pattern matching from difflib | 14.29% | 10.00% | 4.29 |
| jaccard algorithm with stanza lematization | 30.43% | 10.00% | 20.43 |
| sklearn vectorizer | 0.00% | 10.00% | 10.00 |
| semantic similarity with spacy | 36.13% | 10.00% | 26.13 |
| sentence transformers tensor with codebert | 91.52% | 10.00% | 81.52 |

---

## different, but with a common meaning
### 1.
**a)** def greet(): print('Hi')

**b)** def greet(): print('Hello')

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 90.20% | 90.00% | 0.20 |
| gestalt pattern matching from difflib | 90.20% | 90.00% | 0.20 |
| jaccard algorithm with stanza lematization | 88.24% | 90.00% | 1.76 |
| sklearn vectorizer | 60.30% | 90.00% | 29.70 |
| semantic similarity with spacy | 100.00% | 90.00% | 10.00 |
| sentence transformers tensor with codebert | 99.92% | 90.00% | 9.92 |

---

### 2.
**a)** if not x: return False

**b)** if x == False: return False

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 77.55% | 90.00% | 12.45 |
| gestalt pattern matching from difflib | 73.47% | 90.00% | 16.53 |
| jaccard algorithm with stanza lematization | 87.50% | 90.00% | 2.50 |
| sklearn vectorizer | 73.21% | 90.00% | 16.79 |
| semantic similarity with spacy | 90.68% | 90.00% | 0.68 |
| sentence transformers tensor with codebert | 99.02% | 90.00% | 9.02 |

---

### 3.
**a)** return True if x > 0 else False

**b)** if x > 0:
  return True
else:
  return False

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 82.67% | 85.00% | 2.33 |
| gestalt pattern matching from difflib | 56.00% | 85.00% | 29.00 |
| jaccard algorithm with stanza lematization | 88.89% | 85.00% | 3.89 |
| sklearn vectorizer | 94.87% | 85.00% | 9.87 |
| semantic similarity with spacy | 96.47% | 85.00% | 11.47 |
| sentence transformers tensor with codebert | 97.19% | 85.00% | 12.19 |

---

### 4.
**a)** data = json.loads(s)

**b)** data = json.loads(str(s))

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 88.89% | 80.00% | 8.89 |
| gestalt pattern matching from difflib | 88.89% | 80.00% | 8.89 |
| jaccard algorithm with stanza lematization | 92.86% | 80.00% | 12.86 |
| sklearn vectorizer | 77.65% | 80.00% | 2.35 |
| semantic similarity with spacy | 97.34% | 80.00% | 17.34 |
| sentence transformers tensor with codebert | 94.80% | 80.00% | 14.80 |

---

### 5.
**a)** x = [i for i in range(10) if i%2==0]

**b)** x = list(filter(lambda i: i%2==0, range(10)))

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 66.67% | 90.00% | 23.33 |
| gestalt pattern matching from difflib | 51.85% | 90.00% | 38.15 |
| jaccard algorithm with stanza lematization | 59.26% | 90.00% | 30.74 |
| sklearn vectorizer | 25.23% | 90.00% | 64.77 |
| semantic similarity with spacy | 83.56% | 90.00% | 6.44 |
| sentence transformers tensor with codebert | 94.76% | 90.00% | 4.76 |

---

### 6.
**a)** for line in open('file.txt'):
  print(line)

**b)** with open('file.txt') as f:
  for line in f:
    print(line)

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 83.50% | 95.00% | 11.50 |
| gestalt pattern matching from difflib | 64.08% | 95.00% | 30.92 |
| jaccard algorithm with stanza lematization | 80.95% | 95.00% | 14.05 |
| sklearn vectorizer | 84.66% | 95.00% | 10.34 |
| semantic similarity with spacy | 87.81% | 95.00% | 7.19 |
| sentence transformers tensor with codebert | 98.96% | 95.00% | 3.96 |

---

### 7.
**a)** def identity(x): return x

**b)** def echo(x): return x

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 78.26% | 96.00% | 17.74 |
| gestalt pattern matching from difflib | 78.26% | 96.00% | 17.74 |
| jaccard algorithm with stanza lematization | 70.59% | 96.00% | 25.41 |
| sklearn vectorizer | 50.31% | 96.00% | 45.69 |
| semantic similarity with spacy | 100.00% | 96.00% | 4.00 |
| sentence transformers tensor with codebert | 98.94% | 96.00% | 2.94 |

---

### 8.
**a)** result = a if a > b else b

**b)** if a > b:
  result = a
else:
  result = b

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 77.61% | 98.00% | 20.39 |
| gestalt pattern matching from difflib | 47.76% | 98.00% | 50.24 |
| jaccard algorithm with stanza lematization | 86.67% | 98.00% | 11.33 |
| sklearn vectorizer | 94.28% | 98.00% | 3.72 |
| semantic similarity with spacy | 95.93% | 98.00% | 2.07 |
| sentence transformers tensor with codebert | 97.59% | 98.00% | 0.41 |

---

### 9.
**a)** total += price

**b)** total = total + price

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 80.00% | 95.00% | 15.00 |
| gestalt pattern matching from difflib | 74.29% | 95.00% | 20.71 |
| jaccard algorithm with stanza lematization | 100.00% | 95.00% | 5.00 |
| sklearn vectorizer | 94.87% | 95.00% | 0.13 |
| semantic similarity with spacy | 97.69% | 95.00% | 2.69 |
| sentence transformers tensor with codebert | 97.85% | 95.00% | 2.85 |

---

### 10.
**a)** if x in [1,2,3]: print(x)

**b)** if x == 1 or x == 2 or x == 3: print(x)

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 59.38% | 95.00% | 35.62 |
| gestalt pattern matching from difflib | 59.38% | 95.00% | 35.62 |
| jaccard algorithm with stanza lematization | 73.68% | 95.00% | 21.32 |
| sklearn vectorizer | 31.88% | 95.00% | 63.12 |
| semantic similarity with spacy | 80.82% | 95.00% | 14.18 |
| sentence transformers tensor with codebert | 96.71% | 95.00% | 1.71 |

---

