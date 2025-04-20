# similar, with certain differences
### 1.
**a)** Йшла мати в магазин по печиво.

**b)** Мама йшла до магазину за печивом.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 79.37% |
| gestalt pattern matching from difflib | 66.67% |
| jaccard algorithm with stanza lematization | 71.43% |
| sklearn vectorizer | 10.16% |
| semantic similarity with spacy | 69.28% |
| sentence transformers tensor with multilanguage vectors | 80.86% |
| sentence transformers tensor with ukrainian vectors | 97.65% |

---

### 2.
**a)** Кіт сидів на підвіконні й дивився у двір.

**b)** Кіт сидів на вікні та дивився у двір.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 89.74% |
| gestalt pattern matching from difflib | 89.74% |
| jaccard algorithm with stanza lematization | 83.33% |
| sklearn vectorizer | 63.28% |
| semantic similarity with spacy | 97.43% |
| sentence transformers tensor with multilanguage vectors | 91.91% |
| sentence transformers tensor with ukrainian vectors | 97.71% |

---

### 3.
**a)** Він узяв книжку зі столу.

**b)** Він взяв книгу зі столу.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 89.80% |
| gestalt pattern matching from difflib | 89.80% |
| jaccard algorithm with stanza lematization | 88.24% |
| sklearn vectorizer | 43.16% |
| semantic similarity with spacy | 98.87% |
| sentence transformers tensor with multilanguage vectors | 99.58% |
| sentence transformers tensor with ukrainian vectors | 99.58% |

---

### 4.
**a)** Машина швидко зникла за поворотом.

**b)** Автомобіль швидко зник за рогом.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 78.79% |
| gestalt pattern matching from difflib | 63.64% |
| jaccard algorithm with stanza lematization | 68.18% |
| sklearn vectorizer | 25.23% |
| semantic similarity with spacy | 92.04% |
| sentence transformers tensor with multilanguage vectors | 93.55% |
| sentence transformers tensor with ukrainian vectors | 96.84% |

---

### 5.
**a)** Сонце сідало за горизонт, фарбуючи небо.

**b)** Сонце заходило за обрій, забарвлюючи небо.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 82.93% |
| gestalt pattern matching from difflib | 68.29% |
| jaccard algorithm with stanza lematization | 69.23% |
| sklearn vectorizer | 33.61% |
| semantic similarity with spacy | 97.77% |
| sentence transformers tensor with multilanguage vectors | 95.91% |
| sentence transformers tensor with ukrainian vectors | 97.60% |

---

### 6.
**a)** Вона прокинулась від шуму на вулиці. Було ще темно.

**b)** Дівчина прокинулась через шум на вулиці. Надворі ще панувала темрява.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 76.67% |
| gestalt pattern matching from difflib | 66.67% |
| jaccard algorithm with stanza lematization | 75.86% |
| sklearn vectorizer | 26.97% |
| semantic similarity with spacy | 89.63% |
| sentence transformers tensor with multilanguage vectors | 91.40% |
| sentence transformers tensor with ukrainian vectors | 94.54% |

---

### 7.
**a)** Я поклав листа у конверт. Потім вкинув його до скриньки.

**b)** Я поклав лист у конверт. Потому вкинув його в поштову скриню.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 85.47% |
| gestalt pattern matching from difflib | 85.47% |
| jaccard algorithm with stanza lematization | 80.00% |
| sklearn vectorizer | 33.61% |
| semantic similarity with spacy | 92.70% |
| sentence transformers tensor with multilanguage vectors | 96.41% |
| sentence transformers tensor with ukrainian vectors | 96.20% |

---

### 8.
**a)** Дощ падав безупинно. Люди ховались під парасолями.

**b)** Злива лила без зупину. Люди ховалися під парасольками.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 82.69% |
| gestalt pattern matching from difflib | 75.00% |
| jaccard algorithm with stanza lematization | 85.19% |
| sklearn vectorizer | 15.59% |
| semantic similarity with spacy | 85.88% |
| sentence transformers tensor with multilanguage vectors | 71.42% |
| sentence transformers tensor with ukrainian vectors | 94.74% |

---

### 9.
**a)** Ми довго йшли через поле. Вітер свистів у вухах.

**b)** Ми довго бродили полем. У вухах свистів вітер.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 82.98% |
| gestalt pattern matching from difflib | 61.70% |
| jaccard algorithm with stanza lematization | 69.23% |
| sklearn vectorizer | 50.56% |
| semantic similarity with spacy | 93.29% |
| sentence transformers tensor with multilanguage vectors | 98.69% |
| sentence transformers tensor with ukrainian vectors | 95.97% |

---

### 10.
**a)** Я відкрив двері до кімнати. Всередині було темно. Я почув чийсь подих.

