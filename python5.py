input="123@"
print(type(input))

dummy_digit=''
dummy_char=''

for char in input:
    if char.isdigit():
        dummy_digit+=char
    else:
         dummy_char+=char   
         break
print(type(int(dummy_digit)))
print(type(dummy_char))    