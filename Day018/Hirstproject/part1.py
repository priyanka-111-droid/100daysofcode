#Hirst project-part 1
#Extacting rgb values from spots
#and store rgb values as rgb tuples inside a list

#Tuples:
#like lists tuples are collection of items,but they cannot be MODIFIED and are denoted by () whereas lists are
#denoted by [].

import colorgram

# extract() returns colour objects
colours=colorgram.extract('Day018\Hirstproject\spot.jpg',12)
lis=[]
for x in colours:
    r=x.rgb.r
    g=x.rgb.g 
    b=x.rgb.b
    new_colour=(r,g,b)
    lis.append(new_colour)

print(lis)
# we have stored all values of lis into new list colour_list 

#using color picker,remove all rgb tuples which are shades of white
#saving in new list colour_list
colour_list=[(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16)]
