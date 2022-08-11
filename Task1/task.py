### FUNDAMENTALS OF PYTHON ###

####### TASK 1 - CONVERT ALL LOWERCASE LETTERS TO UPPERCASE LETTERS AND VICE VERSA #######

string1 = input("Enter any String: ")
string1 = string1.swapcase()    #inbuilt function to swap the cases
print(s)


####### TASK 2 - CAPITALIZE FIRST TWO LETTERS OF EVERY WORD #######

lst = input("Enter the String: ").strip().split()
string = ""
for i in lst:       #for every word in the list
    for j in range(len(i)):      #for every letter in the word
        if (j == 0 or j == 1):           #for letter in the first and second position
            j = i[j].upper()
            string = string + j
        else:
            string = string + i[j]
    string = string + " "
print(string)


####### TASK 3 - DIRECTORY #######
def person_lister(i):
    def inner(person):
        return map(i, sorted(person, key=lambda x: int(x[1]), reverse=True))
    return inner

@person_lister
def name_format(person):
    return person[0] + " " + person[1]+ " " + person[2]+ " " + person[3]

if __name__ == '__main__':
    n = int(input("Enter the number of Persons: "))
    person = []
    for i in range(n):
        person.append(input().split())
        
    print("Modified Order of Persons: ")
    print(*name_format(person), sep="\n")
