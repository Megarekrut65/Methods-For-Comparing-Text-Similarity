
SIMILAR = [
    ("def sum(a, b): return a + b", "def add(x, y): return x + y", 98),
    ("for i in range(5): print(i)", "i = 0\nwhile i < 5:\n  print(i)\n  i += 1", 95),
    ("if x == True: return 1", "if x: return 1", 97),
    ("items = [x for x in range(10)]", "items = list(range(10))", 96),
    ("print('Hello, ' + name)", "print(f'Hello, {name}')", 98),
    ("def square(x): return x * x", "def sq(x): return pow(x, 2)", 92),
    ("a, b = b, a", "temp = a\na = b\nb = temp", 95),
    ("return len(s)", "count = 0\nfor _ in s:\n  count += 1\nreturn count", 93),
    ("try: f()\nexcept: pass", "try:\n  f()\nexcept Exception:\n  pass", 90),
    ("with open('file.txt') as f: data = f.read()", "f = open('file.txt')\ndata = f.read()\nf.close()", 91)
]

DIFFERENT = [
    ("print('Hello')", "x = 5 * 7", 0),
    ("def foo(): return True", "if x == 10: print(x)", 0),
    ("a = [1,2,3]", "import math", 0),
    ("while True: pass", "try: x = 1/0\nexcept: pass", 0),
    ("print(sum([1,2,3]))", "open('file.txt')", 0),
    ("x = x + 1", "print('Done')", 5),
    ("x = input()", "def bar(): pass", 0),
    ("for i in range(10): print(i)", "a = {'key': 'value'}", 0),
    ("raise ValueError('error')", "x = [None]*10", 0),
    ("def double(n): return n*2", "sorted(['z','a'])", 10)
]

SAME_SENSE = [
    ("def greet(): print('Hi')", "def greet(): print('Hello')", 90),
    ("if not x: return False", "if x == False: return False", 90),
    ("return True if x > 0 else False", "if x > 0:\n  return True\nelse:\n  return False", 85),
    ("data = json.loads(s)", "data = json.loads(str(s))", 80),
    ("x = [i for i in range(10) if i%2==0]", "x = list(filter(lambda i: i%2==0, range(10)))", 90),
    ("for line in open('file.txt'):\n  print(line)", "with open('file.txt') as f:\n  for line in f:\n    print(line)", 95),
    ("def identity(x): return x", "def echo(x): return x", 96),
    ("result = a if a > b else b", "if a > b:\n  result = a\nelse:\n  result = b", 98),
    ("total += price", "total = total + price", 95),
    ("if x in [1,2,3]: print(x)", "if x == 1 or x == 2 or x == 3: print(x)", 95)
]

TEXTS = {
"similar, with certain differences": SIMILAR,
"completely different": DIFFERENT,
"different, but with a common meaning": SAME_SENSE
}
