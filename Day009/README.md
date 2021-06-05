# Dictionaries

## 1. Dictionaries are created in the form of  key1 : value1, key2:value2,etc.

        programming_dictionary={
        "Bug":"Error in the program that prevents program from running as expected.",
        "Function":"A piece of code you can easily call over and over again.",
        }
        #RETRIEVING items from dictionary
        print(programming_dictionary["Bug"])
        
        #output:
        #Error in the program that prevents program #from running as expected.

        #ADDING items to dictionary
        programming_dictionary["Loop"]="Action of doing something over and over again."

        #PRINTING updated dictionary
        print(programming_dictionary)

        #EDITING value of a key
        programming_dictionary["Bug"]="A moth in your computer."

        #LOOPING through dictionary
        for item in programming_dictionary:
            print(item)    #will only print keys

        #output:
        #Bug
        #Function
        #Loop

        #to print key and its corresponding value
        for key in programming_dictionary:
            print(key) 
            print(programming_dictionary[key])


        #create new dictionary
        new_dictionary={}

        #wipe out existing dictionary
        programming_dictionary={}

## 2. Nesting Lists and Dictionaries

* Previously we saw how to put many key:value pairs in a dictionary separated by commas

        {
            key:value1,
            key2:value2,
        }

* But we can also use list and dictionary itself as value

        {
            key:[List],
            key2:{Dict},
        }

        #nesting
        capitals={
            "France":"Paris",
            "Germany":"Berlin,
        }
        #nesting list in dictionary
        travel_log={
            "France":["Paris","Lille"],
            "Germany":["Berlin","Stuttgart"],
        }
        #nesting dictionary in dictionary
        travel_log={
            "France":{
                "cities_visited":
                ["Paris","Lille"],
                "total_visits":12
            },
            "Germany":{
                "cities_visited":
                ["Berlin","Stuttgart"],
                "total_visits":9
            },
        }
        #nesting dictionaries in one list
        travel_log=[
            {
                "country":"France",
                "cities_visited":
                ["Paris","Lille"],
                "total_visits":12
            },
            {
                "country":"Germany",
                "cities_visited":
                ["Berlin","Stuttgart"],
                "total_visits":9
            },
        ]




# Exercises

## 1. Grading Program

Fork it from [here](https://replit.com/@appbrewery/day-9-1-exercise)

**Instructions:**

You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.

Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.

DO NOT modify lines 1-7 to change the existing student_scores dictionary.

DO NOT write any print statements.

This is the scoring criteria:

Scores 91 - 100: Grade = "Outstanding"

Scores 81 - 90: Grade = "Exceeds Expectations"

Scores 71 - 80: Grade = "Acceptable"

Scores 70 or lower: Grade = "Fail"

Expected Output

        '{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'
**Hint:**

Remember that looping through a Dictionary will only give you the keys and not the values.

If in doubt as to why your code is not doing what you expected, you can always print out the intermediate values.

At the end of your program, the print statement will show the final student_scores dictionary, do not change this.

Solution: [9-1.py](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day009/9-1.py)

## 2.Travel log

fork it from [here](https://replit.com/@appbrewery/day-9-2-exercise#README.md)

Instructions:

You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.

Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
You've visited Russia 2 times.

You've been to Moscow and Saint Petersburg.

DO NOT modify the travel_log directly. You need to create a function that modifies it.

Hint:

Look at the function call above to see what the name of the function should be.

The inputs for the function are positional arguments. The order is very important.

Feel free to choose your own parameter names.

Solution:[9-2.py](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day009/9-2.py)

# Project

## Secret Auction program

Fork starting code from [here](https://replit.com/@appbrewery/blind-auction-start)

See the flowchart [here](https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Blind%20Auction%20Flow%20Chart#R3VnbcpswEP0aPzYDCLB5tHNrZ9pMpu6kzaMMilEDiBHyLV%2FfFYirHMdp7JD4JUGrXV3Ont2V5AE6j9fXHKfhDxaQaGAZwXqALgaWZRqmAf%2BkZFNIHM8qBHNOA6VUC6b0iZSWSrqgAclaioKxSNC0LfRZkhBftGSYc7Zqqz2wqD1riudEE0x9HOnS3zQQoZK6jl13fCV0HpZTm65X9MS41FZbyUIcsFVDhC4H6JwzJoqveH1OIoleCUxhd%2FVMb7UyThKxj8Hs4R5fx%2BMlu%2F52dxPepdM7H31BxShLHC3UjtVixaaEgASAiGoyLkI2ZwmOLmvphLNFEhA5jQGtWuc7YykITRD%2BJUJslHvxQjAQhSKOVG8xp5zo2b0pUcYW3Cc7NlSSBPM5ETv0rMoDwF3CYiL4Buw4ibCgy%2FY6sCLRvNKrYYYPhfQrUDc11Ke%2Fxj9%2FadDXwEqUViEVZJrifP8riLdtIC4JF2S9G0Z928rAHimuqmi1VXNVU99TorBBemQcCSfn1Nhp7clOu092Wjo7Q0hclhEBcDKJchbn6VWcpZsPx1mvZ84OT42z9p6cdfvkrK2hPs4e84LP4e8NjokcIUkXon%2FCOk6LsKajM9a0t1DWPhZlvVOjrLsnZUd9UtbdSdkJ2FrGLaew0Y%2FG2OpI2xtjTf0E9ckp%2B1YqKtNbRmHmynOO1fYcGnU8UoSIsuo4pVrG%2F%2FtppHM8COqEjJOgojqsQB4usLwsUl9QcESOAKwUIjmU6o9kUxnlQ54NLBfHkvDJLEsrh%2FQZKmh41gmWLQcSc%2BjoweIcLVhGfcQGWVPxR5nL7%2FuG%2FGLd6LjYlI0EdpubAISqed%2Fsq83yVml3wCg00Z6VwxweIl7HnONNQyGVcZg9H872yGxxy%2B5e%2BTv6yHN26cNHsYKDxnwFdi90Mxt0Uzw6CcI1noz6eLDQ34mKwwp9KLIzz9N5%2FpfJ5kCu141gR5MZNNy5%2FFpkhMtsvgplpl%2FhnKp51p%2FJEtBN3SGLZ4usp7RdVcqX0na3oh4Oc%2F2AeE8yDSbYtGjjgSM6T%2BDbh82DJ9BEQkN9HI1VR0yDoIg6ktEnPMuHksRW%2BQfGdSYD50KOBYGWFTF3IKiRZ7dzkmFrQG87S1pHw9nrtTxWOeo1BbKVrerk9Q75arhnvnrrC9b2gmZ1HnvQcL%2Fz7GsLbbdwOvbuQttd12v1zeE7FGZTf5o6jwjm1fk68zkhiZ6I3%2FkMjZzOK%2FSWVLztSe9ot80y9TSAu6L5LaTALYQ1kEyUdQyuMlVX%2ByqT2wTEj4pKCSpx%2B4azokkii2fPHnCGL3vA9LYUQ%2FdoLrA0F9ywT18LXdTB2dBxRoephdCsf2osMkr9iy26%2FAc%3D)

Solution: [9-3.py](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day009/9-3.py)



