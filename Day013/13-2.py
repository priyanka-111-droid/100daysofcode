# Step 2:Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1,6)
# print(dice_imgs[dice_num])

#####<<SOLUTION>>>#####

from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]

#First we change code so that it will consistently give an error EVERY time we run it
#dice_num = 6 #this will always give an error

#Now that error shows up consistently,it is easier to debug
#Now we know that we get list index out of range if dice_num=6
#Lists start counting from 0
dice_num=randint(0,5)
print(dice_imgs[dice_num])
