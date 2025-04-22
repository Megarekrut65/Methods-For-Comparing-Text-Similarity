# Result

| Algorithm | Min diff | Max diff | Avg diff |
|-----------|----------|----------|----------|
| gestalt pattern matching | 9.26 | 69.57 | 35.20 |
| gestalt pattern matching from difflib | 9.26 | 81.67 | 36.34 |
| jaccard algorithm with stanza lematization | 9.81 | 70.00 | 38.65 |
| sklearn vectorizer | 0.00 | 98.00 | 49.19 |
| semantic similarity with spacy | 0.22 | 68.84 | 28.92 |
| sentence transformers tensor with multilanguage vectors | 0.42 | 45.66 | 14.69 |
| sentence transformers tensor with ukrainian vectors | 0.26 | 52.97 | 16.76 |
| fine tuned similarity model | 0.53 | 50.54 | 13.83 |

# Examples
## similar, with certain differences
### 1.
**a)** Йшла мати в магазин по печиво.

**b)** Мама йшла до магазину за печивом.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 79.37% | 98.00% | 18.63 |
| gestalt pattern matching from difflib | 66.67% | 98.00% | 31.33 |
| jaccard algorithm with stanza lematization | 71.43% | 98.00% | 26.57 |
| sklearn vectorizer | 10.16% | 98.00% | 87.84 |
| semantic similarity with spacy | 69.28% | 98.00% | 28.72 |
| sentence transformers tensor with multilanguage vectors | 80.86% | 98.00% | 17.14 |
| sentence transformers tensor with ukrainian vectors | 97.65% | 98.00% | 0.35 |
| fine tuned similarity model | 81.53% | 98.00% | 16.47 |

---

### 2.
**a)** Кіт сидів на підвіконні й дивився у двір.

**b)** Кіт сидів на вікні та дивився у двір.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 89.74% | 99.00% | 9.26 |
| gestalt pattern matching from difflib | 89.74% | 99.00% | 9.26 |
| jaccard algorithm with stanza lematization | 83.33% | 99.00% | 15.67 |
| sklearn vectorizer | 63.28% | 99.00% | 35.72 |
| semantic similarity with spacy | 97.43% | 99.00% | 1.57 |
| sentence transformers tensor with multilanguage vectors | 91.91% | 99.00% | 7.09 |
| sentence transformers tensor with ukrainian vectors | 97.71% | 99.00% | 1.29 |
| fine tuned similarity model | 90.71% | 99.00% | 8.29 |

---

### 3.
**a)** Він узяв книжку зі столу.

**b)** Він взяв книгу зі столу.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 89.80% | 100.00% | 10.20 |
| gestalt pattern matching from difflib | 89.80% | 100.00% | 10.20 |
| jaccard algorithm with stanza lematization | 88.24% | 100.00% | 11.76 |
| sklearn vectorizer | 43.16% | 100.00% | 56.84 |
| semantic similarity with spacy | 98.87% | 100.00% | 1.13 |
| sentence transformers tensor with multilanguage vectors | 99.58% | 100.00% | 0.42 |
| sentence transformers tensor with ukrainian vectors | 99.58% | 100.00% | 0.42 |
| fine tuned similarity model | 99.11% | 100.00% | 0.89 |

---

### 4.
**a)** Машина швидко зникла за поворотом.

**b)** Автомобіль швидко зник за рогом.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 78.79% | 95.00% | 16.21 |
| gestalt pattern matching from difflib | 63.64% | 95.00% | 31.36 |
| jaccard algorithm with stanza lematization | 68.18% | 95.00% | 26.82 |
| sklearn vectorizer | 25.23% | 95.00% | 69.77 |
| semantic similarity with spacy | 92.04% | 95.00% | 2.96 |
| sentence transformers tensor with multilanguage vectors | 93.55% | 95.00% | 1.45 |
| sentence transformers tensor with ukrainian vectors | 96.84% | 95.00% | 1.84 |
| fine tuned similarity model | 83.42% | 95.00% | 11.58 |

---

### 5.
**a)** Сонце сідало за горизонт, фарбуючи небо.

