sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

#making dictionary
result={
    word :len(word) for word in sentence.split()
}

print(result)
