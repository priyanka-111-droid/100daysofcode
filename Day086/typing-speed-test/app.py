from time import time

prompt = "hello, my name is Priyanka"
print("Prompt is: " + prompt)
start_time = time()
typed_text = input("Enter the above prompt as fast as possible: ")
end_time = time()


#gross wpm
characters_typed = len(typed_text)
word_count = characters_typed / 5
time_elapsed = end_time - start_time
time_elapsed_in_min = time_elapsed / 60
gross_wpm = word_count / time_elapsed_in_min


#net wpm
errors=0
for char1, char2 in zip(typed_text, prompt):
    if char1 != char2:
        errors += 1
correct_chars = characters_typed - errors
net_wpm = (correct_chars / 5) / (time_elapsed_in_min)

#accuracy
accuracy = (correct_chars / characters_typed) * 100


#print results
print(f"\nGross Typing speed: {gross_wpm:.2f} gross WPM")
print(f"Net typing speed: {net_wpm:.2f} net WPM")
print(f"Accuracy: {accuracy:.2f}%")

