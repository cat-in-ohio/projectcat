import random
book_word=['python', 'java', 'kotlin', 'javascript']
word=random.choice(book_word)
word_list=list('_'*len(word))
attempt=10
while attempt>0:
    print("/nCurrent word: "+''.join(word_list))
    letter=input("Input a letter: ").lower()
    if letter in word:
        for i in range(len(word)):
            if word[i]==letter:
                word_list[i]=letter
        print("You have guessed the lettee!")
    else:
        attempt-=1
        print("That letter doesn't appear in the word."+str(attempt)+"attempts left")
    if '_' not in word_list:
        print("You guessed the word "+word+"!")
        print("You survived!")
        break
    if attempt==0:
        print("You lost!")
    

            


