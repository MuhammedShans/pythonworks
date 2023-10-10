f=open("C:/Users/abhij/Desktop/python_work/looping/FUNCTIONS/string/List works/fileinput/numbers.txt","r")
numbers=[line.rstrip("\n") for line in f]
# for n in numbers:
#     if n.startswith("kl"):
#         print(n)


kerala_numbers=[n for n in numbers if n.startswith("kl")]
print(kerala_numbers)