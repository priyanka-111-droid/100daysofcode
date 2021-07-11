# Making changes to Snake Game

We want our snake game to keep track of highscores and continue instead of displaying GAME OVER.

**In scoreboard.py,**

1.Add attribute high_score and set it to 0.

2.Instead of method game_over(),define new method reset where if high score is more than score,value of high score is updated to score.Now set score to 0.

3.Small change,it makes more sense if we put self.clear() in the update_scoreboard() method just before self.write() INSTEAD of using self.clear() in increase_score() method.

4.In update_scoreboard() method,add High score in f string of self.write().

**In main.py,**

Instead of doing game_is_on =False
and scoreboard.game_over() write scoreboard.reset().

**In snake.py,**

1.create new method reset() where we clear all segments and create snake again and set self.head to 0th segment.Hence,we are going to initialize snake back to center.

2.To make old snake disappear during new game,inside reset() method create for loop of the segments and make segments go to somewhere outside our screen.

**In scoreboard.py**

Go through practicefiles folder and learn how to read and write files,then modify the program to make sure that high scores of game are saved even when we rerun our program.

Create new data.txt file with initial high score as 0.

