student_dict={
    "student":["Angela","James","Lily"],
    "score":[56,76,98]
}

#Looping through dictionary
for(key,value) in student_dict.items():
    print(key)
    # print(value)

#can work with dataframe like dictionary
import pandas

student_data_frame=pandas.DataFrame(student_dict)
# print(student_data_frame)

#Loop through dataframe
for (key,value) in student_data_frame.items():
    print(value)

#Loop through rows of dataframe
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
for(index,row) in student_data_frame.iterrows():
    # print(row.student)
    # print(row.score)
    if(row.student=="Angela"):
        print(row.score)
