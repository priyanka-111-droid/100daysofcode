# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)



###<<<SOLUTION>>>###

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
print(pages)
word_per_page = int(input("Number of words per page: "))
print(word_per_page)
total_words = pages * word_per_page
print(total_words) 


# 1.print(pages) to find out value of pages
# 2.print words_per_page to find out value 
#   But we get error for this line saying its not defined
# 3.Now we know there is a problem with words_per_page
# 4.hence we fix the code to =(assignment) instead of ==
# 5. = means assignment but == means does left side equal right side?