**b)** Сонце заходило за обрій, забарвлюючи небо.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 82.93% | 93.00% | 10.07 |
| gestalt pattern matching from difflib | 68.29% | 93.00% | 24.71 |
| jaccard algorithm with stanza lematization | 69.23% | 93.00% | 23.77 |
| sklearn vectorizer | 33.61% | 93.00% | 59.39 |
| semantic similarity with spacy | 97.77% | 93.00% | 4.77 |
| sentence transformers tensor with multilanguage vectors | 95.91% | 93.00% | 2.91 |
| sentence transformers tensor with ukrainian vectors | 97.60% | 93.00% | 4.60 |
| fine tuned similarity model | 91.42% | 93.00% | 1.58 |

---

### 6.
**a)** Вона прокинулась від шуму на вулиці. Було ще темно.

**b)** Дівчина прокинулась через шум на вулиці. Надворі ще панувала темрява.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 76.67% | 90.00% | 13.33 |
| gestalt pattern matching from difflib | 66.67% | 90.00% | 23.33 |
| jaccard algorithm with stanza lematization | 75.86% | 90.00% | 14.14 |
| sklearn vectorizer | 26.97% | 90.00% | 63.03 |
| semantic similarity with spacy | 89.63% | 90.00% | 0.37 |
| sentence transformers tensor with multilanguage vectors | 91.40% | 90.00% | 1.40 |
| sentence transformers tensor with ukrainian vectors | 94.54% | 90.00% | 4.54 |
| fine tuned similarity model | 88.51% | 90.00% | 1.49 |

---

### 7.
**a)** Я поклав листа у конверт. Потім вкинув його до скриньки.

**b)** Я поклав лист у конверт. Потому вкинув його в поштову скриню.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 85.47% | 98.00% | 12.53 |
| gestalt pattern matching from difflib | 85.47% | 98.00% | 12.53 |
| jaccard algorithm with stanza lematization | 80.00% | 98.00% | 18.00 |
| sklearn vectorizer | 33.61% | 98.00% | 64.39 |
| semantic similarity with spacy | 92.70% | 98.00% | 5.30 |
| sentence transformers tensor with multilanguage vectors | 96.41% | 98.00% | 1.59 |
| sentence transformers tensor with ukrainian vectors | 96.20% | 98.00% | 1.80 |
| fine tuned similarity model | 93.95% | 98.00% | 4.05 |

---

### 8.
**a)** Дощ падав безупинно. Люди ховались під парасолями.

**b)** Злива лила без зупину. Люди ховалися під парасольками.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 82.69% | 95.00% | 12.31 |
| gestalt pattern matching from difflib | 75.00% | 95.00% | 20.00 |
| jaccard algorithm with stanza lematization | 85.19% | 95.00% | 9.81 |
| sklearn vectorizer | 15.59% | 95.00% | 79.41 |
| semantic similarity with spacy | 85.88% | 95.00% | 9.12 |
| sentence transformers tensor with multilanguage vectors | 71.42% | 95.00% | 23.58 |
| sentence transformers tensor with ukrainian vectors | 94.74% | 95.00% | 0.26 |
| fine tuned similarity model | 59.82% | 95.00% | 35.18 |

---

### 9.
**a)** Ми довго йшли через поле. Вітер свистів у вухах.

**b)** Ми довго бродили полем. У вухах свистів вітер.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 82.98% | 98.00% | 15.02 |
| gestalt pattern matching from difflib | 61.70% | 98.00% | 36.30 |
| jaccard algorithm with stanza lematization | 69.23% | 98.00% | 28.77 |
| sklearn vectorizer | 50.56% | 98.00% | 47.44 |
| semantic similarity with spacy | 93.29% | 98.00% | 4.71 |
| sentence transformers tensor with multilanguage vectors | 98.69% | 98.00% | 0.69 |
| sentence transformers tensor with ukrainian vectors | 95.97% | 98.00% | 2.03 |
| fine tuned similarity model | 98.53% | 98.00% | 0.53 |

---

### 10.
**a)** Я відкрив двері до кімнати. Всередині було темно. Я почув чийсь подих.

