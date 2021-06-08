# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])




###<<<SOLUTION>>>###
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])

#1.Copy above code and paste into web debugger
#2.Visualize execution and check execution of each line
#3.We find out that instead of printing list of elements with each element
# multiplied by 2,we are getting only 1 answer
# 4.So solution is to indent line 16 above so that list is printed

