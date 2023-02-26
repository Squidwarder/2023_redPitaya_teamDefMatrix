morse_encode = {"A":"10111", "a":"10111", "B":"111010101", "C":"11101011101",
                "D": "1110101", "E":"1", "F":"101011101", "G":"111011101",
                "H":"1010101", "I":"101", "J":"1011101110111", "K":"111010111", # K is also general invitation to transmit (first contact)
                "L":"101110101", "M":"1110111", "N":"11101", "O":"11101110111",
                "P":"10111011101", "Q":"1110111010111", "R":"1011101", "S":"10101",
                "T":"111", "U":"1010111", "V":"101010111", "W":"101110111",
                "X":"11101010111", "Y":"1110101110111", "Z":"11101110101",
                "0":"1110111011101110111", "1":"10111011101110111", "2":"101011101110111",
                "3":"1010101110111", "4":"10101010111", "5":"101010101", "6":"11101010101",
                "7":"1110111010101", "8":"111011101110101", "9":"11101110111011101",
                ".":"10111010111010111", ",":"1110111010101110111", "?":"101011101110101",
                "\'":"1011101110111011101", "!":"1110101110101110111", "/":"1110101011101",
                "(":"111010111011101", ")":"1110101110111010111", "&":"10111010101",    # ( is also exclusive invitation to transmit (any other message)
                ":":"11101110111010101", ";":"11101011101011101", "=":"1110101010111",
                "+":"1011101011101", "-":"111010101010111", "_":"10101110111010111",
                "\"":"101110101011101", "$":"10101011101010111", "@":"10111011101011101",
                "End of work":"101010111010111", "Error":"101010101010101",             # end of work - the last message of each side
                "Starting signal":"111010111010111", "New message follows":"1011101011101",
                "Verified":"10101011101"}

def morse_encode(plaintext, msg_state):
    #! plain text is a string of words, need to ensure that letters are in capital
    #! msg_state indicates whether the current message is first contact, last message
    #! or messages in between

    ptext_list = plaintext.split(" ")

    ctext_list = list()

    for words in ptext_list:
        encoded = ""
        #! ensure that the words are in uppercase, to ensure no Key errors
        for i in range(len(words.upper())):
            try:
                encoded += morse_encode[words[i]]
                if i + 1 != len(words):
                    encoded += "000"
            except:
                print("Key Error for Encode Dict: Unexpected value encounterd")
                continue

        ctext_list.append(encoded)

    if len(ctext_list) > 1:
        ciphertext_sentence = "0000000".join(ctext_list)
    else:
        ciphertext_sentence = ctext_list[0]
        
    #* Encoded message is in the format of:
    #* Starting signal, long pause, <message>, long pause, One of ending signals
    #* basically "111010111010111" + "0000000" + <message> + "0000000" + <end_signal>
    
    #* adds starting signal and long pause
    ciphertext_sentence = "111010111010111" + "0000000" + ciphertext_sentence
    
    #* adds trailing long pause
    ciphertext_sentence += "0000000"
    
    #*
    