**b)** Я прочинив двері в кімнату. Там панувала темрява. І раптом я почув подих.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 72.73% | 93.00% | 20.27 |
| gestalt pattern matching from difflib | 60.14% | 93.00% | 32.86 |
| jaccard algorithm with stanza lematization | 71.43% | 93.00% | 21.57 |
| sklearn vectorizer | 18.98% | 93.00% | 74.02 |
| semantic similarity with spacy | 93.22% | 93.00% | 0.22 |
| sentence transformers tensor with multilanguage vectors | 96.15% | 93.00% | 3.15 |
| sentence transformers tensor with ukrainian vectors | 95.78% | 93.00% | 2.78 |
| fine tuned similarity model | 92.07% | 93.00% | 0.93 |

---

## completely different
### 1.
**a)** На кухні пахло свіжим хлібом.

**b)** Собака гавкав на місяць усю ніч.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 55.74% | 0.00% | 55.74 |
| gestalt pattern matching from difflib | 22.95% | 0.00% | 22.95 |
| jaccard algorithm with stanza lematization | 48.00% | 0.00% | 48.00 |
| sklearn vectorizer | 10.16% | 0.00% | 10.16 |
| semantic similarity with spacy | 62.27% | 0.00% | 62.27 |
| sentence transformers tensor with multilanguage vectors | 7.55% | 0.00% | 7.55 |
| sentence transformers tensor with ukrainian vectors | 17.96% | 0.00% | 17.96 |
| fine tuned similarity model | 1.44% | 0.00% | 1.44 |

---

### 2.
**a)** Вона закрила книжку й задумалась.

**b)** Поїзд щойно прибув на третій перон.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 44.12% | 0.00% | 44.12 |
| gestalt pattern matching from difflib | 23.53% | 0.00% | 23.53 |
| jaccard algorithm with stanza lematization | 40.74% | 0.00% | 40.74 |
| sklearn vectorizer | 0.00% | 0.00% | 0.00 |
| semantic similarity with spacy | 51.30% | 0.00% | 51.30 |
| sentence transformers tensor with multilanguage vectors | 10.62% | 0.00% | 10.62 |
| sentence transformers tensor with ukrainian vectors | 17.19% | 0.00% | 17.19 |
| fine tuned similarity model | 5.24% | 0.00% | 5.24 |

---

### 3.
**a)** Годинник пробив північ.

**b)** Яблуко впало прямо в калюжу.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 47.06% | 0.00% | 47.06 |
| gestalt pattern matching from difflib | 31.37% | 0.00% | 31.37 |
| jaccard algorithm with stanza lematization | 36.36% | 0.00% | 36.36 |
| sklearn vectorizer | 0.00% | 0.00% | 0.00 |
| semantic similarity with spacy | 60.91% | 0.00% | 60.91 |
| sentence transformers tensor with multilanguage vectors | 13.33% | 0.00% | 13.33 |
| sentence transformers tensor with ukrainian vectors | 33.37% | 0.00% | 33.37 |
| fine tuned similarity model | 8.34% | 0.00% | 8.34 |

---

### 4.
**a)** Він мріяв про політ у космос.

**b)** Чайник свистів на всю квартиру.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 50.00% | 0.00% | 50.00 |
| gestalt pattern matching from difflib | 23.33% | 0.00% | 23.33 |
| jaccard algorithm with stanza lematization | 47.62% | 0.00% | 47.62 |
| sklearn vectorizer | 0.00% | 0.00% | 0.00 |
| semantic similarity with spacy | 60.76% | 0.00% | 60.76 |
| sentence transformers tensor with multilanguage vectors | 16.04% | 0.00% | 16.04 |
| sentence transformers tensor with ukrainian vectors | 8.54% | 0.00% | 8.54 |
| fine tuned similarity model | 5.50% | 0.00% | 5.50 |

---

### 5.
**a)** Море гриміло, наче злий бог прокинувся.

