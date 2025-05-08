# Result

| Algorithm | Min diff | Max diff | Avg diff |
|-----------|----------|----------|----------|
| gestalt pattern matching | 0.00 | 81.67 | 36.55 |
| jaccard similarity | 0.00 | 98.00 | 42.41 |
| sklearn vectorizer | 0.00 | 98.00 | 48.93 |
| spacy semantic similarity | 0.00 | 98.00 | 30.76 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 0.00 | 53.97 | 16.65 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 0.00 | 59.63 | 17.79 |
| scratch similarity model | 22.03 | 85.58 | 50.27 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 0.00 | 50.54 | 15.28 |

# Examples
## simple examples
### 1.
**a)** Інформатика

**b)** Інформатика

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 100.00% | 100.00% | 0.00 |
| jaccard similarity | 100.00% | 100.00% | 0.00 |
| sklearn vectorizer | 100.00% | 100.00% | 0.00 |
| spacy semantic similarity | 100.00% | 100.00% | 0.00 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 100.00% | 100.00% | 0.00 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 100.00% | 100.00% | 0.00 |
| scratch similarity model | 54.07% | 100.00% | 45.93 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 100.00% | 100.00% | 0.00 |

---

### 2.
**a)** Математика

**b)** Матаметика

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 80.00% | 98.00% | 18.00 |
| jaccard similarity | 0.00% | 98.00% | 98.00 |
| sklearn vectorizer | 0.00% | 98.00% | 98.00 |
| spacy semantic similarity | 0.00% | 98.00% | 98.00 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 72.17% | 98.00% | 25.83 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 68.05% | 98.00% | 29.95 |
| scratch similarity model | 32.53% | 98.00% | 65.47 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 76.63% | 98.00% | 21.37 |

---

### 3.
**a)** Формула для розрахунку

**b)** Розрахункова формула

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 42.86% | 100.00% | 57.14 |
| jaccard similarity | 25.00% | 100.00% | 75.00 |
| sklearn vectorizer | 26.06% | 100.00% | 73.94 |
| spacy semantic similarity | 58.62% | 100.00% | 41.38 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 95.04% | 100.00% | 4.96 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 97.39% | 100.00% | 2.61 |
| scratch similarity model | 51.28% | 100.00% | 48.72 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 92.88% | 100.00% | 7.12 |

---

### 4.
**a)** Вчений знайшов неймовірний збіг

**b)** Неймовірний збіг був знайдений вченим

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 44.12% | 100.00% | 55.88 |
| jaccard similarity | 50.00% | 100.00% | 50.00 |
| sklearn vectorizer | 29.12% | 100.00% | 70.88 |
| spacy semantic similarity | 81.28% | 100.00% | 18.72 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 93.09% | 100.00% | 6.91 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 92.42% | 100.00% | 7.58 |
| scratch similarity model | 52.70% | 100.00% | 47.30 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 91.73% | 100.00% | 8.27 |

---

### 5.
**a)** Додаток

**b)** Застосунок

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 47.06% | 95.00% | 47.94 |
| jaccard similarity | 0.00% | 95.00% | 95.00 |
| sklearn vectorizer | 0.00% | 95.00% | 95.00 |
| spacy semantic similarity | 37.32% | 95.00% | 57.68 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 77.80% | 95.00% | 17.20 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 71.07% | 95.00% | 23.93 |
| scratch similarity model | 54.07% | 95.00% | 40.93 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 69.92% | 95.00% | 25.08 |

---

### 6.
**a)** Розробник

**b)** Програміст

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 21.05% | 95.00% | 73.95 |
| jaccard similarity | 0.00% | 95.00% | 95.00 |
| sklearn vectorizer | 0.00% | 95.00% | 95.00 |
| spacy semantic similarity | 50.65% | 95.00% | 44.35 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 71.13% | 95.00% | 23.87 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 76.29% | 95.00% | 18.71 |
| scratch similarity model | 54.07% | 95.00% | 40.93 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 66.86% | 95.00% | 28.14 |