**b)** Я прочинив двері в кімнату. Там панувала темрява. І раптом я почув подих когось невидимого.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 74.53% |
| gestalt pattern matching from difflib | 53.42% |
| jaccard algorithm with stanza lematization | 75.86% |
| sklearn vectorizer | 16.87% |
| semantic similarity with spacy | 93.24% |
| sentence transformers tensor with multilanguage vectors | 91.92% |
| sentence transformers tensor with ukrainian vectors | 95.10% |

---

# completely different
### 1.
**a)** На кухні пахло свіжим хлібом.

**b)** Собака гавкав на місяць усю ніч.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 55.74% |
| gestalt pattern matching from difflib | 22.95% |
| jaccard algorithm with stanza lematization | 48.00% |
| sklearn vectorizer | 10.16% |
| semantic similarity with spacy | 62.27% |
| sentence transformers tensor with multilanguage vectors | 7.55% |
| sentence transformers tensor with ukrainian vectors | 17.96% |

---

### 2.
**a)** Вона закрила книжку й задумалась.

**b)** Поїзд щойно прибув на третій перон.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 44.12% |
| gestalt pattern matching from difflib | 23.53% |
| jaccard algorithm with stanza lematization | 40.74% |
| sklearn vectorizer | 0.00% |
| semantic similarity with spacy | 51.30% |
| sentence transformers tensor with multilanguage vectors | 10.62% |
| sentence transformers tensor with ukrainian vectors | 17.19% |

---

### 3.
**a)** Годинник пробив північ.

**b)** Яблуко впало прямо в калюжу.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 47.06% |
| gestalt pattern matching from difflib | 31.37% |
| jaccard algorithm with stanza lematization | 36.36% |
| sklearn vectorizer | 0.00% |
| semantic similarity with spacy | 60.91% |
| sentence transformers tensor with multilanguage vectors | 13.33% |
| sentence transformers tensor with ukrainian vectors | 33.37% |

---

### 4.
**a)** Він мріяв про політ у космос.

**b)** Чайник свистів на всю квартиру.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 50.00% |
| gestalt pattern matching from difflib | 23.33% |
| jaccard algorithm with stanza lematization | 47.62% |
| sklearn vectorizer | 0.00% |
| semantic similarity with spacy | 60.76% |
| sentence transformers tensor with multilanguage vectors | 16.04% |
| sentence transformers tensor with ukrainian vectors | 8.54% |

---

### 5.
**a)** Море гриміло, наче злий бог прокинувся.

**b)** Сусід знову свердлить о сьомій ранку.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 65.79% |
| gestalt pattern matching from difflib | 28.95% |
| jaccard algorithm with stanza lematization | 60.71% |
| sklearn vectorizer | 0.00% |
| semantic similarity with spacy | 50.48% |
| sentence transformers tensor with multilanguage vectors | 17.72% |
| sentence transformers tensor with ukrainian vectors | 40.94% |

---

### 6.
**a)** З полиці впала стара світлина.

**b)** Птах пролетів повз стару ялинку.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 67.74% |
| gestalt pattern matching from difflib | 45.16% |
| jaccard algorithm with stanza lematization | 59.09% |
| sklearn vectorizer | 0.00% |
| semantic similarity with spacy | 55.26% |
| sentence transformers tensor with multilanguage vectors | 33.08% |
| sentence transformers tensor with ukrainian vectors | 56.99% |

---

### 7.
**a)** Натиснувши кнопку, він зник у тумані.

**b)** Сміх дитини лунав серед натовпу.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 69.57% |
| gestalt pattern matching from difflib | 11.59% |
| jaccard algorithm with stanza lematization | 54.17% |
| sklearn vectorizer | 0.00% |
| semantic similarity with spacy | 58.56% |
| sentence transformers tensor with multilanguage vectors | 14.35% |
| sentence transformers tensor with ukrainian vectors | 35.67% |

---

### 8.
**a)** Вогонь тихо тріщав у каміні.

**b)** Годинник зупинився опівночі.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 50.00% |
| gestalt pattern matching from difflib | 21.43% |
| jaccard algorithm with stanza lematization | 36.00% |
| sklearn vectorizer | 0.00% |
| semantic similarity with spacy | 68.84% |
| sentence transformers tensor with multilanguage vectors | 19.79% |
| sentence transformers tensor with ukrainian vectors | 38.61% |

---

### 9.
**a)** Перо ковзало по папері впевнено й швидко.

**b)** Її пальці грали мелодію без нот.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 54.79% |
| gestalt pattern matching from difflib | 27.40% |
| jaccard algorithm with stanza lematization | 48.15% |
| sklearn vectorizer | 0.00% |
| semantic similarity with spacy | 55.91% |
| sentence transformers tensor with multilanguage vectors | 21.31% |
| sentence transformers tensor with ukrainian vectors | 35.34% |

---

### 10.
**a)** На вулиці загорілись ліхтарі.

**b)** Зірки спалахнули в нічному небі.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 62.30% |
| gestalt pattern matching from difflib | 26.23% |
| jaccard algorithm with stanza lematization | 46.15% |
| sklearn vectorizer | 0.00% |
| semantic similarity with spacy | 66.41% |
| sentence transformers tensor with multilanguage vectors | 46.92% |
| sentence transformers tensor with ukrainian vectors | 62.97% |