**b)** Сусід знову свердлить о сьомій ранку.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 65.79% | 0.00% | 65.79 |
| gestalt pattern matching from difflib | 28.95% | 0.00% | 28.95 |
| jaccard algorithm with stanza lematization | 60.71% | 0.00% | 60.71 |
| sklearn vectorizer | 0.00% | 0.00% | 0.00 |
| semantic similarity with spacy | 50.48% | 0.00% | 50.48 |
| sentence transformers tensor with multilanguage vectors | 17.72% | 0.00% | 17.72 |
| sentence transformers tensor with ukrainian vectors | 40.94% | 0.00% | 40.94 |
| fine tuned similarity model | 4.46% | 0.00% | 4.46 |

---

### 6.
**a)** З полиці впала стара світлина.

**b)** Птах пролетів повз стару ялинку.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 67.74% | 5.00% | 62.74 |
| gestalt pattern matching from difflib | 45.16% | 5.00% | 40.16 |
| jaccard algorithm with stanza lematization | 59.09% | 5.00% | 54.09 |
| sklearn vectorizer | 0.00% | 5.00% | 5.00 |
| semantic similarity with spacy | 55.26% | 5.00% | 50.26 |
| sentence transformers tensor with multilanguage vectors | 33.08% | 5.00% | 28.08 |
| sentence transformers tensor with ukrainian vectors | 56.99% | 5.00% | 51.99 |
| fine tuned similarity model | 27.30% | 5.00% | 22.30 |

---

### 7.
**a)** Натиснувши кнопку, він зник у тумані.

**b)** Сміх дитини лунав серед натовпу.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 69.57% | 0.00% | 69.57 |
| gestalt pattern matching from difflib | 11.59% | 0.00% | 11.59 |
| jaccard algorithm with stanza lematization | 54.17% | 0.00% | 54.17 |
| sklearn vectorizer | 0.00% | 0.00% | 0.00 |
| semantic similarity with spacy | 58.56% | 0.00% | 58.56 |
| sentence transformers tensor with multilanguage vectors | 14.35% | 0.00% | 14.35 |
| sentence transformers tensor with ukrainian vectors | 35.67% | 0.00% | 35.67 |
| fine tuned similarity model | 6.70% | 0.00% | 6.70 |

---

### 8.
**a)** Вогонь тихо тріщав у каміні.

**b)** Годинник зупинився опівночі.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 50.00% | 0.00% | 50.00 |
| gestalt pattern matching from difflib | 21.43% | 0.00% | 21.43 |
| jaccard algorithm with stanza lematization | 36.00% | 0.00% | 36.00 |
| sklearn vectorizer | 0.00% | 0.00% | 0.00 |
| semantic similarity with spacy | 68.84% | 0.00% | 68.84 |
| sentence transformers tensor with multilanguage vectors | 19.79% | 0.00% | 19.79 |
| sentence transformers tensor with ukrainian vectors | 38.61% | 0.00% | 38.61 |
| fine tuned similarity model | 3.00% | 0.00% | 3.00 |

---

### 9.
**a)** Перо ковзало по папері впевнено й швидко.

**b)** Її пальці грали мелодію без нот.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 54.79% | 0.00% | 54.79 |
| gestalt pattern matching from difflib | 27.40% | 0.00% | 27.40 |
| jaccard algorithm with stanza lematization | 48.15% | 0.00% | 48.15 |
| sklearn vectorizer | 0.00% | 0.00% | 0.00 |
| semantic similarity with spacy | 55.91% | 0.00% | 55.91 |
| sentence transformers tensor with multilanguage vectors | 21.31% | 0.00% | 21.31 |
| sentence transformers tensor with ukrainian vectors | 35.34% | 0.00% | 35.34 |
| fine tuned similarity model | 13.76% | 0.00% | 13.76 |

---

### 10.
**a)** На вулиці загорілись ліхтарі.

