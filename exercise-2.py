# TASK 1
text = "Berlin is a world city of culture, politics, media and science."
print(len(text))

# TASK 2
## Option 1
text = "Berlin is a world city of culture, politics, media and science."
print(text[0], text[-1])
## Option 2
text = "Berlin is a world city of culture, politics, media and science."
first_character = text[0]
last_character = text[-1]
print(first_character +" "+ last_character)
## Option 3
text = "Berlin is a world city of culture, politics, media and science."
print(text[0], text[62])

# TASK 3
## Option 1
text = "Berlin is a world city of culture, politics, media and science."
print("First three characters: ", text[0:3].upper())
## Option 2
text = "Berlin is a world city of culture, politics, media and science."
text_upper = (text.upper())
print("First three characters:", text[0:3].upper())

# TASK 4
## Option 1
text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital. "
print("B appears:", text.count("B"), "times")
## Option 2
text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital"
result = text.count("B")
print("B appears:", result, "times")

# TASK 5
## Option 1
text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."
print("Last ten characters:", text[-10:])
## Option 2
text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."
print(f"Last ten characters: {text[-10:]}")

# TASK 6
## Option 1
text = "---Python programming---"
print(text.strip("-"))
## Option 2
text = "---Python programming---"
print(text.replace("-", " "))
## Option 3
text = "---Python programming---"
print(text.lstrip("-").rstrip("-"))

# TASK 7
## Option 1
first_name = "Mary"
last_name = "Mat"
print(f"Firstname: {first_name}\nLastname: {last_name}")
## Option 2
first_name = "Mary"
last_name = "Mat"
print("Firstname: " + first_name + "n\ Lastname: ", last_name)
## Option 3
first_name = "Mary"
last_name = "Mat"
print("Firstname:", first_name)
print("Lastname:", last_name)