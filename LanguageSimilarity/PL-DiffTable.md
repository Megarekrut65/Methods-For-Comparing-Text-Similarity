
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
    <td>20.22</td>
    <td>23.93</td>
    <td>24.32</td>
    <td>47.69</td>
    <td>21.90</td>
    <td>1.08</td>
  </tr>
  <tr>
    <td><pre><code>for i in range(5): print(i)</code></pre><pre><code>i = 0
while i < 5:
  print(i)
  i += 1</code></pre></td>
    <td>42.69</td>
    <td>48.85</td>
    <td>49.17</td>
    <td>72.97</td>
    <td>24.02</td>
    <td>2.27</td>
  </tr>
  <tr>
    <td><pre><code>if x == True: return 1</code></pre><pre><code>if x: return 1</code></pre></td>
    <td>19.22</td>
    <td>19.22</td>
    <td>12.38</td>
    <td>26.07</td>
    <td>5.07</td>
    <td>1.33</td>
  </tr>
  <tr>
    <td><pre><code>items = [x for x in range(10)]</code></pre><pre><code>items = list(range(10))</code></pre></td>
    <td>28.08</td>
    <td>28.08</td>
    <td>24.57</td>
    <td>44.99</td>
    <td>15.97</td>
    <td>1.60</td>
  </tr>
  <tr>
    <td><pre><code>print('Hello, ' + name)</code></pre><pre><code>print(f'Hello, {name}')</code></pre></td>
    <td>11.04</td>
    <td>15.39</td>
    <td>18.00</td>
    <td>2.00</td>
    <td>11.17</td>
    <td>0.26</td>
  </tr>
  <tr>
    <td><pre><code>def square(x): return x * x</code></pre><pre><code>def sq(x): return pow(x, 2)</code></pre></td>
    <td>17.93</td>
    <td>17.93</td>
    <td>25.33</td>
    <td>50.88</td>
    <td>24.98</td>
    <td>4.79</td>
  </tr>
  <tr>
    <td><pre><code>a, b = b, a</code></pre><pre><code>temp = a
a = b
b = temp</code></pre></td>
    <td>42.06</td>
    <td>59.71</td>
    <td>55.00</td>
    <td>95.00</td>
    <td>15.42</td>
    <td>0.21</td>
  </tr>
  <tr>
    <td><pre><code>return len(s)</code></pre><pre><code>count = 0
for _ in s:
  count += 1
return count</code></pre></td>
    <td>63.00</td>
    <td>66.33</td>
    <td>59.67</td>
    <td>80.84</td>
    <td>27.61</td>
    <td>1.11</td>
  </tr>
  <tr>
    <td><pre><code>try: f()
except: pass</code></pre><pre><code>try:
  f()
except Exception:
  pass</code></pre></td>
    <td>15.00</td>
    <td>15.00</td>
    <td>11.05</td>
    <td>12.35</td>
    <td>8.87</td>
    <td>8.63</td>
  </tr>
  <tr>
    <td><pre><code>with open('file.txt') as f: data = f.read()</code></pre><pre><code>f = open('file.txt')
data = f.read()
f.close()</code></pre></td>
    <td>12.35</td>
    <td>19.09</td>
    <td>11.83</td>
    <td>27.72</td>
    <td>3.80</td>
    <td>7.96</td>
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
    <td>0.00</td>
    <td>0.00</td>
    <td>0.00</td>
    <td>0.00</td>
    <td>50.48</td>
    <td>93.41</td>
  </tr>
  <tr>
    <td><pre><code>def foo(): return True</code></pre><pre><code>if x == 10: print(x)</code></pre></td>
    <td>47.62</td>
    <td>28.57</td>
    <td>42.11</td>
    <td>0.00</td>
    <td>61.04</td>
    <td>95.08</td>
  </tr>
  <tr>
    <td><pre><code>a = [1,2,3]</code></pre><pre><code>import math</code></pre></td>
    <td>18.18</td>
    <td>9.09</td>
    <td>12.50</td>
    <td>0.00</td>
    <td>27.07</td>
    <td>87.01</td>
  </tr>
  <tr>
    <td><pre><code>while True: pass</code></pre><pre><code>try: x = 1/0
