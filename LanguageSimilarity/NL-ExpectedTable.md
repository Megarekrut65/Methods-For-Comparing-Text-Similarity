
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
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
  </tr>
  <tr>
    <td><pre><code>Кіт сидів на підвіконні й дивився у двір.</code></pre><pre><code>Кіт сидів на вікні та дивився у двір.</code></pre></td>
    <td>99.00%</td>
    <td>99.00%</td>
    <td>99.00%</td>
    <td>99.00%</td>
    <td>99.00%</td>
    <td>99.00%</td>
    <td>99.00%</td>
    <td>99.00%</td>
  </tr>
  <tr>
    <td><pre><code>Він узяв книжку зі столу.</code></pre><pre><code>Він взяв книгу зі столу.</code></pre></td>
    <td>100.00%</td>
    <td>100.00%</td>
    <td>100.00%</td>
    <td>100.00%</td>
    <td>100.00%</td>
    <td>100.00%</td>
    <td>100.00%</td>
    <td>100.00%</td>
  </tr>
  <tr>
    <td><pre><code>Машина швидко зникла за поворотом.</code></pre><pre><code>Автомобіль швидко зник за рогом.</code></pre></td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
  </tr>
  <tr>
    <td><pre><code>Сонце сідало за горизонт, фарбуючи небо.</code></pre><pre><code>Сонце заходило за обрій, забарвлюючи небо.</code></pre></td>
    <td>93.00%</td>
    <td>93.00%</td>
    <td>93.00%</td>
    <td>93.00%</td>
    <td>93.00%</td>
    <td>93.00%</td>
    <td>93.00%</td>
    <td>93.00%</td>
  </tr>
  <tr>
    <td><pre><code>Вона прокинулась від шуму на вулиці. Було ще темно.</code></pre><pre><code>Дівчина прокинулась через шум на вулиці. Надворі ще панувала темрява.</code></pre></td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
  </tr>
  <tr>
    <td><pre><code>Я поклав листа у конверт. Потім вкинув його до скриньки.</code></pre><pre><code>Я поклав лист у конверт. Потому вкинув його в поштову скриню.</code></pre></td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
  </tr>
  <tr>
    <td><pre><code>Дощ падав безупинно. Люди ховались під парасолями.</code></pre><pre><code>Злива лила без зупину. Люди ховалися під парасольками.</code></pre></td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
  </tr>
  <tr>
    <td><pre><code>Ми довго йшли через поле. Вітер свистів у вухах.</code></pre><pre><code>Ми довго бродили полем. У вухах свистів вітер.</code></pre></td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
  </tr>
  <tr>
    <td><pre><code>Я відкрив двері до кімнати. Всередині було темно. Я почув чийсь подих.</code></pre><pre><code>Я прочинив двері в кімнату. Там панувала темрява. І раптом я почув подих.</code></pre></td>
    <td>93.00%</td>
    <td>93.00%</td>
    <td>93.00%</td>
    <td>93.00%</td>
    <td>93.00%</td>
    <td>93.00%</td>
    <td>93.00%</td>
    <td>93.00%</td>
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
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
  </tr>
  <tr>
    <td><pre><code>Вона закрила книжку й задумалась.</code></pre><pre><code>Поїзд щойно прибув на третій перон.</code></pre></td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
  </tr>
  <tr>
    <td><pre><code>Годинник пробив північ.</code></pre><pre><code>Яблуко впало прямо в калюжу.</code></pre></td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
  </tr>
  <tr>
    <td><pre><code>Він мріяв про політ у космос.</code></pre><pre><code>Чайник свистів на всю квартиру.</code></pre></td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
  </tr>
  <tr>
    <td><pre><code>Море гриміло, наче злий бог прокинувся.</code></pre><pre><code>Сусід знову свердлить о сьомій ранку.</code></pre></td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
  </tr>
  <tr>
    <td><pre><code>З полиці впала стара світлина.</code></pre><pre><code>Птах пролетів повз стару ялинку.</code></pre></td>
    <td>5.00%</td>
    <td>5.00%</td>
    <td>5.00%</td>
    <td>5.00%</td>
    <td>5.00%</td>
    <td>5.00%</td>
    <td>5.00%</td>
    <td>5.00%</td>
  </tr>
  <tr>
    <td><pre><code>Натиснувши кнопку, він зник у тумані.</code></pre><pre><code>Сміх дитини лунав серед натовпу.</code></pre></td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
  </tr>
  <tr>
    <td><pre><code>Вогонь тихо тріщав у каміні.</code></pre><pre><code>Годинник зупинився опівночі.</code></pre></td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
  </tr>
  <tr>
    <td><pre><code>Перо ковзало по папері впевнено й швидко.</code></pre><pre><code>Її пальці грали мелодію без нот.</code></pre></td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
    <td>0.00%</td>
  </tr>
  <tr>
    <td><pre><code>На вулиці загорілись ліхтарі.</code></pre><pre><code>Зірки спалахнули в нічному небі.</code></pre></td>
    <td>10.00%</td>
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
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
  </tr>
  <tr>
    <td><pre><code>Я більше не хочу з тобою говорити.</code></pre><pre><code>Мені не цікаво продовжувати цю розмову.</code></pre></td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
  </tr>
  <tr>
    <td><pre><code>Ми запізнились на поїзд.</code></pre><pre><code>Поїзд поїхав без нас.</code></pre></td>
    <td>85.00%</td>
    <td>85.00%</td>
    <td>85.00%</td>
    <td>85.00%</td>
    <td>85.00%</td>
    <td>85.00%</td>
    <td>85.00%</td>
    <td>85.00%</td>
  </tr>
  <tr>
    <td><pre><code>Вона чудово співає.</code></pre><pre><code>У неї прекрасний голос.</code></pre></td>
    <td>80.00%</td>
    <td>80.00%</td>
    <td>80.00%</td>
    <td>80.00%</td>
    <td>80.00%</td>
    <td>80.00%</td>
    <td>80.00%</td>
    <td>80.00%</td>
  </tr>
  <tr>
    <td><pre><code>Діти гралися на майданчику.</code></pre><pre><code>Малеча бавилась на вулиці.</code></pre></td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
    <td>90.00%</td>
  </tr>
  <tr>
    <td><pre><code>Я не пам’ятаю його імені.</code></pre><pre><code>Його ім’я вилетіло в мене з голови.</code></pre></td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
  </tr>
  <tr>
    <td><pre><code>Він мешкає за кордоном.</code></pre><pre><code>Зараз він живе в іншій країні.</code></pre></td>
    <td>96.00%</td>
    <td>96.00%</td>
    <td>96.00%</td>
    <td>96.00%</td>
    <td>96.00%</td>
    <td>96.00%</td>
    <td>96.00%</td>
    <td>96.00%</td>
  </tr>
  <tr>
    <td><pre><code>Ця страва мені дуже подобається.</code></pre><pre><code>Я обожнюю цю їжу.</code></pre></td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
    <td>98.00%</td>
  </tr>
  <tr>
    <td><pre><code>Мені потрібно трохи часу.</code></pre><pre><code>Дай мені ще кілька хвилин.</code></pre></td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
  </tr>
  <tr>
    <td><pre><code>Вона завжди приходить вчасно.</code></pre><pre><code>Вона ніколи не запізнюється.</code></pre></td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
    <td>95.00%</td>
  </tr>
</table>