**b)** Зірки спалахнули в нічному небі.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 62.30% | 10.00% | 52.30 |
| gestalt pattern matching from difflib | 26.23% | 10.00% | 16.23 |
| jaccard algorithm with stanza lematization | 46.15% | 10.00% | 36.15 |
| sklearn vectorizer | 0.00% | 10.00% | 10.00 |
| semantic similarity with spacy | 66.41% | 10.00% | 56.41 |
| sentence transformers tensor with multilanguage vectors | 46.92% | 10.00% | 36.92 |
| sentence transformers tensor with ukrainian vectors | 62.97% | 10.00% | 52.97 |
| fine tuned similarity model | 43.06% | 10.00% | 33.06 |

---

## different, but with a common meaning
### 1.
**a)** Він заснув під час фільму.

**b)** Поки йшло кіно, він задрімав.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 61.82% | 90.00% | 28.18 |
| gestalt pattern matching from difflib | 25.45% | 90.00% | 64.55 |
| jaccard algorithm with stanza lematization | 40.00% | 90.00% | 50.00 |
| sklearn vectorizer | 11.23% | 90.00% | 78.77 |
| semantic similarity with spacy | 65.53% | 90.00% | 24.47 |
| sentence transformers tensor with multilanguage vectors | 92.51% | 90.00% | 2.51 |
| sentence transformers tensor with ukrainian vectors | 91.35% | 90.00% | 1.35 |
| fine tuned similarity model | 91.28% | 90.00% | 1.28 |

---

### 2.
**a)** Я більше не хочу з тобою говорити.

**b)** Мені не цікаво продовжувати цю розмову.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 60.27% | 90.00% | 29.73 |
| gestalt pattern matching from difflib | 35.62% | 90.00% | 54.38 |
| jaccard algorithm with stanza lematization | 44.83% | 90.00% | 45.17 |
| sklearn vectorizer | 10.16% | 90.00% | 79.84 |
| semantic similarity with spacy | 75.34% | 90.00% | 14.66 |
| sentence transformers tensor with multilanguage vectors | 66.82% | 90.00% | 23.18 |
| sentence transformers tensor with ukrainian vectors | 75.98% | 90.00% | 14.02 |
| fine tuned similarity model | 61.17% | 90.00% | 28.83 |

---

### 3.
**a)** Ми запізнились на поїзд.

**b)** Поїзд поїхав без нас.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 62.22% | 85.00% | 22.78 |
| gestalt pattern matching from difflib | 31.11% | 85.00% | 53.89 |
| jaccard algorithm with stanza lematization | 50.00% | 85.00% | 35.00 |
| sklearn vectorizer | 14.44% | 85.00% | 70.56 |
| semantic similarity with spacy | 45.62% | 85.00% | 39.38 |
| sentence transformers tensor with multilanguage vectors | 70.42% | 85.00% | 14.58 |
| sentence transformers tensor with ukrainian vectors | 71.57% | 85.00% | 13.43 |
| fine tuned similarity model | 59.10% | 85.00% | 25.90 |

---

### 4.
**a)** Вона чудово співає.

**b)** У неї прекрасний голос.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 42.86% | 80.00% | 37.14 |
| gestalt pattern matching from difflib | 19.05% | 80.00% | 60.95 |
| jaccard algorithm with stanza lematization | 30.43% | 80.00% | 49.57 |
| sklearn vectorizer | 0.00% | 80.00% | 80.00 |
| semantic similarity with spacy | 60.90% | 80.00% | 19.10 |
| sentence transformers tensor with multilanguage vectors | 88.09% | 80.00% | 8.09 |
| sentence transformers tensor with ukrainian vectors | 92.48% | 80.00% | 12.48 |
| fine tuned similarity model | 85.74% | 80.00% | 5.74 |

---

### 5.
**a)** Діти гралися на майданчику.

**b)** Малеча бавилась на вулиці.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 60.38% | 90.00% | 29.62 |
| gestalt pattern matching from difflib | 37.74% | 90.00% | 52.26 |
| jaccard algorithm with stanza lematization | 40.00% | 90.00% | 50.00 |
| sklearn vectorizer | 14.44% | 90.00% | 75.56 |
| semantic similarity with spacy | 90.24% | 90.00% | 0.24 |
| sentence transformers tensor with multilanguage vectors | 44.34% | 90.00% | 45.66 |
| sentence transformers tensor with ukrainian vectors | 60.09% | 90.00% | 29.91 |
| fine tuned similarity model | 39.46% | 90.00% | 50.54 |

