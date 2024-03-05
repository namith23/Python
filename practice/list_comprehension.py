#number = [1,2,3]
#new_num = [n + 1 for n in number]
#print(new_num)

#name = "qwerty"
#letters_list = [letter for letter in name]
#print(letters_list)

#range = [num * 2 for num in range(1,5)]
#print(range)

names = ["alex", "andrew", "raju", "Dave","Freddy","beth"]
short_name = [name.upper() for name in names if len(name) > 5]
print(short_name)