---

### 7.
**a)** Дослідження

**b)** Бінарне дерево

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 8.00% | 0.00% | 8.00 |
| jaccard similarity | 0.00% | 0.00% | 0.00 |
| sklearn vectorizer | 0.00% | 0.00% | 0.00 |
| spacy semantic similarity | 25.37% | 0.00% | 25.37 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 40.14% | 0.00% | 40.14 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 25.12% | 0.00% | 25.12 |
| scratch similarity model | 54.07% | 0.00% | 54.07 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 31.40% | 0.00% | 31.40 |

---

### 8.
**a)** Застосунок

**b)** Рисунок

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 58.82% | 0.00% | 58.82 |
| jaccard similarity | 0.00% | 0.00% | 0.00 |
| sklearn vectorizer | 0.00% | 0.00% | 0.00 |
| spacy semantic similarity | 21.05% | 0.00% | 21.05 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 53.97% | 0.00% | 53.97 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 59.63% | 0.00% | 59.63 |
| scratch similarity model | 54.07% | 0.00% | 54.07 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 41.25% | 0.00% | 41.25 |

---

### 9.
**a)** Твердження було доведене

**b)** Розробник створив застосунок

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 15.38% | 0.00% | 15.38 |
| jaccard similarity | 0.00% | 0.00% | 0.00 |
| sklearn vectorizer | 0.00% | 0.00% | 0.00 |
| spacy semantic similarity | 25.73% | 0.00% | 25.73 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 35.62% | 0.00% | 35.62 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 23.53% | 0.00% | 23.53 |
| scratch similarity model | 77.18% | 0.00% | 77.18 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 18.40% | 0.00% | 18.40 |

---

## similar, with certain differences
### 1.
**a)** Йшла мати в магазин по печиво.

**b)** Мама йшла до магазину за печивом.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 66.67% | 98.00% | 31.33 |
| jaccard similarity | 27.27% | 98.00% | 70.73 |
| sklearn vectorizer | 10.16% | 98.00% | 87.84 |
| spacy semantic similarity | 69.28% | 98.00% | 28.72 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 80.86% | 98.00% | 17.14 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 97.65% | 98.00% | 0.35 |
| scratch similarity model | 41.84% | 98.00% | 56.16 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 81.53% | 98.00% | 16.47 |

---

### 2.
**a)** Кіт сидів на підвіконні й дивився у двір.

**b)** Кіт сидів на вікні та дивився у двір.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 89.74% | 99.00% | 9.26 |
| jaccard similarity | 63.64% | 99.00% | 35.36 |
| sklearn vectorizer | 63.28% | 99.00% | 35.72 |
| spacy semantic similarity | 97.43% | 99.00% | 1.57 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 91.91% | 99.00% | 7.09 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 97.71% | 99.00% | 1.29 |
| scratch similarity model | 42.59% | 99.00% | 56.41 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 90.71% | 99.00% | 8.29 |

---

### 3.
**a)** Він узяв книжку зі столу.

**b)** Він взяв книгу зі столу.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 89.80% | 100.00% | 10.20 |
| jaccard similarity | 50.00% | 100.00% | 50.00 |
| sklearn vectorizer | 43.16% | 100.00% | 56.84 |
| spacy semantic similarity | 98.87% | 100.00% | 1.13 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 99.58% | 100.00% | 0.42 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 99.58% | 100.00% | 0.42 |
| scratch similarity model | 33.29% | 100.00% | 66.71 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 99.11% | 100.00% | 0.89 |

---

### 4.
**a)** Машина швидко зникла за поворотом.

**b)** Автомобіль швидко зник за рогом.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 63.64% | 95.00% | 31.36 |
| jaccard similarity | 50.00% | 95.00% | 45.00 |
| sklearn vectorizer | 25.23% | 95.00% | 69.77 |
| spacy semantic similarity | 92.04% | 95.00% | 2.96 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 93.55% | 95.00% | 1.45 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 96.84% | 95.00% | 1.84 |
| scratch similarity model | 70.91% | 95.00% | 24.09 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 83.42% | 95.00% | 11.58 |