---

### 6.
**a)** Я не пам’ятаю його імені.

**b)** Його ім’я вилетіло в мене з голови.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 60.00% | 95.00% | 35.00 |
| gestalt pattern matching from difflib | 30.00% | 95.00% | 65.00 |
| jaccard algorithm with stanza lematization | 52.38% | 95.00% | 42.62 |
| sklearn vectorizer | 11.23% | 95.00% | 83.77 |
| semantic similarity with spacy | 60.39% | 95.00% | 34.61 |
| sentence transformers tensor with multilanguage vectors | 68.36% | 95.00% | 26.64 |
| sentence transformers tensor with ukrainian vectors | 70.96% | 95.00% | 24.04 |
| fine tuned similarity model | 64.43% | 95.00% | 30.57 |

---

### 7.
**a)** Він мешкає за кордоном.

**b)** Зараз він живе в іншій країні.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 52.83% | 96.00% | 43.17 |
| gestalt pattern matching from difflib | 37.74% | 96.00% | 58.26 |
| jaccard algorithm with stanza lematization | 47.62% | 96.00% | 48.38 |
| sklearn vectorizer | 12.74% | 96.00% | 83.26 |
| semantic similarity with spacy | 68.69% | 96.00% | 27.31 |
| sentence transformers tensor with multilanguage vectors | 73.89% | 96.00% | 22.11 |
| sentence transformers tensor with ukrainian vectors | 94.27% | 96.00% | 1.73 |
| fine tuned similarity model | 69.16% | 96.00% | 26.84 |

---

### 8.
**a)** Ця страва мені дуже подобається.

**b)** Я обожнюю цю їжу.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 40.82% | 98.00% | 57.18 |
| gestalt pattern matching from difflib | 16.33% | 98.00% | 81.67 |
| jaccard algorithm with stanza lematization | 28.00% | 98.00% | 70.00 |
| sklearn vectorizer | 0.00% | 98.00% | 98.00 |
| semantic similarity with spacy | 59.01% | 98.00% | 38.99 |
| sentence transformers tensor with multilanguage vectors | 87.66% | 98.00% | 10.34 |
| sentence transformers tensor with ukrainian vectors | 92.74% | 98.00% | 5.26 |
| fine tuned similarity model | 85.86% | 98.00% | 12.14 |

---

### 9.
**a)** Мені потрібно трохи часу.

**b)** Дай мені ще кілька хвилин.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 47.06% | 95.00% | 47.94 |
| gestalt pattern matching from difflib | 27.45% | 95.00% | 67.55 |
| jaccard algorithm with stanza lematization | 32.00% | 95.00% | 63.00 |
| sklearn vectorizer | 12.74% | 95.00% | 82.26 |
| semantic similarity with spacy | 76.07% | 95.00% | 18.93 |
| sentence transformers tensor with multilanguage vectors | 76.08% | 95.00% | 18.92 |
| sentence transformers tensor with ukrainian vectors | 67.39% | 95.00% | 27.61 |
| fine tuned similarity model | 71.43% | 95.00% | 23.57 |

---

### 10.
**a)** Вона завжди приходить вчасно.

**b)** Вона ніколи не запізнюється.

| Algorithm | Similarity | Expected | Diff |
|-----------|------------|----------|------|
| gestalt pattern matching | 59.65% | 95.00% | 35.35 |
| gestalt pattern matching from difflib | 42.11% | 95.00% | 52.89 |
| jaccard algorithm with stanza lematization | 48.00% | 95.00% | 47.00 |
| sklearn vectorizer | 14.44% | 95.00% | 80.56 |
| semantic similarity with spacy | 79.71% | 95.00% | 15.29 |
| sentence transformers tensor with multilanguage vectors | 71.47% | 95.00% | 23.53 |
| sentence transformers tensor with ukrainian vectors | 74.53% | 95.00% | 20.47 |
| fine tuned similarity model | 70.42% | 95.00% | 24.58 |

---

