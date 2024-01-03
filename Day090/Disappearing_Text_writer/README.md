# Disappearing Text Writing App


## Feature
App lets user type but when user does not type anything for more than 10 seconds, app deletes whatever has
been written so far.

## Approach:

- Build Text Editor class using Tkinter GUI
- Start timer and start main loop.
- Attach bindings on keypresses and buttons so that if user presses them, timer starts again.
- If user does not press anything for 10 seconds,start timer again and go to a function `user_is_inactive` where 
all that he has written so far is deleted.