---

### 5.
**a)** Сонце сідало за горизонт, фарбуючи небо.

**b)** Сонце заходило за обрій, забарвлюючи небо.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 68.29% | 93.00% | 24.71 |
| jaccard similarity | 45.45% | 93.00% | 47.55 |
| sklearn vectorizer | 33.61% | 93.00% | 59.39 |
| spacy semantic similarity | 97.77% | 93.00% | 4.77 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 95.91% | 93.00% | 2.91 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 97.60% | 93.00% | 4.60 |
| scratch similarity model | 41.22% | 93.00% | 51.78 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 91.42% | 93.00% | 1.58 |

---

### 6.
**a)** Вона прокинулась від шуму на вулиці. Було ще темно.

**b)** Дівчина прокинулась через шум на вулиці. Надворі ще панувала темрява.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 66.67% | 90.00% | 23.33 |
| jaccard similarity | 31.25% | 90.00% | 58.75 |
| sklearn vectorizer | 26.97% | 90.00% | 63.03 |
| spacy semantic similarity | 89.63% | 90.00% | 0.37 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 91.40% | 90.00% | 1.40 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 94.54% | 90.00% | 4.54 |
| scratch similarity model | 36.10% | 90.00% | 53.90 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 88.51% | 90.00% | 1.49 |

---

### 7.
**a)** Я поклав листа у конверт. Потім вкинув його до скриньки.

**b)** Я поклав лист у конверт. Потому вкинув його в поштову скриню.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 85.47% | 98.00% | 12.53 |
| jaccard similarity | 53.33% | 98.00% | 44.67 |
| sklearn vectorizer | 33.61% | 98.00% | 64.39 |
| spacy semantic similarity | 92.70% | 98.00% | 5.30 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 96.41% | 98.00% | 1.59 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 96.20% | 98.00% | 1.80 |
| scratch similarity model | 60.66% | 98.00% | 37.34 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 93.95% | 98.00% | 4.05 |

---

### 8.
**a)** Дощ падав безупинно. Люди ховались під парасолями.

**b)** Злива лила без зупину. Люди ховалися під парасольками.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 75.00% | 95.00% | 20.00 |
| jaccard similarity | 30.77% | 95.00% | 64.23 |
| sklearn vectorizer | 15.59% | 95.00% | 79.41 |
| spacy semantic similarity | 85.88% | 95.00% | 9.12 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 71.42% | 95.00% | 23.58 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 94.74% | 95.00% | 0.26 |
| scratch similarity model | 72.97% | 95.00% | 22.03 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 59.82% | 95.00% | 35.18 |

---

### 9.
**a)** Ми довго йшли через поле. Вітер свистів у вухах.

**b)** Ми довго бродили полем. У вухах свистів вітер.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 61.70% | 98.00% | 36.30 |
| jaccard similarity | 58.33% | 98.00% | 39.67 |
| sklearn vectorizer | 50.56% | 98.00% | 47.44 |
| spacy semantic similarity | 93.29% | 98.00% | 4.71 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 98.69% | 98.00% | 0.69 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 95.97% | 98.00% | 2.03 |
| scratch similarity model | 71.53% | 98.00% | 26.47 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 98.53% | 98.00% | 0.53 |

---

### 10.
**a)** Я відкрив двері до кімнати. Всередині було темно. Я почув чийсь подих.

**b)** Я прочинив двері в кімнату. Там панувала темрява. І раптом я почув подих.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 60.14% | 93.00% | 32.86 |
| jaccard similarity | 31.58% | 93.00% | 61.42 |
| sklearn vectorizer | 18.98% | 93.00% | 74.02 |
| spacy semantic similarity | 93.22% | 93.00% | 0.22 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 96.15% | 93.00% | 3.15 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 95.78% | 93.00% | 2.78 |
| scratch similarity model | 29.30% | 93.00% | 63.70 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 92.07% | 93.00% | 0.93 |

