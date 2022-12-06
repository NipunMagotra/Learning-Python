letter = '''Dear NAME
         you are selected
         DATE'''
Name = input("What's your name\n")
date = input("What's your date\n")
letter = letter.replace("NAME", Name)
letter = letter.replace("DATE", date)
print(letter)
