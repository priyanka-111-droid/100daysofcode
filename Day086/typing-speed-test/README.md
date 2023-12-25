# Typing Speed Test

Note: Run gui.py to see full functionality.

## Approach

### Logic (app.py)

- Typing formulas - https://www.speedtypingonline.com/typing-equations 
- To find errors, use zip to iterate simultaneously and do not use nested loop otherwise it counts errors for every character, which may lead to inaccurate results. 
- Net wpm needs to divide correct characters/5 and then divide by time elapsed in minute.If we subtract from Gross wpm, it can give negative value.So don't use that formula.
- Display gross wpm,net wpm and accuracy.

### GUI (gui.py)

- Include general Tkinter Set up (UI set up part)
- First added only for 1 prompt.
- When user clicks Done button,calculate gross wpm,net wpm and accuracy
- display gross wpm,net wpm and accuracy.


### Enhancements
- Ability to choose a random prompt from a list of prompts(prompts.py) which is taken from
https://randomwordgenerator.com/json/sentences.json
- Default value of number of questions(question_counter) will be 1.

#### Scenario 1 - User types prompt and clicks Done button.
- In this case, when user clicks Done button,calculate gross wpm,net wpm and accuracy
- Display gross wpm,net wpm and accuracy.
- When user clicks Done button,Download Story button is enabled and user and click on the 
button to get a `story.txt` file that combines all the sentences he has typed to form
a story.

#### Scenario 2 - User types prompt and clicks Next button.
- In this case, when user clicks Next button, calculate gross wpm,net wpm and accuracy of current question.
But we need to find total_gross_wpm, total_net_wpm,total_accuracy or combined gross wpm,net wpm and accuracy of all prompts obtained so far. Then we will take average of these values by dividing them by number of prompts answered so far.
```
total_gross_wpm += gross_wpm
total_net_wpm += net_wpm
total_accuracy += accuracy
```
- Increment number of questions(question_counter) by 1.
- Reset the start time for the new prompt
- Reset entry field.
- Display the next prompt.

