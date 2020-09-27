# GameOfLife

## About
  Реализация игры ["Жизнь"](https://ru.wikipedia.org/wiki/%D0%98%D0%B3%D1%80%D0%B0_%C2%AB%D0%96%D0%B8%D0%B7%D0%BD%D1%8C%C2%BB) Джона Конвэя

### Run the project

         python3 game.py --file file_name

Где file_name это путь к файлу, в котором содержатся начальные условия игры.
Вы репозитории представлены два примера: slider.txt и space.txt, можно использовать их либо создать свои стартовые условия.

### Creating initial conditions
  В каждую строку файла записываютcя координаты формата: 
  
         x y

  где x - номер столбца, а y - номер строки, а точка [x][y] клетка с жизнью.
  
### Arguments
  Пользователь может изменять аргументы поля:

         python3 game.py --file file_name --width 800 --height 600 --cell 9 --game_speed 5
        
  width - ширина игрового поля (в пикселях)
  height - высота игрового поля (в пикселях)
  сell - размер стороны клетки (в пикселях)
  game_speed - cкорость игры
   
