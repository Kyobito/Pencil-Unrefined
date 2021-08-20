def caesar_cipher(word, base):
  up_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  low_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  new_word = ''
  for letter in word:
    if letter.isnumeric() == True or letter.isalpha()==False:
      new_word += letter
    elif letter.isupper == True:
      try:
        new_word += up_alpha[up_alpha.index(letter)+base]
      except IndexError:
        difference = (len(up_alpha)-1)-up_alpha.index(letter)
        new_word += up_alpha[difference]
    else:
        try:
          new_word += low_alpha[low_alpha.index(letter)+base]
        except IndexError:
          difference_low = (len(low_alpha)-1)-low_alpha.index(letter)
          new_word += low_alpha[difference_low]
            
  return new_word

def substitution(word, substitute, specify): #proto
  char_list = list(substitute)
  new_word = ''
  counter = 0
  if len(substitute) != len(specify):
    return "Second and third arguments were not entered correctly"
  for letter in word:
    counter=0
    for sub in char_list:
      if letter == sub:
        counter+=1
        new_word+=specify[char_list.index(sub)]
    if counter==0:
        new_word+=letter
  return new_word
    
def binary(number):
  new_number = bin(number) + ""
  new_number = new_number[2:]
  return new_number

def hexadecimal(number):
  new_number = hex(int(number))
  new_number = new_number[2:]
  return new_number