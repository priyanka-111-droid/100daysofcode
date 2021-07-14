import pandas
data=pandas.read_csv("Day026/Project/NATO-alphabet/nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
phonetic_dict={ row.letter:row.code for (index,row) in data.iterrows()}
# print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word=input("Enter a word :").upper()
result=[phonetic_dict[x]  for x in word]
print(result)



#OTHER WAY TO DO THIS PROJECT:
# word=input().upper()
# result=[]
# for x in word:
#     for(index,row) in data.iterrows():
#         if(row.letter==x):
#             result.append(row.code)

# print(result)


    
