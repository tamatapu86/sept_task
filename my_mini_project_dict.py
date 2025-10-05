dictionary = {}

while True:
    print("\nDictionary Management System")
    print("1. Add a word")
    print("2. Search for Meaning")
    print("3. Display all the words")
    print("4. Update meaning")
    print("5. Delete word")
    print("6. Exit")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        word = input("Enter the word to add: ").lower()
        meaning = input("Enter the meaning to the word: ").lower()
        dictionary[word] = meaning
        print("Word and Meaning enetered sucessfully")

    elif choice == "2":
        word = input("Enter the word to know meaning: ").lower()
        if word in dictionary:
            print("Meaning", dictionary[word])
        else:
            print("Word not found in dictionary")
    
    elif choice == "3":
        if dictionary:
            print("words and thier meanings")
            for word,meaning in dictionary.items():
                print(f'{word} : {meaning}')
        else:
            print("Dictionary is empty ")
    
    elif choice == "4":
        word = input("Enter the word to update the meaning: ").lower()
        if word in dictionary:
            new_meaning = input("Enter the meaning: ").lower()
            dictionary[word] = new_meaning
            print("Meaning updated sucessfully!")
            print("Updated meaning" ,dictionary[word])
        else:
            print("Word not found in Dictionary")
    elif choice == "5":
        word = input("Enter the word to delete: ").lower()
        if word in dictionary:
            del dictionary[word]
            print("Word Deleted sucessfully")
        else:
            print("Word not found in dictionary")
    elif choice == "6":
        print("Exited  the programme!!!")
        break
    else:
        print("Invalid input, Please enter valid input")













