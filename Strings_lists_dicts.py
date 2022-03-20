# String

my_string = "some text"
print(my_string)
print("1, 2, 3, 4, 5".split(', '))
word_of_my_string = my_string.split(' ')
second_string = "street/house/apartment"
words_of_second_string = second_string.split('/')
print(word_of_my_string)
print(words_of_second_string)
print("INDEX", my_string[3])
print(my_string.find('me text'))
print(my_string.upper())
print(my_string.lower())
print(my_string.startswith("so"))
print(my_string.endswith("ext"))
print(my_string.replace(' ', '-'))
print(', '.join(['1', '2', '3', '4', '5']))
random_number = 12
print(f"another one text, and my old text is {my_string}, random number {random_number}")
print(" double quotes: \" \", single quotes in quotes: ' '")

# List
my_list = [1, True, "sdad", [234214, 242342, 3, 24]]
print(my_list)
print(my_list.append(False))
print(my_list.extend([1, 2, 4, 5, 6]))
print(my_list.remove("sdad"))
print(my_list)

# Dict
my_dict = {1: "asd", 2: "dsds", 3: "caca"}
print(my_dict)
print(my_dict[1])
print(my_dict[2])
print(my_dict[3])
print(my_dict.keys())

if 7 in my_dict.keys():
    print(my_dict[7])

print(my_dict.get(2, "WRONG KEY"))

print(my_dict.update({4: "faga"}))
print(my_dict)
