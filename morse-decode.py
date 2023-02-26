morse_decode = {"10111":"A", "111010101":"B", "11101011101":"C",
                "1110101":"D", "1":"E", "101011101":"F", "111011101":"G",
                "1010101":"H", "101":"I", "1011101110111":"J", "111010111":"K", # K is also general invitation to transmit (first contact)
                "101110101":"L", "1110111":"M", "11101":"N", "11101110111":"O",
                "10111011101":"P", "1110111010111":"Q", "1011101":"R", "10101":"S",
                "111":"T", "1010111":"U", "101010111":"V", "101110111":"W",
                "11101010111":"X", "1110101110111":"Y", "11101110101":"Z",
                "1110111011101110111":"0", "10111011101110111":"1", "101011101110111":"2",
                "1010101110111":"3", "10101010111":"4", "101010101":"5", "11101010101":"6",
                "1110111010101":"7", "111011101110101":"8", "11101110111011101":"9",
                "10111010111010111":".", "1110111010101110111":",", "101011101110101":"?",
                "1011101110111011101":"\'", "1110101110101110111":"!", "1110101011101":"/",
                "111010111011101":"(", "1110101110111010111":")", "10111010101":"&",    # ( is also exclusive invitation to transmit (any other message)
                "11101110111010101":":", "11101011101011101":";", "1110101010111":"=",
                "1011101011101":"+", "111010101010111":"-", "10101110111010111":"_",
                "101110101011101":"\"", "10101011101010111":"$", "10111011101011101":"@",
                "101010111010111":"End of work", "101010101010101":"Error",             # end of work - the last message of each side
                "111010111010111":"Starting signal", "1011101011101":"New message follows",
                "10101011101":"Verified"}

ciphertext = input("Enter a code to be decoded: [10111 is A] ")

ctext_list = ciphertext.split("0000000")

plaintext_list = list()

for words in ctext_list:
    word = ""
    letters = words.split("000")
    for let in letters:
        try:
            word += morse_decode[let]
        except:
            print("KeyError: An unexpected symbol has come up")
            continue
    
    plaintext_list.append(word)

plaintext_sentence = " ".join(plaintext_list)

print(plaintext_sentence)

#* the first word is the starting signal, and the last word is the ending signal
print(plaintext_list[1:len(plaintext_list) - 1])