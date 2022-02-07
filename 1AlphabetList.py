#displays all the elements in the list
letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
print(letters)

#Display the second letter in the alphabet
for index  in range(1,26,2):
    print(letters[index])

    #displays the remaining letters
    print(letters[index-1])

