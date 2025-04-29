
**SIMILAR, WITH CERTAIN DIFFERENCES**

<table>
  <tr>
    <th>Text pairs</th>
    <th>gestalt pattern matching</th>
    <th>gestalt pattern matching from difflib</th>
    <th>jaccard algorithm with stanza lematization</th>
    <th>sklearn vectorizer</th>
    <th>semantic similarity with spacy</th>
    <th>sentence transformers tensor with codebert</th>
  </tr>
  <tr>
    <td><pre><code>def sum(a, b): return a + b</code></pre><pre><code>def add(x, y): return x + y</code></pre></td>
    <td>77.78%</td>
    <td>74.07%</td>
    <td>73.68%</td>
    <td>50.31%</td>
    <td>76.10%</td>
    <td>99.08%</td>
  </tr>
  <tr>
    <td><pre><code>for i in range(5): print(i)</code></pre><pre><code>i = 0
while i < 5:
  print(i)
  i += 1</code></pre></td>
    <td>52.31%</td>
    <td>46.15%</td>
    <td>45.83%</td>
    <td>22.03%</td>
    <td>70.98%</td>
    <td>92.73%</td>
  </tr>
  <tr>
    <td><pre><code>if x == True: return 1</code></pre><pre><code>if x: return 1</code></pre></td>
    <td>77.78%</td>
    <td>77.78%</td>
    <td>84.62%</td>
    <td>70.93%</td>
    <td>91.93%</td>
    <td>98.33%</td>
  </tr>
  <tr>
    <td><pre><code>items = [x for x in range(10)]</code></pre><pre><code>items = list(range(10))</code></pre></td>
    <td>67.92%</td>
    <td>67.92%</td>
    <td>71.43%</td>
    <td>51.01%</td>
    <td>80.03%</td>
    <td>97.60%</td>
  </tr>
  <tr>
    <td><pre><code>print('Hello, ' + name)</code></pre><pre><code>print(f'Hello, {name}')</code></pre></td>
    <td>86.96%</td>
    <td>82.61%</td>
    <td>80.00%</td>
    <td>100.00%</td>
    <td>86.83%</td>
    <td>97.74%</td>
  </tr>
  <tr>
    <td><pre><code>def square(x): return x * x</code></pre><pre><code>def sq(x): return pow(x, 2)</code></pre></td>
    <td>74.07%</td>
    <td>74.07%</td>
    <td>66.67%</td>
    <td>41.12%</td>
    <td>67.02%</td>
    <td>96.79%</td>
  </tr>
  <tr>
    <td><pre><code>a, b = b, a</code></pre><pre><code>temp = a
a = b
b = temp</code></pre></td>
    <td>52.94%</td>
    <td>35.29%</td>
    <td>40.00%</td>
    <td>0.00%</td>
    <td>79.58%</td>
    <td>94.79%</td>
  </tr>
  <tr>
    <td><pre><code>return len(s)</code></pre><pre><code>count = 0
for _ in s:
  count += 1
return count</code></pre></td>
    <td>30.00%</td>
    <td>26.67%</td>
    <td>33.33%</td>
    <td>12.16%</td>
    <td>65.39%</td>
    <td>94.11%</td>
  </tr>
  <tr>
    <td><pre><code>try: f()
except: pass</code></pre><pre><code>try:
  f()
except Exception:
  pass</code></pre></td>
    <td>75.00%</td>
    <td>75.00%</td>
    <td>78.95%</td>
    <td>77.65%</td>
    <td>98.87%</td>
    <td>98.63%</td>
  </tr>
  <tr>
    <td><pre><code>with open('file.txt') as f: data = f.read()</code></pre><pre><code>f = open('file.txt')
data = f.read()
f.close()</code></pre></td>
    <td>78.65%</td>
    <td>71.91%</td>
    <td>79.17%</td>
    <td>63.28%</td>
    <td>94.80%</td>
    <td>98.96%</td>
  </tr>
</table>

**COMPLETELY DIFFERENT**

<table>
  <tr>
    <th>Text pairs</th>
    <th>gestalt pattern matching</th>
    <th>gestalt pattern matching from difflib</th>
    <th>jaccard algorithm with stanza lematization</th>
    <th>sklearn vectorizer</th>
    <th>semantic similarity with spacy</th>
    <th>sentence transformers tensor with codebert</th>
  </tr>
  <tr>
    <td><pre><code>print('Hello')</code></pre><pre><code>x = 5 * 7</code></pre></td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>50.48%</td>
    <td>93.41%</td>
  </tr>
  <tr>
    <td><pre><code>def foo(): return True</code></pre><pre><code>if x == 10: print(x)</code></pre></td>
    <td>47.62%</td>
    <td>28.57%</td>
    <td>42.11%</td>
    <td>0.00%</td>
    <td>61.04%</td>
    <td>95.08%</td>
  </tr>
  <tr>
    <td><pre><code>a = [1,2,3]</code></pre><pre><code>import math</code></pre></td>
    <td>18.18%</td>
    <td>9.09%</td>
    <td>12.50%</td>
    <td>0.00%</td>
    <td>27.07%</td>
    <td>87.01%</td>
  </tr>
  <tr>
    <td><pre><code>while True: pass</code></pre><pre><code>try: x = 1/0
