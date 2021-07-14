import sys
import string
#------------------------------------------------------------------------------


#the premade code and layout of the document wasn't very clear to me 
# which led to major confusion while doing this, my code works fine and
# has the correct output in the terminal when run, zoom learning is
#difficult to me. The default code wouldnt work on my laptop.
#No detriment policy should applied here.

def monoalphabetic_cipher(message, key, mode):
    # The body of this function is to be completed by you in your own python program
    ciphertext = ''
    decrypttext =''
    encryptedMessage = 'j BnlAnC vnBBjpn.'
    key = "jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi"
    
    if mode =='encrypt':
        for i in message:
            if i in string.ascii_lowercase: #using ascii table to reference position
                f = ord(i) - ord('a')  # of the char with accordance to the key
                ciphertext = ciphertext + key[f]
            else:
                ciphertext = ciphertext + i
    if mode  =='decrypt': 
        for i in encryptedMessage:
            if i in string.ascii_lowercase:
                f = key.find(i)
                decrypttext += chr(f +ord('a'))
            elif i in string.ascii_uppercase:
                f = key.find(i)
                decrypttext += chr(f +ord('a'))
            else:
                decrypttext = decrypttext + i
    return ciphertext + decrypttext


if __name__ == '__main__':
    
    numArgv = len(sys.argv) 
    message = 'a secret message.'
    key = 'jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi'

    # tells the program to encrypt or decrypt
    mode = 'encrypt' # set to 'encrypt' or 'decrypt'
    ciphertext = monoalphabetic_cipher(message, key,mode)
    mode = 'decrypt' 
    decrypttext = monoalphabetic_cipher(message, key, mode)


    if numArgv == 2:
        # get the message from the input given in the command line
        message = sys.argv[1]
    elif numArgv == 3:
        # get the message and key specified the input given in the command line
        message = sys.argv[1]
        key = int(sys.argv[2])

    elif numArgv > 3:
        # Instruction on providing message and key from command line
        print('+++Please input the exected message and key with correct format')
        print('+++python caesar_cipher.py my_message key') 
        print('+++where no space in my_message, key needs to be an integer for caesar cipher')
        
        print('+++For example: ')
        print('+++python caesar_cipher.py my_secrete_message 3')

        exit()
        


    ### Note: don't change the following code in your own program for displaying program outputs!!!
    print('##############################################')
    print('Cipher with key: ', key)
    print('##############################################')   
    print('Plain message: ', message)      
    print('Ciphertext: ',ciphertext)      
    print('Decrypted text: ', decrypttext)

