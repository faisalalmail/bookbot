print("hello world")
with open("books/frankenstein.txt") as f:
    file_contents = f.read()

length = len(file_contents.split())
print(f"The book contains {length}")

with open("books/frankenstein.txt") as fr:
    file_contents1 = fr.read()

low_cased = file_contents1.lower()

char_count = {}
f_length = len(low_cased)

for char in low_cased:
    if char in char_count:
        char_count[char] = char_count[char] + 1
    else:
        char_count[char] = 1

print(char_count)

for cha in char_count:
    print(f" the characher {cha} was found {char_count[cha]} times")
#for i in range(0,f_length):
#    if 
print("---first report end---")

to_sort = []

def sort_by(e):
    return e["num"]

for cha in char_count:
    to_sort.append({"letter":cha,"num":char_count[cha]})

to_sort.sort(reverse=True, key=sort_by)


for k in to_sort:
    if k["letter"].isalpha():
        print(f"The {k["letter"]} character was found {k["num"]} times")

print("___Report End___")