---

## completely different
### 1.
**a)** На кухні пахло свіжим хлібом.

**b)** Собака гавкав на місяць усю ніч.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 22.95% | 0.00% | 22.95 |
| jaccard similarity | 18.18% | 0.00% | 18.18 |
| sklearn vectorizer | 10.16% | 0.00% | 10.16 |
| spacy semantic similarity | 62.27% | 0.00% | 62.27 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 7.55% | 0.00% | 7.55 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 17.96% | 0.00% | 17.96 |
| scratch similarity model | 71.78% | 0.00% | 71.78 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 1.44% | 0.00% | 1.44 |

---

### 2.
**a)** Вона закрила книжку й задумалась.

**b)** Поїзд щойно прибув на третій перон.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 23.53% | 0.00% | 23.53 |
| jaccard similarity | 8.33% | 0.00% | 8.33 |
| sklearn vectorizer | 0.00% | 0.00% | 0.00 |
| spacy semantic similarity | 51.30% | 0.00% | 51.30 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 10.62% | 0.00% | 10.62 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 17.19% | 0.00% | 17.19 |
| scratch similarity model | 58.74% | 0.00% | 58.74 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 5.24% | 0.00% | 5.24 |

---

### 3.
**a)** Годинник пробив північ.

**b)** Яблуко впало прямо в калюжу.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 31.37% | 0.00% | 31.37 |
| jaccard similarity | 11.11% | 0.00% | 11.11 |
| sklearn vectorizer | 0.00% | 0.00% | 0.00 |
| spacy semantic similarity | 60.91% | 0.00% | 60.91 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 13.33% | 0.00% | 13.33 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 33.37% | 0.00% | 33.37 |
| scratch similarity model | 63.41% | 0.00% | 63.41 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 8.34% | 0.00% | 8.34 |

---

### 4.
**a)** Він мріяв про політ у космос.

**b)** Чайник свистів на всю квартиру.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 23.33% | 0.00% | 23.33 |
| jaccard similarity | 8.33% | 0.00% | 8.33 |
| sklearn vectorizer | 0.00% | 0.00% | 0.00 |
| spacy semantic similarity | 60.76% | 0.00% | 60.76 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 16.04% | 0.00% | 16.04 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 8.54% | 0.00% | 8.54 |
| scratch similarity model | 38.87% | 0.00% | 38.87 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 5.50% | 0.00% | 5.50 |

---

### 5.
**a)** Море гриміло, наче злий бог прокинувся.

**b)** Сусід знову свердлить о сьомій ранку.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 28.95% | 0.00% | 28.95 |
| jaccard similarity | 7.14% | 0.00% | 7.14 |
| sklearn vectorizer | 0.00% | 0.00% | 0.00 |
| spacy semantic similarity | 50.48% | 0.00% | 50.48 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 17.72% | 0.00% | 17.72 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 40.94% | 0.00% | 40.94 |
| scratch similarity model | 55.36% | 0.00% | 55.36 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 4.46% | 0.00% | 4.46 |

---

### 6.
**a)** З полиці впала стара світлина.

**b)** Птах пролетів повз стару ялинку.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 45.16% | 5.00% | 40.16 |
| jaccard similarity | 20.00% | 5.00% | 15.00 |
| sklearn vectorizer | 0.00% | 5.00% | 5.00 |
| spacy semantic similarity | 55.26% | 5.00% | 50.26 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 33.08% | 5.00% | 28.08 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 56.99% | 5.00% | 51.99 |
| scratch similarity model | 61.90% | 5.00% | 56.90 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 27.30% | 5.00% | 22.30 |

---

### 7.
**a)** Натиснувши кнопку, він зник у тумані.

**b)** Сміх дитини лунав серед натовпу.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 11.59% | 0.00% | 11.59 |
| jaccard similarity | 7.69% | 0.00% | 7.69 |
| sklearn vectorizer | 0.00% | 0.00% | 0.00 |
| spacy semantic similarity | 58.56% | 0.00% | 58.56 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 14.35% | 0.00% | 14.35 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 35.67% | 0.00% | 35.67 |
| scratch similarity model | 58.35% | 0.00% | 58.35 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 6.70% | 0.00% | 6.70 |

