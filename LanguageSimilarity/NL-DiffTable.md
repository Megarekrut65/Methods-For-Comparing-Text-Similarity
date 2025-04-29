
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
    <td>18.63</td>
    <td>31.33</td>
    <td>26.57</td>
    <td>87.84</td>
    <td>28.72</td>
    <td>17.14</td>
    <td>0.35</td>
    <td>16.47</td>
  </tr>
  <tr>
    <td><pre><code>Кіт сидів на підвіконні й дивився у двір.</code></pre><pre><code>Кіт сидів на вікні та дивився у двір.</code></pre></td>
    <td>9.26</td>
    <td>9.26</td>
    <td>15.67</td>
    <td>35.72</td>
    <td>1.57</td>
    <td>7.09</td>
    <td>1.29</td>
    <td>8.29</td>
  </tr>
  <tr>
    <td><pre><code>Він узяв книжку зі столу.</code></pre><pre><code>Він взяв книгу зі столу.</code></pre></td>
    <td>10.20</td>
    <td>10.20</td>
    <td>11.76</td>
    <td>56.84</td>
    <td>1.13</td>
    <td>0.42</td>
    <td>0.42</td>
    <td>0.89</td>
  </tr>
  <tr>
    <td><pre><code>Машина швидко зникла за поворотом.</code></pre><pre><code>Автомобіль швидко зник за рогом.</code></pre></td>
    <td>16.21</td>
    <td>31.36</td>
    <td>26.82</td>
    <td>69.77</td>
    <td>2.96</td>
    <td>1.45</td>
    <td>1.84</td>
    <td>11.58</td>
  </tr>
  <tr>
    <td><pre><code>Сонце сідало за горизонт, фарбуючи небо.</code></pre><pre><code>Сонце заходило за обрій, забарвлюючи небо.</code></pre></td>
    <td>10.07</td>
    <td>24.71</td>
    <td>23.77</td>
    <td>59.39</td>
    <td>4.77</td>
    <td>2.91</td>
    <td>4.60</td>
    <td>1.58</td>
  </tr>
  <tr>
    <td><pre><code>Вона прокинулась від шуму на вулиці. Було ще темно.</code></pre><pre><code>Дівчина прокинулась через шум на вулиці. Надворі ще панувала темрява.</code></pre></td>
    <td>13.33</td>
    <td>23.33</td>
    <td>14.14</td>
    <td>63.03</td>
    <td>0.37</td>
    <td>1.40</td>
    <td>4.54</td>
    <td>1.49</td>
  </tr>
  <tr>
    <td><pre><code>Я поклав листа у конверт. Потім вкинув його до скриньки.</code></pre><pre><code>Я поклав лист у конверт. Потому вкинув його в поштову скриню.</code></pre></td>
    <td>12.53</td>
    <td>12.53</td>
    <td>18.00</td>
    <td>64.39</td>
    <td>5.30</td>
    <td>1.59</td>
    <td>1.80</td>
    <td>4.05</td>
  </tr>
  <tr>
    <td><pre><code>Дощ падав безупинно. Люди ховались під парасолями.</code></pre><pre><code>Злива лила без зупину. Люди ховалися під парасольками.</code></pre></td>
    <td>12.31</td>
    <td>20.00</td>
    <td>9.81</td>
    <td>79.41</td>
    <td>9.12</td>
    <td>23.58</td>
    <td>0.26</td>
    <td>35.18</td>
  </tr>
  <tr>
    <td><pre><code>Ми довго йшли через поле. Вітер свистів у вухах.</code></pre><pre><code>Ми довго бродили полем. У вухах свистів вітер.</code></pre></td>
    <td>15.02</td>
    <td>36.30</td>
    <td>28.77</td>
    <td>47.44</td>
    <td>4.71</td>
    <td>0.69</td>
    <td>2.03</td>
    <td>0.53</td>
  </tr>
  <tr>
    <td><pre><code>Я відкрив двері до кімнати. Всередині було темно. Я почув чийсь подих.</code></pre><pre><code>Я прочинив двері в кімнату. Там панувала темрява. І раптом я почув подих.</code></pre></td>
    <td>20.27</td>
    <td>32.86</td>
    <td>21.57</td>
    <td>74.02</td>
    <td>0.22</td>
    <td>3.15</td>
    <td>2.78</td>
    <td>0.93</td>
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
    <td>55.74</td>
    <td>22.95</td>
    <td>48.00</td>
    <td>10.16</td>
    <td>62.27</td>
    <td>7.55</td>
    <td>17.96</td>
    <td>1.44</td>
  </tr>
  <tr>
    <td><pre><code>Вона закрила книжку й задумалась.</code></pre><pre><code>Поїзд щойно прибув на третій перон.</code></pre></td>
    <td>44.12</td>
    <td>23.53</td>
    <td>40.74</td>
    <td>0.00</td>
    <td>51.30</td>
    <td>10.62</td>
    <td>17.19</td>
    <td>5.24</td>
  </tr>
  <tr>
    <td><pre><code>Годинник пробив північ.</code></pre><pre><code>Яблуко впало прямо в калюжу.</code></pre></td>
    <td>47.06</td>
    <td>31.37</td>
    <td>36.36</td>
    <td>0.00</td>
    <td>60.91</td>
    <td>13.33</td>
    <td>33.37</td>
    <td>8.34</td>
  </tr>
  <tr>
    <td><pre><code>Він мріяв про політ у космос.</code></pre><pre><code>Чайник свистів на всю квартиру.</code></pre></td>
    <td>50.00</td>
    <td>23.33</td>
    <td>47.62</td>
    <td>0.00</td>
    <td>60.76</td>
    <td>16.04</td>
    <td>8.54</td>
    <td>5.50</td>
  </tr>
  <tr>
    <td><pre><code>Море гриміло, наче злий бог прокинувся.</code></pre><pre><code>Сусід знову свердлить о сьомій ранку.</code></pre></td>
    <td>65.79</td>
    <td>28.95</td>
    <td>60.71</td>
    <td>0.00</td>
    <td>50.48</td>
    <td>17.72</td>
    <td>40.94</td>
    <td>4.46</td>
  </tr>
  <tr>
    <td><pre><code>З полиці впала стара світлина.</code></pre><pre><code>Птах пролетів повз стару ялинку.</code></pre></td>
    <td>62.74</td>
    <td>40.16</td>
    <td>54.09</td>
    <td>5.00</td>
    <td>50.26</td>
    <td>28.08</td>
    <td>51.99</td>
    <td>22.30</td>
  </tr>
  <tr>
    <td><pre><code>Натиснувши кнопку, він зник у тумані.</code></pre><pre><code>Сміх дитини лунав серед натовпу.</code></pre></td>
    <td>69.57</td>
    <td>11.59</td>
    <td>54.17</td>
    <td>0.00</td>
    <td>58.56</td>
    <td>14.35</td>
    <td>35.67</td>
    <td>6.70</td>
  </tr>
  <tr>
    <td><pre><code>Вогонь тихо тріщав у каміні.</code></pre><pre><code>Годинник зупинився опівночі.</code></pre></td>
    <td>50.00</td>
    <td>21.43</td>
    <td>36.00</td>
    <td>0.00</td>
    <td>68.84</td>
    <td>19.79</td>
    <td>38.61</td>
    <td>3.00</td>
  </tr>
  <tr>
    <td><pre><code>Перо ковзало по папері впевнено й швидко.</code></pre><pre><code>Її пальці грали мелодію без нот.</code></pre></td>
    <td>54.79</td>
    <td>27.40</td>
    <td>48.15</td>
    <td>0.00</td>
    <td>55.91</td>
    <td>21.31</td>
    <td>35.34</td>
    <td>13.76</td>
  </tr>
  <tr>
    <td><pre><code>На вулиці загорілись ліхтарі.</code></pre><pre><code>Зірки спалахнули в нічному небі.</code></pre></td>
    <td>52.30</td>
    <td>16.23</td>
    <td>36.15</td>
    <td>10.00</td>
    <td>56.41</td>
    <td>36.92</td>
    <td>52.97</td>
    <td>33.06</td>
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
    <td>28.18</td>
    <td>64.55</td>
    <td>50.00</td>
    <td>78.77</td>
    <td>24.47</td>
    <td>2.51</td>
    <td>1.35</td>
    <td>1.28</td>
  </tr>
  <tr>
    <td><pre><code>Я більше не хочу з тобою говорити.</code></pre><pre><code>Мені не цікаво продовжувати цю розмову.</code></pre></td>
    <td>29.73</td>
    <td>54.38</td>
    <td>45.17</td>
    <td>79.84</td>
    <td>14.66</td>
    <td>23.18</td>
    <td>14.02</td>
    <td>28.83</td>
  </tr>
  <tr>
    <td><pre><code>Ми запізнились на поїзд.</code></pre><pre><code>Поїзд поїхав без нас.</code></pre></td>
    <td>22.78</td>
    <td>53.89</td>
    <td>35.00</td>
    <td>70.56</td>
    <td>39.38</td>
    <td>14.58</td>
    <td>13.43</td>
    <td>25.90</td>
  </tr>
  <tr>
    <td><pre><code>Вона чудово співає.</code></pre><pre><code>У неї прекрасний голос.</code></pre></td>
    <td>37.14</td>
    <td>60.95</td>
    <td>49.57</td>
    <td>80.00</td>
    <td>19.10</td>
    <td>8.09</td>
    <td>12.48</td>
    <td>5.74</td>
  </tr>
  <tr>
    <td><pre><code>Діти гралися на майданчику.</code></pre><pre><code>Малеча бавилась на вулиці.</code></pre></td>
    <td>29.62</td>
    <td>52.26</td>
    <td>50.00</td>
    <td>75.56</td>
    <td>0.24</td>
    <td>45.66</td>
    <td>29.91</td>
    <td>50.54</td>
  </tr>
  <tr>
    <td><pre><code>Я не пам’ятаю його імені.</code></pre><pre><code>Його ім’я вилетіло в мене з голови.</code></pre></td>
    <td>35.00</td>
    <td>65.00</td>
    <td>42.62</td>
    <td>83.77</td>
    <td>34.61</td>
    <td>26.64</td>
    <td>24.04</td>
    <td>30.57</td>
  </tr>
  <tr>
    <td><pre><code>Він мешкає за кордоном.</code></pre><pre><code>Зараз він живе в іншій країні.</code></pre></td>
    <td>43.17</td>
    <td>58.26</td>
    <td>48.38</td>
    <td>83.26</td>
    <td>27.31</td>
    <td>22.11</td>
    <td>1.73</td>
    <td>26.84</td>
  </tr>
  <tr>
    <td><pre><code>Ця страва мені дуже подобається.</code></pre><pre><code>Я обожнюю цю їжу.</code></pre></td>
    <td>57.18</td>
    <td>81.67</td>
    <td>70.00</td>
    <td>98.00</td>
    <td>38.99</td>
    <td>10.34</td>
    <td>5.26</td>
    <td>12.14</td>
  </tr>
  <tr>
    <td><pre><code>Мені потрібно трохи часу.</code></pre><pre><code>Дай мені ще кілька хвилин.</code></pre></td>
    <td>47.94</td>
    <td>67.55</td>
    <td>63.00</td>
    <td>82.26</td>
    <td>18.93</td>
    <td>18.92</td>
    <td>27.61</td>
    <td>23.57</td>
  </tr>
  <tr>
    <td><pre><code>Вона завжди приходить вчасно.</code></pre><pre><code>Вона ніколи не запізнюється.</code></pre></td>
    <td>35.35</td>
    <td>52.89</td>
    <td>47.00</td>
    <td>80.56</td>
    <td>15.29</td>
    <td>23.53</td>
    <td>20.47</td>
    <td>24.58</td>
  </tr>
</table>