---

# different, but with a common meaning
### 1.
**a)** Він заснув під час фільму.

**b)** Поки йшло кіно, він задрімав.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 61.82% |
| gestalt pattern matching from difflib | 25.45% |
| jaccard algorithm with stanza lematization | 40.00% |
| sklearn vectorizer | 11.23% |
| semantic similarity with spacy | 65.53% |
| sentence transformers tensor with multilanguage vectors | 92.51% |
| sentence transformers tensor with ukrainian vectors | 91.35% |

---

### 2.
**a)** Я більше не хочу з тобою говорити.

**b)** Мені не цікаво продовжувати цю розмову.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 60.27% |
| gestalt pattern matching from difflib | 35.62% |
| jaccard algorithm with stanza lematization | 44.83% |
| sklearn vectorizer | 10.16% |
| semantic similarity with spacy | 75.34% |
| sentence transformers tensor with multilanguage vectors | 66.82% |
| sentence transformers tensor with ukrainian vectors | 75.98% |

---

### 3.
**a)** Ми запізнились на поїзд.

**b)** Поїзд поїхав без нас.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 62.22% |
| gestalt pattern matching from difflib | 31.11% |
| jaccard algorithm with stanza lematization | 50.00% |
| sklearn vectorizer | 14.44% |
| semantic similarity with spacy | 45.62% |
| sentence transformers tensor with multilanguage vectors | 70.42% |
| sentence transformers tensor with ukrainian vectors | 71.57% |

---

### 4.
**a)** Вона чудово співає.

**b)** У неї прекрасний голос.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 42.86% |
| gestalt pattern matching from difflib | 19.05% |
| jaccard algorithm with stanza lematization | 30.43% |
| sklearn vectorizer | 0.00% |
| semantic similarity with spacy | 60.90% |
| sentence transformers tensor with multilanguage vectors | 88.09% |
| sentence transformers tensor with ukrainian vectors | 92.48% |

---

### 5.
**a)** Діти гралися на майданчику.

**b)** Малеча бавилась на вулиці.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 60.38% |
| gestalt pattern matching from difflib | 37.74% |
| jaccard algorithm with stanza lematization | 40.00% |
| sklearn vectorizer | 14.44% |
| semantic similarity with spacy | 90.24% |
| sentence transformers tensor with multilanguage vectors | 44.34% |
| sentence transformers tensor with ukrainian vectors | 60.09% |

---

### 6.
**a)** Я не пам’ятаю його імені.

**b)** Його ім’я вилетіло в мене з голови.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 60.00% |
| gestalt pattern matching from difflib | 30.00% |
| jaccard algorithm with stanza lematization | 52.38% |
| sklearn vectorizer | 11.23% |
| semantic similarity with spacy | 60.39% |
| sentence transformers tensor with multilanguage vectors | 68.36% |
| sentence transformers tensor with ukrainian vectors | 70.96% |

---

### 7.
**a)** Він мешкає за кордоном.

**b)** Зараз він живе в іншій країні.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 52.83% |
| gestalt pattern matching from difflib | 37.74% |
| jaccard algorithm with stanza lematization | 47.62% |
| sklearn vectorizer | 12.74% |
| semantic similarity with spacy | 68.69% |
| sentence transformers tensor with multilanguage vectors | 73.89% |
| sentence transformers tensor with ukrainian vectors | 94.27% |

---

### 8.
**a)** Ця страва мені дуже подобається.

**b)** Я обожнюю цю їжу.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 40.82% |
| gestalt pattern matching from difflib | 16.33% |
| jaccard algorithm with stanza lematization | 28.00% |
| sklearn vectorizer | 0.00% |
| semantic similarity with spacy | 59.01% |
| sentence transformers tensor with multilanguage vectors | 87.66% |
| sentence transformers tensor with ukrainian vectors | 92.74% |

---

### 9.
**a)** Мені потрібно трохи часу.

**b)** Дай мені ще кілька хвилин.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 47.06% |
| gestalt pattern matching from difflib | 27.45% |
| jaccard algorithm with stanza lematization | 32.00% |
| sklearn vectorizer | 12.74% |
| semantic similarity with spacy | 76.07% |
| sentence transformers tensor with multilanguage vectors | 76.08% |
| sentence transformers tensor with ukrainian vectors | 67.39% |

---

### 10.
**a)** Вона завжди приходить вчасно.

**b)** Вона ніколи не запізнюється.

| Algorithm | Similarity |
|-----------|------------|
| gestalt pattern matching | 59.65% |
| gestalt pattern matching from difflib | 42.11% |
| jaccard algorithm with stanza lematization | 48.00% |
| sklearn vectorizer | 14.44% |
| semantic similarity with spacy | 79.71% |
| sentence transformers tensor with multilanguage vectors | 71.47% |
| sentence transformers tensor with ukrainian vectors | 74.53% |

---