except: pass</code></pre></td>
    <td>48.78</td>
    <td>39.02</td>
    <td>31.82</td>
    <td>20.20</td>
    <td>71.18</td>
    <td>94.40</td>
  </tr>
  <tr>
    <td><pre><code>print(sum([1,2,3]))</code></pre><pre><code>open('file.txt')</code></pre></td>
    <td>34.29</td>
    <td>22.86</td>
    <td>26.09</td>
    <td>0.00</td>
    <td>72.84</td>
    <td>94.63</td>
  </tr>
  <tr>
    <td><pre><code>x = x + 1</code></pre><pre><code>print('Done')</code></pre></td>
    <td>5.00</td>
    <td>5.00</td>
    <td>5.00</td>
    <td>5.00</td>
    <td>39.22</td>
    <td>86.45</td>
  </tr>
  <tr>
    <td><pre><code>x = input()</code></pre><pre><code>def bar(): pass</code></pre></td>
    <td>38.46</td>
    <td>23.08</td>
    <td>22.22</td>
    <td>0.00</td>
    <td>60.25</td>
    <td>96.98</td>
  </tr>
  <tr>
    <td><pre><code>for i in range(10): print(i)</code></pre><pre><code>a = {'key': 'value'}</code></pre></td>
    <td>25.00</td>
    <td>20.83</td>
    <td>16.00</td>
    <td>0.00</td>
    <td>50.77</td>
    <td>93.78</td>
  </tr>
  <tr>
    <td><pre><code>raise ValueError('error')</code></pre><pre><code>x = [None]*10</code></pre></td>
    <td>15.79</td>
    <td>5.26</td>
    <td>13.04</td>
    <td>0.00</td>
    <td>44.61</td>
    <td>95.61</td>
  </tr>
  <tr>
    <td><pre><code>def double(n): return n*2</code></pre><pre><code>sorted(['z','a'])</code></pre></td>
    <td>23.33</td>
    <td>4.29</td>
    <td>20.43</td>
    <td>10.00</td>
    <td>26.13</td>
    <td>81.52</td>
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
    <td>0.20</td>
    <td>0.20</td>
    <td>1.76</td>
    <td>29.70</td>
    <td>10.00</td>
    <td>9.92</td>
  </tr>
  <tr>
    <td><pre><code>if not x: return False</code></pre><pre><code>if x == False: return False</code></pre></td>
    <td>12.45</td>
    <td>16.53</td>
    <td>2.50</td>
    <td>16.79</td>
    <td>0.68</td>
    <td>9.02</td>
  </tr>
  <tr>
    <td><pre><code>return True if x > 0 else False</code></pre><pre><code>if x > 0:
  return True
else:
  return False</code></pre></td>
    <td>2.33</td>
    <td>29.00</td>
    <td>3.89</td>
    <td>9.87</td>
    <td>11.47</td>
    <td>12.19</td>
  </tr>
  <tr>
    <td><pre><code>data = json.loads(s)</code></pre><pre><code>data = json.loads(str(s))</code></pre></td>
    <td>8.89</td>
    <td>8.89</td>
    <td>12.86</td>
    <td>2.35</td>
    <td>17.34</td>
    <td>14.80</td>
  </tr>
  <tr>
    <td><pre><code>x = [i for i in range(10) if i%2==0]</code></pre><pre><code>x = list(filter(lambda i: i%2==0, range(10)))</code></pre></td>
    <td>23.33</td>
    <td>38.15</td>
    <td>30.74</td>
    <td>64.77</td>
    <td>6.44</td>
    <td>4.76</td>
  </tr>
  <tr>
    <td><pre><code>for line in open('file.txt'):
  print(line)</code></pre><pre><code>with open('file.txt') as f:
  for line in f:
    print(line)</code></pre></td>
    <td>11.50</td>
    <td>30.92</td>
    <td>14.05</td>
    <td>10.34</td>
    <td>7.19</td>
    <td>3.96</td>
  </tr>
  <tr>
    <td><pre><code>def identity(x): return x</code></pre><pre><code>def echo(x): return x</code></pre></td>
    <td>17.74</td>
    <td>17.74</td>
    <td>25.41</td>
    <td>45.69</td>
    <td>4.00</td>
    <td>2.94</td>
  </tr>
  <tr>
    <td><pre><code>result = a if a > b else b</code></pre><pre><code>if a > b:
  result = a
else:
  result = b</code></pre></td>
    <td>20.39</td>
    <td>50.24</td>
    <td>11.33</td>
    <td>3.72</td>
    <td>2.07</td>
    <td>0.41</td>
  </tr>
  <tr>
    <td><pre><code>total += price</code></pre><pre><code>total = total + price</code></pre></td>
    <td>15.00</td>
    <td>20.71</td>
    <td>5.00</td>
    <td>0.13</td>
    <td>2.69</td>
    <td>2.85</td>
  </tr>
  <tr>
    <td><pre><code>if x in [1,2,3]: print(x)</code></pre><pre><code>if x == 1 or x == 2 or x == 3: print(x)</code></pre></td>
    <td>35.62</td>
    <td>35.62</td>
    <td>21.32</td>
    <td>63.12</td>
    <td>14.18</td>
    <td>1.71</td>
  </tr>
</table>
