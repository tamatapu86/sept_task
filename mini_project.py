dictionary_1 = {}
while True:
    print("\nDictionary management system")
    print("1. Add a word: ")
    print("2. Search for Meaning: ")
    print("3. Display All Words: ")
    print("4. Update Meaning: ")
    print("5. Delete Word: ")
    print("6. Exit: ")
    
    choice = input("Enter your choice: ")
    if choice == "1":
        word = input("Enter the word: ").lower()
        meaning = input("Enter the meaning: ").lower()
        dictionary_1[word] = meaning
        print("Word added sucessfully!!!")
    elif choice == "2":
        word = input("Enter the word for search: ").lower()
        if word in dictionary_1:
            print("Meaning:",dictionary_1[word])
        else:
            print("Word not found in dictionary")
    elif choice == "3":
        if dictionary_1:
            print("Words and their meanings: ")
            for word,meaning in dictionary_1.items():
                print(f" {word} : {meaning}")
            else:
                print("Dictionary is empyty")
    elif choice == "4":
        word = input("Enter the word to update meaning: ")
        if word in dictionary_1:
            new_meaning = input("Enter the new meaning")
            dictionary_1[word] = new_meaning
            print("Meaning updated sucessfully!!!")
            print("Updated meaning",dictionary_1[word])
        else:
            print("Word not found in the dictionary")
    elif choice == "5":
        word = input("Enter the word to deleate ").lower
        if word in dictionary_1:
            del dictionary_1[word]
            print("word deleted sucessfully")
        else:
            print("word not found in dictionary")
    elif choice == "6":
        print("Exiting the programme")
    else:
        print("invalid inputs, Plesae enter valid inputs")

            







    

