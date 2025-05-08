
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
    <td>32.28%</td>
    <td>47.00%</td>
  </tr>
  <tr>
    <td><pre><code>if x == True: return 1</code></pre><pre><code>if x: return 1</code></pre></td>
    <td>72.73%</td>
    <td>57.14%</td>
    <td>14.29%</td>
    <td>62.50%</td>
    <td>100.00%</td>
    <td>96.58%</td>
    <td>47.00%</td>
  </tr>
  <tr>
    <td><pre><code>print('Hello')</code></pre><pre><code>x = 5 * 7</code></pre></td>
    <td>18.18%</td>
    <td>10.00%</td>
    <td>0.00%</td>
    <td>14.29%</td>
    <td>99.00%</td>
    <td>7.98%</td>
    <td>38.00%</td>
  </tr>
  <tr>
    <td><pre><code>x = 5
y = x - 3
z = y * 4</code></pre><pre><code>x = 5
y = x * 4
z = y - 3</code></pre></td>
    <td>77.78%</td>
    <td>100.00%</td>
    <td>77.78%</td>
    <td>62.50%</td>
    <td>100.00%</td>
    <td>99.99%</td>
    <td>50.00%</td>
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
    <td>100.00%</td>
    <td>100.00%</td>
    <td>100.00%</td>
    <td>100.00%</td>
    <td>100.00%</td>
    <td>32.28%</td>
    <td>47.00%</td>
  </tr>
  <tr>
    <td><pre><code>for i in range(5): print(i)</code></pre><pre><code>i = 0
while i < 5:
  print(i)
  i += 1</code></pre></td>
    <td>57.14%</td>
    <td>35.71%</td>
    <td>11.11%</td>
    <td>41.18%</td>
    <td>97.00%</td>
    <td>41.59%</td>
    <td>33.00%</td>
  </tr>
  <tr>
    <td><pre><code>if x == True: return 1</code></pre><pre><code>if x: return 1</code></pre></td>
    <td>72.73%</td>
    <td>57.14%</td>
    <td>14.29%</td>
    <td>62.50%</td>
    <td>100.00%</td>
    <td>96.58%</td>
    <td>47.00%</td>
  </tr>
  <tr>
    <td><pre><code>items = [x for x in range(10)]</code></pre><pre><code>items = list(range(10))</code></pre></td>
    <td>63.16%</td>
    <td>71.43%</td>
    <td>45.45%</td>
    <td>70.00%</td>
    <td>99.00%</td>
    <td>44.46%</td>
    <td>43.00%</td>
  </tr>
  <tr>
    <td><pre><code>print('Hello, ' + name)</code></pre><pre><code>print(f'Hello, {name}')</code></pre></td>
    <td>71.43%</td>
    <td>50.00%</td>
    <td>71.43%</td>
    <td>62.50%</td>
    <td>99.00%</td>
    <td>100.00%</td>
    <td>45.00%</td>
  </tr>
  <tr>
    <td><pre><code>def square(x): return x * x</code></pre><pre><code>def sq(x): return pow(x, 2)</code></pre></td>
    <td>75.00%</td>
    <td>55.56%</td>
    <td>62.50%</td>
    <td>66.67%</td>
    <td>100.00%</td>
    <td>100.00%</td>
    <td>40.00%</td>
  </tr>
  <tr>
    <td><pre><code>a, b = b, a</code></pre><pre><code>temp = a
a = b
b = temp</code></pre></td>
    <td>63.64%</td>
    <td>75.00%</td>
    <td>25.00%</td>
    <td>40.00%</td>
    <td>99.00%</td>
    <td>47.46%</td>
    <td>40.00%</td>
  </tr>
  <tr>
    <td><pre><code>return len(s)</code></pre><pre><code>count = 0
for _ in s:
  count += 1
return count</code></pre></td>
    <td>21.05%</td>
    <td>20.00%</td>
    <td>0.00%</td>
    <td>15.38%</td>
    <td>98.00%</td>
    <td>19.21%</td>
    <td>40.00%</td>
  </tr>
  <tr>
    <td><pre><code>try: f()
except: pass</code></pre><pre><code>try:
  f()
except Exception:
  pass</code></pre></td>
    <td>92.31%</td>
    <td>100.00%</td>
    <td>71.43%</td>
    <td>87.50%</td>
    <td>100.00%</td>
    <td>11.47%</td>
    <td>47.00%</td>
  </tr>
  <tr>
    <td><pre><code>with open('file.txt') as f: data = f.read()</code></pre><pre><code>f = open('file.txt')
data = f.read()
f.close()</code></pre></td>
    <td>62.07%</td>
    <td>66.67%</td>
    <td>0.00%</td>
    <td>46.67%</td>
    <td>100.00%</td>
    <td>79.79%</td>
    <td>42.00%</td>
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
    <td>18.18%</td>
    <td>10.00%</td>
    <td>0.00%</td>
    <td>14.29%</td>
    <td>99.00%</td>
    <td>7.98%</td>
    <td>38.00%</td>
  </tr>
  <tr>
    <td><pre><code>def foo(): return True</code></pre><pre><code>if x == 10: print(x)</code></pre></td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>10.00%</td>
    <td>99.00%</td>
    <td>42.02%</td>
    <td>41.00%</td>
  </tr>
  <tr>
    <td><pre><code>a = [1,2,3]</code></pre><pre><code>import math</code></pre></td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>14.29%</td>
    <td>99.00%</td>
    <td>27.68%</td>
    <td>40.00%</td>
  </tr>
  <tr>
    <td><pre><code>while True: pass</code></pre><pre><code>try: x = 1/0
