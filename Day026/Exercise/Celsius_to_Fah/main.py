weather_c = {
        "Monday": 12,
        "Tuesday": 14,
        "Wednesday": 15,
        "Thursday": 14,
        "Friday": 21,
        "Saturday": 22,
        "Sunday": 24,
    }


weather_f={day:(temp_c * 9/5) + 32  for (day,temp_c) in weather_c.items() }
print(weather_f)