except: pass</code></pre></td>
    <td>48.78%</td>
    <td>39.02%</td>
    <td>31.82%</td>
    <td>20.20%</td>
    <td>71.18%</td>
    <td>94.40%</td>
  </tr>
  <tr>
    <td><pre><code>print(sum([1,2,3]))</code></pre><pre><code>open('file.txt')</code></pre></td>
    <td>34.29%</td>
    <td>22.86%</td>
    <td>26.09%</td>
    <td>0.00%</td>
    <td>72.84%</td>
    <td>94.63%</td>
  </tr>
  <tr>
    <td><pre><code>x = x + 1</code></pre><pre><code>print('Done')</code></pre></td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>44.22%</td>
    <td>91.45%</td>
  </tr>
  <tr>
    <td><pre><code>x = input()</code></pre><pre><code>def bar(): pass</code></pre></td>
    <td>38.46%</td>
    <td>23.08%</td>
    <td>22.22%</td>
    <td>0.00%</td>
    <td>60.25%</td>
    <td>96.98%</td>
  </tr>
  <tr>
    <td><pre><code>for i in range(10): print(i)</code></pre><pre><code>a = {'key': 'value'}</code></pre></td>
    <td>25.00%</td>
    <td>20.83%</td>
    <td>16.00%</td>
    <td>0.00%</td>
    <td>50.77%</td>
    <td>93.78%</td>
  </tr>
  <tr>
    <td><pre><code>raise ValueError('error')</code></pre><pre><code>x = [None]*10</code></pre></td>
    <td>15.79%</td>
    <td>5.26%</td>
    <td>13.04%</td>
    <td>0.00%</td>
    <td>44.61%</td>
    <td>95.61%</td>
  </tr>
  <tr>
    <td><pre><code>def double(n): return n*2</code></pre><pre><code>sorted(['z','a'])</code></pre></td>
    <td>33.33%</td>
    <td>14.29%</td>
    <td>30.43%</td>
    <td>0.00%</td>
    <td>36.13%</td>
    <td>91.52%</td>
  </tr>
</table>

**DIFFERENT, BUT WITH A COMMON MEANING**

<table>
  <tr>
    <th>Text pairs</th>
    <th>gestalt pattern matching</th>
    <th>gestalt pattern matching from difflib</th>
    <th>jaccard algorithm with stanza lematization</th>
    <th>sklearn vectorizer</th>
    <th>semantic similarity with spacy</th>
    <th>sentence transformers tensor with codebert</th>
  </tr>
  <tr>
    <td><pre><code>def greet(): print('Hi')</code></pre><pre><code>def greet(): print('Hello')</code></pre></td>
    <td>90.20%</td>
    <td>90.20%</td>
    <td>88.24%</td>
    <td>60.30%</td>
    <td>100.00%</td>
    <td>99.92%</td>
  </tr>
  <tr>
    <td><pre><code>if not x: return False</code></pre><pre><code>if x == False: return False</code></pre></td>
    <td>77.55%</td>
    <td>73.47%</td>
    <td>87.50%</td>
    <td>73.21%</td>
    <td>90.68%</td>
    <td>99.02%</td>
  </tr>
  <tr>
    <td><pre><code>return True if x > 0 else False</code></pre><pre><code>if x > 0:
  return True
else:
  return False</code></pre></td>
    <td>82.67%</td>
    <td>56.00%</td>
    <td>88.89%</td>
    <td>94.87%</td>
    <td>96.47%</td>
    <td>97.19%</td>
  </tr>
  <tr>
    <td><pre><code>data = json.loads(s)</code></pre><pre><code>data = json.loads(str(s))</code></pre></td>
    <td>88.89%</td>
    <td>88.89%</td>
    <td>92.86%</td>
    <td>77.65%</td>
    <td>97.34%</td>
    <td>94.80%</td>
  </tr>
  <tr>
    <td><pre><code>x = [i for i in range(10) if i%2==0]</code></pre><pre><code>x = list(filter(lambda i: i%2==0, range(10)))</code></pre></td>
    <td>66.67%</td>
    <td>51.85%</td>
    <td>59.26%</td>
    <td>25.23%</td>
    <td>83.56%</td>
    <td>94.76%</td>
  </tr>
  <tr>
    <td><pre><code>for line in open('file.txt'):
  print(line)</code></pre><pre><code>with open('file.txt') as f:
  for line in f:
    print(line)</code></pre></td>
    <td>83.50%</td>
    <td>64.08%</td>
    <td>80.95%</td>
    <td>84.66%</td>
    <td>87.81%</td>
    <td>98.96%</td>
  </tr>
  <tr>
    <td><pre><code>def identity(x): return x</code></pre><pre><code>def echo(x): return x</code></pre></td>
    <td>78.26%</td>
    <td>78.26%</td>
    <td>70.59%</td>
    <td>50.31%</td>
    <td>100.00%</td>
    <td>98.94%</td>
  </tr>
  <tr>
    <td><pre><code>result = a if a > b else b</code></pre><pre><code>if a > b:
  result = a
else:
  result = b</code></pre></td>
    <td>77.61%</td>
    <td>47.76%</td>
    <td>86.67%</td>
    <td>94.28%</td>
    <td>95.93%</td>
    <td>97.59%</td>
  </tr>
  <tr>
    <td><pre><code>total += price</code></pre><pre><code>total = total + price</code></pre></td>
    <td>80.00%</td>
    <td>74.29%</td>
    <td>100.00%</td>
    <td>94.87%</td>
    <td>97.69%</td>
    <td>97.85%</td>
  </tr>
  <tr>
    <td><pre><code>if x in [1,2,3]: print(x)</code></pre><pre><code>if x == 1 or x == 2 or x == 3: print(x)</code></pre></td>
    <td>59.38%</td>
    <td>59.38%</td>
    <td>73.68%</td>
    <td>31.88%</td>
    <td>80.82%</td>
    <td>96.71%</td>
  </tr>
</table>
