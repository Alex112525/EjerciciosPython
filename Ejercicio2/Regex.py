import re

pattern_no_letters = "[^A-z]*$"
pattern_only_numbers = "[0-9]*$"
pattern_upper_letters = "[A-Z]*$"
pattern_lower_letters = "\ *[a-z]*$"
pattern_no_numbers = "[^0-9]*$"

string = "123"

if(re.match(pattern_no_letters,string)):
    print("No contiene letras")
else:
    print("Contiene letras")

if(re.match(pattern_only_numbers,string)):
    print("Solo numeros")
else:
    print("Otros caracteres ademas de numeros")

if(re.match(pattern_upper_letters,string)):
    print("Solo Letras mayusculas")
else:
    print("No solo letras mayusculas")

if(re.match(pattern_lower_letters,string)):
    print("Solo letras minusculas")
else:
    print("No solo letras minusculas")

if(re.match(pattern_no_numbers,string)):
    print("No contiene numeros")
else:
    print("Contiene numeros")