---

### 8.
**a)** Вогонь тихо тріщав у каміні.

**b)** Годинник зупинився опівночі.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 21.43% | 0.00% | 21.43 |
| jaccard similarity | 11.11% | 0.00% | 11.11 |
| sklearn vectorizer | 0.00% | 0.00% | 0.00 |
| spacy semantic similarity | 68.84% | 0.00% | 68.84 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 19.79% | 0.00% | 19.79 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 38.61% | 0.00% | 38.61 |
| scratch similarity model | 24.88% | 0.00% | 24.88 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 3.00% | 0.00% | 3.00 |

---

### 9.
**a)** Перо ковзало по папері впевнено й швидко.

**b)** Її пальці грали мелодію без нот.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 27.40% | 0.00% | 27.40 |
| jaccard similarity | 7.14% | 0.00% | 7.14 |
| sklearn vectorizer | 0.00% | 0.00% | 0.00 |
| spacy semantic similarity | 55.91% | 0.00% | 55.91 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 21.31% | 0.00% | 21.31 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 35.34% | 0.00% | 35.34 |
| scratch similarity model | 66.95% | 0.00% | 66.95 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 13.76% | 0.00% | 13.76 |

---

### 10.
**a)** На вулиці загорілись ліхтарі.

**b)** Зірки спалахнули в нічному небі.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 26.23% | 10.00% | 16.23 |
| jaccard similarity | 10.00% | 10.00% | 0.00 |
| sklearn vectorizer | 0.00% | 10.00% | 10.00 |
| spacy semantic similarity | 66.41% | 10.00% | 56.41 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 46.92% | 10.00% | 36.92 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 62.97% | 10.00% | 52.97 |
| scratch similarity model | 58.59% | 10.00% | 48.59 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 43.06% | 10.00% | 33.06 |

---

## different, but with a common meaning
### 1.
**a)** Він заснув під час фільму.

**b)** Поки йшло кіно, він задрімав.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 25.45% | 90.00% | 64.55 |
| jaccard similarity | 18.18% | 90.00% | 71.82 |
| sklearn vectorizer | 11.23% | 90.00% | 78.77 |
| spacy semantic similarity | 65.53% | 90.00% | 24.47 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 92.51% | 90.00% | 2.51 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 91.35% | 90.00% | 1.35 |
| scratch similarity model | 23.23% | 90.00% | 66.77 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 91.28% | 90.00% | 1.28 |

---

### 2.
**a)** Я більше не хочу з тобою говорити.

**b)** Мені не цікаво продовжувати цю розмову.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 35.62% | 90.00% | 54.38 |
| jaccard similarity | 25.00% | 90.00% | 65.00 |
| sklearn vectorizer | 10.16% | 90.00% | 79.84 |
| spacy semantic similarity | 75.34% | 90.00% | 14.66 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 66.82% | 90.00% | 23.18 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 75.98% | 90.00% | 14.02 |
| scratch similarity model | 45.37% | 90.00% | 44.63 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 61.17% | 90.00% | 28.83 |

---

### 3.
**a)** Ми запізнились на поїзд.

**b)** Поїзд поїхав без нас.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 31.11% | 85.00% | 53.89 |
| jaccard similarity | 42.86% | 85.00% | 42.14 |
| sklearn vectorizer | 14.44% | 85.00% | 70.56 |
| spacy semantic similarity | 45.62% | 85.00% | 39.38 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 70.42% | 85.00% | 14.58 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 71.57% | 85.00% | 13.43 |
| scratch similarity model | 43.41% | 85.00% | 41.59 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 59.10% | 85.00% | 25.90 |

---

### 4.
**a)** Вона чудово співає.

