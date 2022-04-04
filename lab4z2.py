fi = open("textbook.txt")
txt = fi.read()
print("total symbols " + str(len(txt)))
print("total symbols without space " + str(len(txt.replace(" ", ""))))

txt = txt.replace("!", "").replace(",", "").replace(".", "").split(" ")
print(len(txt))
distinct = set(txt)
print(len(distinct))