import random

list1 = ["Hello", "Good morning", "Hallo pane", "Good evening", "Greetings", "Hi"]
list2 = ["Waazzup", "U ok?", "Wats poppin", "How do you do", "hELL NO", "stop trappin"]
list3 = ["Man", "Bro", "Brudda", "Hommie", "Choppa", "Dude"]

newPhrase = list1[random.randint(0, len(list1))-1] + " " + \
            list2[random.randint(0, len(list2))-1] + " " + \
            list3[random.randint(0, len(list3))-1]
print(newPhrase)