**b)** У неї прекрасний голос.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 19.05% | 80.00% | 60.95 |
| jaccard similarity | 28.57% | 80.00% | 51.43 |
| sklearn vectorizer | 0.00% | 80.00% | 80.00 |
| spacy semantic similarity | 60.90% | 80.00% | 19.10 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 88.09% | 80.00% | 8.09 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 92.48% | 80.00% | 12.48 |
| scratch similarity model | 49.77% | 80.00% | 30.23 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 85.74% | 80.00% | 5.74 |

---

### 5.
**a)** Діти гралися на майданчику.

**b)** Малеча бавилась на вулиці.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 37.74% | 90.00% | 52.26 |
| jaccard similarity | 25.00% | 90.00% | 65.00 |
| sklearn vectorizer | 14.44% | 90.00% | 75.56 |
| spacy semantic similarity | 90.24% | 90.00% | 0.24 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 44.34% | 90.00% | 45.66 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 60.09% | 90.00% | 29.91 |
| scratch similarity model | 56.57% | 90.00% | 33.43 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 39.46% | 90.00% | 50.54 |

---

### 6.
**a)** Я не пам’ятаю його імені.

**b)** Його ім’я вилетіло в мене з голови.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 30.00% | 95.00% | 65.00 |
| jaccard similarity | 40.00% | 95.00% | 55.00 |
| sklearn vectorizer | 11.23% | 95.00% | 83.77 |
| spacy semantic similarity | 60.39% | 95.00% | 34.61 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 68.36% | 95.00% | 26.64 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 70.96% | 95.00% | 24.04 |
| scratch similarity model | 47.12% | 95.00% | 47.88 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 64.43% | 95.00% | 30.57 |

---

### 7.
**a)** Він мешкає за кордоном.

**b)** Зараз він живе в іншій країні.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 37.74% | 96.00% | 58.26 |
| jaccard similarity | 20.00% | 96.00% | 76.00 |
| sklearn vectorizer | 12.74% | 96.00% | 83.26 |
| spacy semantic similarity | 68.69% | 96.00% | 27.31 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 73.89% | 96.00% | 22.11 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 94.27% | 96.00% | 1.73 |
| scratch similarity model | 32.41% | 96.00% | 63.59 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 69.16% | 96.00% | 26.84 |

---

### 8.
**a)** Ця страва мені дуже подобається.

**b)** Я обожнюю цю їжу.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 16.33% | 98.00% | 81.67 |
| jaccard similarity | 37.50% | 98.00% | 60.50 |
| sklearn vectorizer | 0.00% | 98.00% | 98.00 |
| spacy semantic similarity | 59.01% | 98.00% | 38.99 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 87.66% | 98.00% | 10.34 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 92.74% | 98.00% | 5.26 |
| scratch similarity model | 52.07% | 98.00% | 45.93 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 85.86% | 98.00% | 12.14 |

---

### 9.
**a)** Мені потрібно трохи часу.

**b)** Дай мені ще кілька хвилин.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 27.45% | 95.00% | 67.55 |
| jaccard similarity | 22.22% | 95.00% | 72.78 |
| sklearn vectorizer | 12.74% | 95.00% | 82.26 |
| spacy semantic similarity | 76.07% | 95.00% | 18.93 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 76.08% | 95.00% | 18.92 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 67.39% | 95.00% | 27.61 |
| scratch similarity model | 9.42% | 95.00% | 85.58 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 71.43% | 95.00% | 23.57 |

---

### 10.
**a)** Вона завжди приходить вчасно.

**b)** Вона ніколи не запізнюється.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 42.11% | 95.00% | 52.89 |
| jaccard similarity | 25.00% | 95.00% | 70.00 |
| sklearn vectorizer | 14.44% | 95.00% | 80.56 |
| spacy semantic similarity | 79.71% | 95.00% | 15.29 |
| multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 71.47% | 95.00% | 23.53 |
| ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base) | 74.53% | 95.00% | 20.47 |
| scratch similarity model | 70.96% | 95.00% | 24.04 |
| fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2) | 70.42% | 95.00% | 24.58 |

---

