        #dictinary of words
#add new word and their meaning 
#and updating a new meaning 
#and following actions: add a word,
# search for a meaning,
# display all words, 
# update meaning, 
# delete word etc...

dictionary={}
while True:
    print(" Dictiionary mangement")
    print("1.add" \
    " a new word")
    print("2.search for  meaning ")
    print("3.Display all words")
    print("4.update meaning")
    print("5.delete word")
    print("6.EXIT")
    
    choice=input("Enter u r cboice :")
    
    if choice=="1":
        word=input("enter a new word:").lower()
        meaning=input("enter their meaning:")
        dictionary[word]=meaning
        print("word added successfully!")

    elif choice=="2":
        word=input("Enter word to search:").lower()
        if word in dictionary:
            print("meaning:",dictionary[word] )
        else:
            print("word mot found")    
    elif choice==3:
        print(dictionary)

    elif choice=="4":
        word = input("Enter the word to update: ").lower()
        if word in dictionary:
            new_meaning = input("Enter the new meaning: ")
            dictionary[word] = new_meaning
            print("Meaning updated successfully!")
        else:
            print("Word not found.")
    elif choice=="5":
        word=input("Enter a WORD TO DELETE:")
        if word in dictionary:
            removed=dictionary.pop(word)
            print("Deleted successfully")
        else:
            print("word not found")
    else:
        print("enter correct choice")


            
