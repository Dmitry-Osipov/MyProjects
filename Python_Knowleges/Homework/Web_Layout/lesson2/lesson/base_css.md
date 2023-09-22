# Единицы измерения CSS:
Относительные:
- px – пиксель;
- % – проценты;
- em – высота текущего шрифта;
- и т.д.

Абсолютные:
- cm – сантиметр;
- mm – миллиметр;
- in – дюйм;
- pt – пункт;
- и т.д.


Именованные;

Функциональные RGB;

Шестнадцатеричные RGB.

# width, height - ширина и высота:
h1 {

    width: 300px;
    height: 200px;
}

# background - фон элемента:
- background-color: #ff0;
- background-image: url(img/foto.jpg);
- background-position: top; (bottom | left | right);
- background-repeat: repeat-x; (repeat-y |
no-repeat);
- background-size: cover; (contain | 100%).
- Объединённое значение: background: #ff0 url(img/foto.jpg) top repeat-x;
(любое из свойств может отсутствовать)

# border - рамка:
1. border-color: red; (#f00 |
RGB(255, 0, 0));
2. border-style: solid; (dotted |
dashed | groove | ridge | solid
| double | inset | outset);
3. border-width: 2px.

# border-width - толщина рамки:
1. (1px 2px) – 1px: верхняя и
нижняя, 2px: левая и
правая;
2. (1px 2px 3px) – 1px:
верхняя, 2px: левая и
правая, 3 нижняя;
3. (1px 2px 3px 4px) – 1px:
верхняя, 2px: правая, 3px:
нижняя, 4px: левая.

# Добавление рамки:
Для создания рамки вокруг текста, изображения или блока используется
объединенное свойство:

h1 {

    border: 1px solid black;
}

# color - цвет текста:
- color: red; 
- color: #78fa2e;
- color: RGB(34, 21, 56);

# font - шрифт текста:
- font-family: "Times New Roman", serif, Verdana;
- serif – шрифты с засечками;
- sans-serif – рублённые шрифты, без засечек;
- cursive – курсивные шрифты;
- fantasy – декоративные шрифты;
- monospace – моноширные шрифты.

1. font-style: italic; (oblique | normal | bold);
2. font-variant: small-caps; 
3. font-weight: bold; (bolder | lighter | 100 | 200);
4. font-size: 20px; (small | medium | large);

# list-style – вид маркера:
1. list-style-type: circle; (disc | square | armenian | decimal);
2. list-style-position: inside | outside;
3. list-style-image: url(img/list.png).

# Редактирование текста:
- text-align: center; (justify | left | right);
- text-decoration: none; (line-through | overline | underline | none);
- text-transform: capitalize; (lowercase | uppercase).

# Наследование и группирование:
Не все свойства CSS наследуются. Например, ссылка не наследуется, надо прописать:

p {
    
    font-size: 18px;
    color: red;
}
    p a {

        color: inherit;
}

Пример группирования:

h1, h3, p {

    text-align: center;
    color: blue;
}
        h1 {

        font-family: Verdana;
}
        h3 {

        font-family: Arial;
}
        p {

        font-size: 12px;
}

# Приоритеты:
CSS-свойство получает максимальный приоритет в каскаде стилей при добавлении !important.

h1 {
    
    color: black !important;
}
    h1 {

    color: green;
}

Стиль в теге style в HTML имеет приоритет над файлом CSS.

Приоритеты применения стилей:
1. уровень приоритета селекторов;
2. стили, заданные в разделе head;
3. стили во внешних файлах;
4. наследуемые стили от предков.