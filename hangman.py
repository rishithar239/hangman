import random

words = ['ballon','camel','pencil']
chosen_word = random.choice(words)

strings = [ 

''' _______
     |/      |
     |      (_) 
     |      \|/
     |       |
     |      / \
     |
 jgs_|___ ''',
 ''' _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
 jgs_|___ ''',
 ''' _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
 jgs_|___ ''' ,
 '''  _______
     |/      |
     |      (_)
     |      \|
     |       |
     |      
     |
 jgs_|___ ''' ,
 '''  _______
     |/      |
     |      (_)
     |       |
     |       |
     |      
     |
 jgs_|___ ''' ,
 '''  _______
     |/      |
     |      (_)
     |     
     |     
     |     
     |
 jgs_|___ ''']

length = len(chosen_word)
display_word = '_'*length
print(display_word) 
def replace_str_index(text,index=0,replacement=''):
    return (text[:index]) + replacement + (text[index+1:])

end_of_game = False
lives=6

while not end_of_game:
    guessed_letter = input("guess a letter:").lower()
    if guessed_letter in display_word:
        print("you've already guessed this word")
        
    for position in range(length):
        if guessed_letter == chosen_word[position]:
            display_word = replace_str_index(display_word,position,guessed_letter)
    
    print(display_word)
    
    if guessed_letter not in chosen_word:
        print("Sorry, you've guessed wrong letter.")
        print(strings[lives - 1])
        print()
        lives -= 1

    if display_word == chosen_word:
        end_of_game = True
        print("You win!")
        
    if lives == 0:
        end_of_game = True
        print("you lose")

