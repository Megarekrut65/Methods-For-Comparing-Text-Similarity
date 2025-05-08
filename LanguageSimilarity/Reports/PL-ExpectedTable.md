
**SIMPLE**

<table>
  <tr>
    <th>Text pairs</th>
    <th>gestalt pattern matching with ast</th>
    <th>jaccard similarity with ast</th>
    <th>sequence matching with ast</th>
    <th>tree edit distance</th>
    <th>codebert model cos similarity</th>
    <th>codet5 description similarity</th>
    <th>fine tuned codebert</th>
  </tr>
  <tr>
    <td><pre><code>def sum(a, b): return a + b</code></pre><pre><code>def add(x, y): return x + y</code></pre></td>
    <td>100.00%</td>
    <td>100.00%</td>
    <td>100.00%</td>
    <td>100.00%</td>
    <td>100.00%</td>
    <td>100.00%</td>
    <td>100.00%</td>
  </tr>
  <tr>
    <td><pre><code>if x == True: return 1</code></pre><pre><code>if x: return 1</code></pre></td>
    <td>97.00%</td>
    <td>97.00%</td>
    <td>97.00%</td>
    <td>97.00%</td>
    <td>97.00%</td>
    <td>97.00%</td>
    <td>97.00%</td>
  </tr>
  <tr>
    <td><pre><code>print('Hello')</code></pre><pre><code>x = 5 * 7</code></pre></td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
  </tr>
  <tr>
    <td><pre><code>x = 5
y = x - 3
z = y * 4</code></pre><pre><code>x = 5
y = x * 4
z = y - 3</code></pre></td>
    <td>40.00%</td>
    <td>40.00%</td>
    <td>40.00%</td>
    <td>40.00%</td>
    <td>40.00%</td>
    <td>40.00%</td>
    <td>40.00%</td>
  </tr>
</table>

**SIMILAR, WITH CERTAIN DIFFERENCES**

<table>
  <tr>
    <th>Text pairs</th>
    <th>gestalt pattern matching with ast</th>
    <th>jaccard similarity with ast</th>
    <th>sequence matching with ast</th>
    <th>tree edit distance</th>
    <th>codebert model cos similarity</th>
    <th>codet5 description similarity</th>
    <th>fine tuned codebert</th>
  </tr>
  <tr>
    <td><pre><code>def sum(a, b): return a + b</code></pre><pre><code>def add(x, y): return x + y</code></pre></td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
  </tr>
  <tr>
    <td><pre><code>for i in range(5): print(i)</code></pre><pre><code>i = 0
while i < 5:
  print(i)
  i += 1</code></pre></td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
  </tr>
  <tr>
    <td><pre><code>if x == True: return 1</code></pre><pre><code>if x: return 1</code></pre></td>
    <td>97.00%</td>
    <td>97.00%</td>
    <td>97.00%</td>
    <td>97.00%</td>
    <td>97.00%</td>
    <td>97.00%</td>
    <td>97.00%</td>
  </tr>
  <tr>
    <td><pre><code>items = [x for x in range(10)]</code></pre><pre><code>items = list(range(10))</code></pre></td>
    <td>96.00%</td>
    <td>96.00%</td>
    <td>96.00%</td>
    <td>96.00%</td>
    <td>96.00%</td>
    <td>96.00%</td>
    <td>96.00%</td>
  </tr>
  <tr>
    <td><pre><code>print('Hello, ' + name)</code></pre><pre><code>print(f'Hello, {name}')</code></pre></td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
  </tr>
  <tr>
    <td><pre><code>def square(x): return x * x</code></pre><pre><code>def sq(x): return pow(x, 2)</code></pre></td>
    <td>92.00%</td>
    <td>92.00%</td>
    <td>92.00%</td>
    <td>92.00%</td>
    <td>92.00%</td>
    <td>92.00%</td>
    <td>92.00%</td>
  </tr>
  <tr>
    <td><pre><code>a, b = b, a</code></pre><pre><code>temp = a
a = b
b = temp</code></pre></td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
  </tr>
  <tr>
    <td><pre><code>return len(s)</code></pre><pre><code>count = 0
for _ in s:
  count += 1
return count</code></pre></td>
    <td>93.00%</td>
    <td>93.00%</td>
    <td>93.00%</td>
    <td>93.00%</td>
    <td>93.00%</td>
    <td>93.00%</td>
    <td>93.00%</td>
  </tr>
  <tr>
    <td><pre><code>try: f()
except: pass</code></pre><pre><code>try:
  f()
except Exception:
  pass</code></pre></td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
  </tr>
  <tr>
    <td><pre><code>with open('file.txt') as f: data = f.read()</code></pre><pre><code>f = open('file.txt')
data = f.read()
f.close()</code></pre></td>
    <td>91.00%</td>
    <td>91.00%</td>
    <td>91.00%</td>
    <td>91.00%</td>
    <td>91.00%</td>
    <td>91.00%</td>
    <td>91.00%</td>
  </tr>
</table>

