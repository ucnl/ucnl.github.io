---
layout: post
title: Мюоны не помогут
---

### Приветствую вас, глубокоуважаемые!

> Всратосфера - одно из мест, где рождаются мюоны

## Preface

Третьего дня (С) попалась на глаза такая новость [Разработан подземный «GPS»: он работает на основе мюонов космических лучей](https://hightech.fm/2023/06/15/underground-navigation). В том смысле что все, все пропало, вы с вашим [подводным GPS](https://docs.unavlab.com/navigation_and_tracking_systems_ru.html#redwave) больше не нужны, тут вот мюоны из всратосферы пронзают толщи и по ним теперь и будут определять координаты под водой.

Тут, кстати, интересный момент: когда читаешь новости, с твоей профессиональной сферой никак не связанные, они кажутся вполне нормальными (если в наше время к новостям вообще можно применить такое прилагательное). Но иногда, редко-редко, попадается что-то знакомое. И если убрать эмоции, то остается только концентрированный испанский стыд.

Статья японских авторов, на основе которой hightech.fm выпустили новость, доступна, например, на [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2589004223010775). 

Для начала давайте проследим эрозию заголовков. В оригинале статья называется:  

**First navigation with wireless muometric navigation system (MuWNS) in indoor and underground environments**, что можно перевести как **Первые опыты навигации при помощи беспроводной _мюометрической_ навигационной системы (MuWNS) под землей и внутри помещений**

Я не специалист по ядерной физике и не ручаюсь за точность термина _мюометрический_, может быть, правильнее сказать _мюонометричсеский_. Но я кое-что знаю про навигацию и навигационные системы.

Заголовок новости у hightech.fm звучит чуть менее конкретно, как бы усыпляя наше внимание: 

**Исследование подтвердило возможность создания системы для навигации под землей на основе сверхбыстрых частиц космических лучей.**

А крупный заголовок в самом верху звучит куда более желто:

**Разработан подземный «GPS»: он работает на основе мюонов космических лучей**

Предыстория понятна, теперь, как говорил классик:

## Давайте разбираться

Про мюоны нам нужно знать самый минимум неоспоримых фактов:

- Они существуют
- Летят на околосветовых скоростях
- Слабо взаимодействуют с веществом и могут проходить километры горной породы (до 2 км) или толщу океанской воды (до 8.5 км)
- Их можно детектировать
- Условно, поток мюонов составляет тысячи частиц на квадратный метр поверхности в минуту

Работает, описанная в японской статье система, следующим образом:

Есть референсные детекторы и есть детектор на навигационном приемнике. Мюон пролетает через один из референсных детекторов, положение которого известно. 
Это событие фиксируется, то есть в некий момент времени частица попала в детектор. 

С некоторой ненулевой вероятностью этот же самый мюон попадает в детектор, расположенный на навигационном приемнике. Это событие так же фиксируется, то есть, опять определяется момент времени.

А теперь внимание: **если** часы референсного детектора, по которым он фиксирует событие, и часы на навигационном приемнике синхронизированы, то у нас получается измеренная дальность между референсным детектором и детектором на навигационном приемнике. Три таких измерения (выполненные с разными референсными детекторами, а следовательно, с разными мюонами) позволяют рассчитать положение в трехмерном пространстве. Мы принимаем, что скорость мюона ядерщики знают или умеют хорошо измерять.

Обеспечить точную синхронизацию часов детекторов и навигационного приёмника с требуемой точностью на какое-то время (десятки минут или часы или даже дни) в принципе возможно.

**Но.**  

_"Всегда ведь есть какое-то "но", правда?" (С)_

Чтобы _рассчитать_ положение навигационного приемника, вам **в одном месте** нужны и **времена детектирования** частиц на **референсных детекторах**, и времена детектирования частиц на **навигационном приемнике**. 

Иными словами, в зависимости от того, где вы хотите получить координату, вам нужно будет куда-то передать информацию: или с референсных детекторов на навигационный приемник, или наоборот.

Ну, или если вас устроит разбор полетов пост-фактум, навигационный приемник может сохранить все события, вернуться, и потом можно будет построить траекторию его движения.

## В **сухом** остатке

Авторы статьи сразу явно указали, где такой способ может использоваться: например, в помещении, где всюду есть WiFi или что-то со схожим функционалом. 
Можно ли WiFi-ем оборудовать пещеру? Ну, думается что да.

Можно для подводных целей использовать этот способ? Если обеспечить связь через кабель - тоже да. 

Похоже ли это хоть сколько на GPS? Нет. И то и другое - навигационная система, и только это у них общее. В остальном - нет. 

В реальности же там целая уйма проблем разной степени сложности: и площади детекторов (в статье это ~1 м<sup>2</sup>, и малая вероятность попадания одного мюона в один из референсных детекторов и в детектор навигационного приемника, и высокая вероятность ложных срабатываний (как быть уверенным что это именно тот мюон?) и сложность длительного хранения синхронизации часов и прочее, и прочее и прочее.

На этом разрешите откланяться,

Ваш, до **глубины** души,  
[@AlekUnderwater](https://github.com/AlekUnderwater)



