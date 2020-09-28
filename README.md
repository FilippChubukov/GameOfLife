# GameOfLife

## About
  implementation of the game ["Life"](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

### Run the project

         python3 game.py --file file_name

file_name is the path to the file containing the initial game data.
the repository contain two examples: slider.txt and space.txt. You can use them or create your own.

### Creating initial data
  The coordinates of the cell with life are recorded in each line of the file: 
  
         x y

  x - column number, y - line number
  
### Arguments
  User can change field settings:

         python3 game.py --file file_name --width 800 --height 600 --cell 9 --game_speed 5
        
  width - width of the playing field
  
  height - height of the playing field
  
  сell - size of the cell
  
  game_speed - speed of the game
  
### Requirements
* python 3
* pygame

## Contributors

* Chubukov Filipp  