**COMPLETELY DIFFERENT**

<table>
  <tr>
    <th>Text pairs</th>
    <th>gestalt pattern matching with ast</th>
    <th>jaccard similarity with ast</th>
    <th>sequence matching with ast</th>
    <th>tree edit distance</th>
    <th>codebert model cos similarity</th>
    <th>codet5 description similarity</th>
    <th>fine tuned codebert</th>
  </tr>
  <tr>
    <td><pre><code>print('Hello')</code></pre><pre><code>x = 5 * 7</code></pre></td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
  </tr>
  <tr>
    <td><pre><code>def foo(): return True</code></pre><pre><code>if x == 10: print(x)</code></pre></td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
  </tr>
  <tr>
    <td><pre><code>a = [1,2,3]</code></pre><pre><code>import math</code></pre></td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
  </tr>
  <tr>
    <td><pre><code>while True: pass</code></pre><pre><code>try: x = 1/0
except: pass</code></pre></td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
  </tr>
  <tr>
    <td><pre><code>print(sum([1,2,3]))</code></pre><pre><code>open('file.txt')</code></pre></td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
  </tr>
  <tr>
    <td><pre><code>x = x + 1</code></pre><pre><code>print('Done')</code></pre></td>
    <td>5.00%</td>
    <td>5.00%</td>
    <td>5.00%</td>
    <td>5.00%</td>
    <td>5.00%</td>
    <td>5.00%</td>
    <td>5.00%</td>
  </tr>
  <tr>
    <td><pre><code>x = input()</code></pre><pre><code>def bar(): pass</code></pre></td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
  </tr>
  <tr>
    <td><pre><code>for i in range(10): print(i)</code></pre><pre><code>a = {'key': 'value'}</code></pre></td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
  </tr>
  <tr>
    <td><pre><code>raise ValueError('error')</code></pre><pre><code>x = [None]*10</code></pre></td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
  </tr>
  <tr>
    <td><pre><code>def double(n): return n*2</code></pre><pre><code>sorted(['z','a'])</code></pre></td>
    <td>10.00%</td>
    <td>10.00%</td>
    <td>10.00%</td>
    <td>10.00%</td>
    <td>10.00%</td>
    <td>10.00%</td>
    <td>10.00%</td>
  </tr>
</table>

**DIFFERENT, BUT WITH A COMMON MEANING**

<table>
  <tr>
    <th>Text pairs</th>
    <th>gestalt pattern matching with ast</th>
    <th>jaccard similarity with ast</th>
    <th>sequence matching with ast</th>
    <th>tree edit distance</th>
    <th>codebert model cos similarity</th>
    <th>codet5 description similarity</th>
    <th>fine tuned codebert</th>
  </tr>
  <tr>
    <td><pre><code>def greet(): print('Hi')</code></pre><pre><code>def greet(): print('Hello')</code></pre></td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
  </tr>
  <tr>
    <td><pre><code>if not x: return False</code></pre><pre><code>if x == False: return False</code></pre></td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
  </tr>
  <tr>
    <td><pre><code>return True if x > 0 else False</code></pre><pre><code>if x > 0:
  return True
else:
  return False</code></pre></td>
    <td>85.00%</td>
    <td>85.00%</td>
    <td>85.00%</td>
    <td>85.00%</td>
    <td>85.00%</td>
    <td>85.00%</td>
    <td>85.00%</td>
  </tr>
  <tr>
    <td><pre><code>data = json.loads(s)</code></pre><pre><code>data = json.loads(str(s))</code></pre></td>
    <td>80.00%</td>
    <td>80.00%</td>
    <td>80.00%</td>
    <td>80.00%</td>
    <td>80.00%</td>
    <td>80.00%</td>
    <td>80.00%</td>
  </tr>
  <tr>
    <td><pre><code>x = [i for i in range(10) if i%2==0]</code></pre><pre><code>x = list(filter(lambda i: i%2==0, range(10)))</code></pre></td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
  </tr>
  <tr>
    <td><pre><code>for line in open('file.txt'):
  print(line)</code></pre><pre><code>with open('file.txt') as f:
  for line in f:
    print(line)</code></pre></td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
  </tr>
  <tr>
    <td><pre><code>def identity(x): return x</code></pre><pre><code>def echo(x): return x</code></pre></td>
    <td>96.00%</td>
    <td>96.00%</td>
    <td>96.00%</td>
    <td>96.00%</td>
    <td>96.00%</td>
    <td>96.00%</td>
    <td>96.00%</td>
  </tr>
  <tr>
    <td><pre><code>result = a if a > b else b</code></pre><pre><code>if a > b:
  result = a
else:
  result = b</code></pre></td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
  </tr>
  <tr>
    <td><pre><code>total += price</code></pre><pre><code>total = total + price</code></pre></td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
  </tr>
  <tr>
    <td><pre><code>if x in [1,2,3]: print(x)</code></pre><pre><code>if x == 1 or x == 2 or x == 3: print(x)</code></pre></td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
  </tr>
</table>
