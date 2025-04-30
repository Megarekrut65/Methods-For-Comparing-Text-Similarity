# Result

| Algorithm | Min diff | Max diff | Avg diff |
|-----------|----------|----------|----------|
| abstract syntax tree | 0.00 | 90.00 | 37.07 |
| context free grammar | 0.00 | 90.00 | 37.07 |

# Examples
## similar, with certain differences
### 1.
**a)** def sum(a, b): return a + b

**b)** def add(x, y): return x + y

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 100.00% | 98.00% | 2.00 |
| context free grammar | 100.00% | 98.00% | 2.00 |

---

### 2.
**a)** for i in range(5): print(i)

**b)** i = 0
while i < 5:
  print(i)
  i += 1

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 5.00% | 95.00% | 90.00 |
| context free grammar | 5.00% | 95.00% | 90.00 |

---

### 3.
**a)** if x == True: return 1

**b)** if x: return 1

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 33.00% | 97.00% | 64.00 |
| context free grammar | 33.00% | 97.00% | 64.00 |

---

### 4.
**a)** items = [x for x in range(10)]

**b)** items = list(range(10))

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 50.00% | 96.00% | 46.00 |
| context free grammar | 50.00% | 96.00% | 46.00 |

---

### 5.
**a)** print('Hello, ' + name)

**b)** print(f'Hello, {name}')

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 80.00% | 98.00% | 18.00 |
| context free grammar | 80.00% | 98.00% | 18.00 |

---

### 6.
**a)** def square(x): return x * x

**b)** def sq(x): return pow(x, 2)

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 73.00% | 92.00% | 19.00 |
| context free grammar | 73.00% | 92.00% | 19.00 |

---

### 7.
**a)** a, b = b, a

**b)** temp = a
a = b
b = temp

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 50.00% | 95.00% | 45.00 |
| context free grammar | 50.00% | 95.00% | 45.00 |

---

### 8.
**a)** return len(s)

**b)** count = 0
for _ in s:
  count += 1
return count

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 11.00% | 93.00% | 82.00 |
| context free grammar | 11.00% | 93.00% | 82.00 |

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
| abstract syntax tree | 50.00% | 90.00% | 40.00 |
| context free grammar | 50.00% | 90.00% | 40.00 |

---

### 10.
**a)** with open('file.txt') as f: data = f.read()

**b)** f = open('file.txt')
data = f.read()
f.close()

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 18.00% | 91.00% | 73.00 |
| context free grammar | 18.00% | 91.00% | 73.00 |

---

## completely different
### 1.
**a)** print('Hello')

**b)** x = 5 * 7

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 12.00% | 0.00% | 12.00 |
| context free grammar | 12.00% | 0.00% | 12.00 |

---

### 2.
**a)** def foo(): return True

**b)** if x == 10: print(x)

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 8.00% | 0.00% | 8.00 |
| context free grammar | 8.00% | 0.00% | 8.00 |

---

### 3.
**a)** a = [1,2,3]

**b)** import math

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 11.00% | 0.00% | 11.00 |
| context free grammar | 11.00% | 0.00% | 11.00 |

---

### 4.
**a)** while True: pass

**b)** try: x = 1/0
except: pass

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 9.00% | 0.00% | 9.00 |
| context free grammar | 9.00% | 0.00% | 9.00 |

---

### 5.
**a)** print(sum([1,2,3]))

**b)** open('file.txt')

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 38.00% | 0.00% | 38.00 |
| context free grammar | 38.00% | 0.00% | 38.00 |

---

### 6.
**a)** x = x + 1

**b)** print('Done')

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 11.00% | 5.00% | 6.00 |
| context free grammar | 11.00% | 5.00% | 6.00 |

---

### 7.
**a)** x = input()

**b)** def bar(): pass

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 14.00% | 0.00% | 14.00 |
| context free grammar | 14.00% | 0.00% | 14.00 |

---

### 8.
**a)** for i in range(10): print(i)

**b)** a = {'key': 'value'}

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 14.00% | 0.00% | 14.00 |
| context free grammar | 14.00% | 0.00% | 14.00 |

---

### 9.
**a)** raise ValueError('error')

**b)** x = [None]*10

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 10.00% | 0.00% | 10.00 |
| context free grammar | 10.00% | 0.00% | 10.00 |

---

### 10.
**a)** def double(n): return n*2

**b)** sorted(['z','a'])

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 10.00% | 10.00% | 0.00 |
| context free grammar | 10.00% | 10.00% | 0.00 |

---

## different, but with a common meaning
### 1.
**a)** def greet(): print('Hi')

**b)** def greet(): print('Hello')

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 100.00% | 90.00% | 10.00 |
| context free grammar | 100.00% | 90.00% | 10.00 |

---

### 2.
**a)** if not x: return False

**b)** if x == False: return False

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 44.00% | 90.00% | 46.00 |
| context free grammar | 44.00% | 90.00% | 46.00 |

---

### 3.
**a)** return True if x > 0 else False

**b)** if x > 0:
  return True
else:
  return False

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 18.00% | 85.00% | 67.00 |
| context free grammar | 18.00% | 85.00% | 67.00 |

---

### 4.
**a)** data = json.loads(s)

**b)** data = json.loads(str(s))

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 57.00% | 80.00% | 23.00 |
| context free grammar | 57.00% | 80.00% | 23.00 |

---

### 5.
**a)** x = [i for i in range(10) if i%2==0]

**b)** x = list(filter(lambda i: i%2==0, range(10)))

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 28.00% | 90.00% | 62.00 |
| context free grammar | 28.00% | 90.00% | 62.00 |

---

### 6.
**a)** for line in open('file.txt'):
  print(line)

**b)** with open('file.txt') as f:
  for line in f:
    print(line)

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 15.00% | 95.00% | 80.00 |
| context free grammar | 15.00% | 95.00% | 80.00 |

---

### 7.
**a)** def identity(x): return x

**b)** def echo(x): return x

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 100.00% | 96.00% | 4.00 |
| context free grammar | 100.00% | 96.00% | 4.00 |

---

### 8.
**a)** result = a if a > b else b

**b)** if a > b:
  result = a
else:
  result = b

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 33.00% | 98.00% | 65.00 |
| context free grammar | 33.00% | 98.00% | 65.00 |

---

### 9.
**a)** total += price

**b)** total = total + price

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 20.00% | 95.00% | 75.00 |
| context free grammar | 20.00% | 95.00% | 75.00 |

---

### 10.
**a)** if x in [1,2,3]: print(x)

**b)** if x == 1 or x == 2 or x == 3: print(x)

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| abstract syntax tree | 16.00% | 95.00% | 79.00 |
| context free grammar | 16.00% | 95.00% | 79.00 |

---

