
**SIMILAR, WITH CERTAIN DIFFERENCES**

<table>
  <tr>
    <th>Text pairs</th>
    <th>gestalt pattern matching</th>
    <th>gestalt pattern matching from difflib</th>
    <th>jaccard algorithm with stanza lematization</th>
    <th>sklearn vectorizer</th>
    <th>semantic similarity with spacy</th>
    <th>sentence transformers tensor with multilanguage vectors</th>
    <th>sentence transformers tensor with ukrainian vectors</th>
    <th>fine tuned similarity model</th>
  </tr>
  <tr>
    <td><pre><code>Йшла мати в магазин по печиво.</code></pre><pre><code>Мама йшла до магазину за печивом.</code></pre></td>
    <td>79.37%</td>
    <td>66.67%</td>
    <td>71.43%</td>
    <td>10.16%</td>
    <td>69.28%</td>
    <td>80.86%</td>
    <td>97.65%</td>
    <td>81.53%</td>
  </tr>
  <tr>
    <td><pre><code>Кіт сидів на підвіконні й дивився у двір.</code></pre><pre><code>Кіт сидів на вікні та дивився у двір.</code></pre></td>
    <td>89.74%</td>
    <td>89.74%</td>
    <td>83.33%</td>
    <td>63.28%</td>
    <td>97.43%</td>
    <td>91.91%</td>
    <td>97.71%</td>
    <td>90.71%</td>
  </tr>
  <tr>
    <td><pre><code>Він узяв книжку зі столу.</code></pre><pre><code>Він взяв книгу зі столу.</code></pre></td>
    <td>89.80%</td>
    <td>89.80%</td>
    <td>88.24%</td>
    <td>43.16%</td>
    <td>98.87%</td>
    <td>99.58%</td>
    <td>99.58%</td>
    <td>99.11%</td>
  </tr>
  <tr>
    <td><pre><code>Машина швидко зникла за поворотом.</code></pre><pre><code>Автомобіль швидко зник за рогом.</code></pre></td>
    <td>78.79%</td>
    <td>63.64%</td>
    <td>68.18%</td>
    <td>25.23%</td>
    <td>92.04%</td>
    <td>93.55%</td>
    <td>96.84%</td>
    <td>83.42%</td>
  </tr>
  <tr>
    <td><pre><code>Сонце сідало за горизонт, фарбуючи небо.</code></pre><pre><code>Сонце заходило за обрій, забарвлюючи небо.</code></pre></td>
    <td>82.93%</td>
    <td>68.29%</td>
    <td>69.23%</td>
    <td>33.61%</td>
    <td>97.77%</td>
    <td>95.91%</td>
    <td>97.60%</td>
    <td>91.42%</td>
  </tr>
  <tr>
    <td><pre><code>Вона прокинулась від шуму на вулиці. Було ще темно.</code></pre><pre><code>Дівчина прокинулась через шум на вулиці. Надворі ще панувала темрява.</code></pre></td>
    <td>76.67%</td>
    <td>66.67%</td>
    <td>75.86%</td>
    <td>26.97%</td>
    <td>89.63%</td>
    <td>91.40%</td>
    <td>94.54%</td>
    <td>88.51%</td>
  </tr>
  <tr>
    <td><pre><code>Я поклав листа у конверт. Потім вкинув його до скриньки.</code></pre><pre><code>Я поклав лист у конверт. Потому вкинув його в поштову скриню.</code></pre></td>
    <td>85.47%</td>
    <td>85.47%</td>
    <td>80.00%</td>
    <td>33.61%</td>
    <td>92.70%</td>
    <td>96.41%</td>
    <td>96.20%</td>
    <td>93.95%</td>
  </tr>
  <tr>
    <td><pre><code>Дощ падав безупинно. Люди ховались під парасолями.</code></pre><pre><code>Злива лила без зупину. Люди ховалися під парасольками.</code></pre></td>
    <td>82.69%</td>
    <td>75.00%</td>
    <td>85.19%</td>
    <td>15.59%</td>
    <td>85.88%</td>
    <td>71.42%</td>
    <td>94.74%</td>
    <td>59.82%</td>
  </tr>
  <tr>
    <td><pre><code>Ми довго йшли через поле. Вітер свистів у вухах.</code></pre><pre><code>Ми довго бродили полем. У вухах свистів вітер.</code></pre></td>
    <td>82.98%</td>
    <td>61.70%</td>
    <td>69.23%</td>
    <td>50.56%</td>
    <td>93.29%</td>
    <td>98.69%</td>
    <td>95.97%</td>
    <td>98.53%</td>
  </tr>
  <tr>
    <td><pre><code>Я відкрив двері до кімнати. Всередині було темно. Я почув чийсь подих.</code></pre><pre><code>Я прочинив двері в кімнату. Там панувала темрява. І раптом я почув подих.</code></pre></td>
    <td>72.73%</td>
    <td>60.14%</td>
    <td>71.43%</td>
    <td>18.98%</td>
    <td>93.22%</td>
    <td>96.15%</td>
    <td>95.78%</td>
    <td>92.07%</td>
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
    <th>sentence transformers tensor with multilanguage vectors</th>
    <th>sentence transformers tensor with ukrainian vectors</th>
    <th>fine tuned similarity model</th>
  </tr>
  <tr>
    <td><pre><code>На кухні пахло свіжим хлібом.</code></pre><pre><code>Собака гавкав на місяць усю ніч.</code></pre></td>
    <td>55.74%</td>
    <td>22.95%</td>
    <td>48.00%</td>
    <td>10.16%</td>
    <td>62.27%</td>
    <td>7.55%</td>
    <td>17.96%</td>
    <td>1.44%</td>
  </tr>
  <tr>
    <td><pre><code>Вона закрила книжку й задумалась.</code></pre><pre><code>Поїзд щойно прибув на третій перон.</code></pre></td>
    <td>44.12%</td>
    <td>23.53%</td>
    <td>40.74%</td>
    <td>0.00%</td>
    <td>51.30%</td>
    <td>10.62%</td>
    <td>17.19%</td>
    <td>5.24%</td>
  </tr>
  <tr>
    <td><pre><code>Годинник пробив північ.</code></pre><pre><code>Яблуко впало прямо в калюжу.</code></pre></td>
    <td>47.06%</td>
    <td>31.37%</td>
    <td>36.36%</td>
    <td>0.00%</td>
    <td>60.91%</td>
    <td>13.33%</td>
    <td>33.37%</td>
    <td>8.34%</td>
  </tr>
  <tr>
    <td><pre><code>Він мріяв про політ у космос.</code></pre><pre><code>Чайник свистів на всю квартиру.</code></pre></td>
    <td>50.00%</td>
    <td>23.33%</td>
    <td>47.62%</td>
    <td>0.00%</td>
    <td>60.76%</td>
    <td>16.04%</td>
    <td>8.54%</td>
    <td>5.50%</td>
  </tr>
  <tr>
    <td><pre><code>Море гриміло, наче злий бог прокинувся.</code></pre><pre><code>Сусід знову свердлить о сьомій ранку.</code></pre></td>
    <td>65.79%</td>
    <td>28.95%</td>
    <td>60.71%</td>
    <td>0.00%</td>
    <td>50.48%</td>
    <td>17.72%</td>
    <td>40.94%</td>
    <td>4.46%</td>
  </tr>
  <tr>
    <td><pre><code>З полиці впала стара світлина.</code></pre><pre><code>Птах пролетів повз стару ялинку.</code></pre></td>
    <td>67.74%</td>
    <td>45.16%</td>
    <td>59.09%</td>
    <td>0.00%</td>
    <td>55.26%</td>
    <td>33.08%</td>
    <td>56.99%</td>
    <td>27.30%</td>
  </tr>
  <tr>
    <td><pre><code>Натиснувши кнопку, він зник у тумані.</code></pre><pre><code>Сміх дитини лунав серед натовпу.</code></pre></td>
    <td>69.57%</td>
    <td>11.59%</td>
    <td>54.17%</td>
    <td>0.00%</td>
    <td>58.56%</td>
    <td>14.35%</td>
    <td>35.67%</td>
    <td>6.70%</td>
  </tr>
  <tr>
    <td><pre><code>Вогонь тихо тріщав у каміні.</code></pre><pre><code>Годинник зупинився опівночі.</code></pre></td>
    <td>50.00%</td>
    <td>21.43%</td>
    <td>36.00%</td>
    <td>0.00%</td>
    <td>68.84%</td>
    <td>19.79%</td>
    <td>38.61%</td>
    <td>3.00%</td>
  </tr>
  <tr>
    <td><pre><code>Перо ковзало по папері впевнено й швидко.</code></pre><pre><code>Її пальці грали мелодію без нот.</code></pre></td>
    <td>54.79%</td>
    <td>27.40%</td>
    <td>48.15%</td>
    <td>0.00%</td>
    <td>55.91%</td>
    <td>21.31%</td>
    <td>35.34%</td>
    <td>13.76%</td>
  </tr>
  <tr>
    <td><pre><code>На вулиці загорілись ліхтарі.</code></pre><pre><code>Зірки спалахнули в нічному небі.</code></pre></td>
    <td>62.30%</td>
    <td>26.23%</td>
    <td>46.15%</td>
    <td>0.00%</td>
    <td>66.41%</td>
    <td>46.92%</td>
    <td>62.97%</td>
    <td>43.06%</td>
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
    <th>sentence transformers tensor with multilanguage vectors</th>
    <th>sentence transformers tensor with ukrainian vectors</th>
    <th>fine tuned similarity model</th>
  </tr>
  <tr>
    <td><pre><code>Він заснув під час фільму.</code></pre><pre><code>Поки йшло кіно, він задрімав.</code></pre></td>
    <td>61.82%</td>
    <td>25.45%</td>
    <td>40.00%</td>
    <td>11.23%</td>
    <td>65.53%</td>
    <td>92.51%</td>
    <td>91.35%</td>
    <td>91.28%</td>
  </tr>
  <tr>
    <td><pre><code>Я більше не хочу з тобою говорити.</code></pre><pre><code>Мені не цікаво продовжувати цю розмову.</code></pre></td>
    <td>60.27%</td>
    <td>35.62%</td>
    <td>44.83%</td>
    <td>10.16%</td>
    <td>75.34%</td>
    <td>66.82%</td>
    <td>75.98%</td>
    <td>61.17%</td>
  </tr>
  <tr>
    <td><pre><code>Ми запізнились на поїзд.</code></pre><pre><code>Поїзд поїхав без нас.</code></pre></td>
    <td>62.22%</td>
    <td>31.11%</td>
    <td>50.00%</td>
    <td>14.44%</td>
    <td>45.62%</td>
    <td>70.42%</td>
    <td>71.57%</td>
    <td>59.10%</td>
  </tr>
  <tr>
    <td><pre><code>Вона чудово співає.</code></pre><pre><code>У неї прекрасний голос.</code></pre></td>
    <td>42.86%</td>
    <td>19.05%</td>
    <td>30.43%</td>
    <td>0.00%</td>
    <td>60.90%</td>
    <td>88.09%</td>
    <td>92.48%</td>
    <td>85.74%</td>
  </tr>
  <tr>
    <td><pre><code>Діти гралися на майданчику.</code></pre><pre><code>Малеча бавилась на вулиці.</code></pre></td>
    <td>60.38%</td>
    <td>37.74%</td>
    <td>40.00%</td>
    <td>14.44%</td>
    <td>90.24%</td>
    <td>44.34%</td>
    <td>60.09%</td>
    <td>39.46%</td>
  </tr>
  <tr>
    <td><pre><code>Я не пам’ятаю його імені.</code></pre><pre><code>Його ім’я вилетіло в мене з голови.</code></pre></td>
    <td>60.00%</td>
    <td>30.00%</td>
    <td>52.38%</td>
    <td>11.23%</td>
    <td>60.39%</td>
    <td>68.36%</td>
    <td>70.96%</td>
    <td>64.43%</td>
  </tr>
  <tr>
    <td><pre><code>Він мешкає за кордоном.</code></pre><pre><code>Зараз він живе в іншій країні.</code></pre></td>
    <td>52.83%</td>
    <td>37.74%</td>
    <td>47.62%</td>
    <td>12.74%</td>
    <td>68.69%</td>
    <td>73.89%</td>
    <td>94.27%</td>
    <td>69.16%</td>
  </tr>
  <tr>
    <td><pre><code>Ця страва мені дуже подобається.</code></pre><pre><code>Я обожнюю цю їжу.</code></pre></td>
    <td>40.82%</td>
    <td>16.33%</td>
    <td>28.00%</td>
    <td>0.00%</td>
    <td>59.01%</td>
    <td>87.66%</td>
    <td>92.74%</td>
    <td>85.86%</td>
  </tr>
  <tr>
    <td><pre><code>Мені потрібно трохи часу.</code></pre><pre><code>Дай мені ще кілька хвилин.</code></pre></td>
    <td>47.06%</td>
    <td>27.45%</td>
    <td>32.00%</td>
    <td>12.74%</td>
    <td>76.07%</td>
    <td>76.08%</td>
    <td>67.39%</td>
    <td>71.43%</td>
  </tr>
  <tr>
    <td><pre><code>Вона завжди приходить вчасно.</code></pre><pre><code>Вона ніколи не запізнюється.</code></pre></td>
    <td>59.65%</td>
    <td>42.11%</td>
    <td>48.00%</td>
    <td>14.44%</td>
    <td>79.71%</td>
    <td>71.47%</td>
    <td>74.53%</td>
    <td>70.42%</td>
  </tr>
</table>