except: pass</code></pre></td>
    <td>15.38%</td>
    <td>8.33%</td>
    <td>0.00%</td>
    <td>20.00%</td>
    <td>99.00%</td>
    <td>31.36%</td>
    <td>36.00%</td>
  </tr>
  <tr>
    <td><pre><code>print(sum([1,2,3]))</code></pre><pre><code>open('file.txt')</code></pre></td>
    <td>46.15%</td>
    <td>37.50%</td>
    <td>33.33%</td>
    <td>40.00%</td>
    <td>99.00%</td>
    <td>6.10%</td>
    <td>38.00%</td>
  </tr>
  <tr>
    <td><pre><code>x = x + 1</code></pre><pre><code>print('Done')</code></pre></td>
    <td>18.18%</td>
    <td>11.11%</td>
    <td>0.00%</td>
    <td>28.57%</td>
    <td>99.00%</td>
    <td>22.39%</td>
    <td>41.00%</td>
  </tr>
  <tr>
    <td><pre><code>x = input()</code></pre><pre><code>def bar(): pass</code></pre></td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>20.00%</td>
    <td>100.00%</td>
    <td>5.90%</td>
    <td>44.00%</td>
  </tr>
  <tr>
    <td><pre><code>for i in range(10): print(i)</code></pre><pre><code>a = {'key': 'value'}</code></pre></td>
    <td>25.00%</td>
    <td>20.00%</td>
    <td>20.00%</td>
    <td>20.00%</td>
    <td>98.00%</td>
    <td>21.53%</td>
    <td>36.00%</td>
  </tr>
  <tr>
    <td><pre><code>raise ValueError('error')</code></pre><pre><code>x = [None]*10</code></pre></td>
    <td>16.67%</td>
    <td>9.09%</td>
    <td>0.00%</td>
    <td>12.50%</td>
    <td>99.00%</td>
    <td>10.59%</td>
    <td>34.00%</td>
  </tr>
  <tr>
    <td><pre><code>def double(n): return n*2</code></pre><pre><code>sorted(['z','a'])</code></pre></td>
    <td>14.29%</td>
    <td>7.69%</td>
    <td>0.00%</td>
    <td>11.11%</td>
    <td>99.00%</td>
    <td>37.62%</td>
    <td>42.00%</td>
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
    <td>83.33%</td>
    <td>71.43%</td>
    <td>83.33%</td>
    <td>85.71%</td>
    <td>100.00%</td>
    <td>71.28%</td>
    <td>49.00%</td>
  </tr>
  <tr>
    <td><pre><code>if not x: return False</code></pre><pre><code>if x == False: return False</code></pre></td>
    <td>61.54%</td>
    <td>50.00%</td>
    <td>14.29%</td>
    <td>50.00%</td>
    <td>100.00%</td>
    <td>92.23%</td>
    <td>46.00%</td>
  </tr>
  <tr>
    <td><pre><code>return True if x > 0 else False</code></pre><pre><code>if x > 0:
  return True
else:
  return False</code></pre></td>
    <td>70.59%</td>
    <td>77.78%</td>
    <td>11.11%</td>
    <td>60.00%</td>
    <td>99.00%</td>
    <td>79.27%</td>
    <td>46.00%</td>
  </tr>
  <tr>
    <td><pre><code>data = json.loads(s)</code></pre><pre><code>data = json.loads(str(s))</code></pre></td>
    <td>87.50%</td>
    <td>100.00%</td>
    <td>66.67%</td>
    <td>77.78%</td>
    <td>99.00%</td>
    <td>90.43%</td>
    <td>26.00%</td>
  </tr>
  <tr>
    <td><pre><code>x = [i for i in range(10) if i%2==0]</code></pre><pre><code>x = list(filter(lambda i: i%2==0, range(10)))</code></pre></td>
    <td>63.16%</td>
    <td>68.75%</td>
    <td>25.00%</td>
    <td>55.00%</td>
    <td>98.00%</td>
    <td>93.19%</td>
    <td>39.00%</td>
  </tr>
  <tr>
    <td><pre><code>for line in open('file.txt'):
  print(line)</code></pre><pre><code>with open('file.txt') as f:
  for line in f:
    print(line)</code></pre></td>
    <td>64.00%</td>
    <td>75.00%</td>
    <td>6.67%</td>
    <td>50.00%</td>
    <td>100.00%</td>
    <td>57.41%</td>
    <td>29.00%</td>
  </tr>
  <tr>
    <td><pre><code>def identity(x): return x</code></pre><pre><code>def echo(x): return x</code></pre></td>
    <td>100.00%</td>
    <td>100.00%</td>
    <td>100.00%</td>
    <td>100.00%</td>
    <td>100.00%</td>
    <td>24.13%</td>
    <td>48.00%</td>
  </tr>
  <tr>
    <td><pre><code>result = a if a > b else b</code></pre><pre><code>if a > b:
  result = a
else:
  result = b</code></pre></td>
    <td>52.17%</td>
    <td>71.43%</td>
    <td>7.69%</td>
    <td>41.67%</td>
    <td>99.00%</td>
    <td>67.55%</td>
    <td>43.00%</td>
  </tr>
  <tr>
    <td><pre><code>total += price</code></pre><pre><code>total = total + price</code></pre></td>
    <td>66.67%</td>
    <td>50.00%</td>
    <td>42.86%</td>
    <td>57.14%</td>
    <td>100.00%</td>
    <td>100.00%</td>
    <td>45.00%</td>
  </tr>
  <tr>
    <td><pre><code>if x in [1,2,3]: print(x)</code></pre><pre><code>if x == 1 or x == 2 or x == 3: print(x)</code></pre></td>
    <td>64.52%</td>
    <td>61.54%</td>
    <td>5.26%</td>
    <td>45.00%</td>
    <td>100.00%</td>
    <td>85.81%</td>
    <td>36.00%</td>
  </tr>
</table>
