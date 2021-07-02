# Pong game

Step 1:

* Set up screen 
* create paddle and move paddle

Step 2:

* Create separate Paddle class and move all paddle funcionality to that class
* instantiate objects r_paddle and l_paddle from that class.

Step 3:

* Write separate Ball class
* Ball object has width of 20,height of 20,x_pos=0,y_pos=0(starts at center of screen)
* When screen refreshes make ball move up and towards right 

Step 4:Detect collision and bounce

* detect collision at top and bottom of screen and making ball bounce

Step 5:Detect when paddle misses

* when paddle misses,ball goes to center and then to left side

Step 6:Score keeping using scoreboard class and if ball touches paddle try to keep increasing ball speed .Once one player's paddle misses ball and we reset ,speed is set back to initial 0.1.