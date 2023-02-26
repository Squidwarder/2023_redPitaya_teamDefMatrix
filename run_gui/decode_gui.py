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


def morse_decode_plain(file_data):
    """converts signal data to morse code first, then finally plaintext. 
        Returns the plaintext as a list of words (including start and end signal)

    Args:
        file_data (string): A string that contains signal data
    """
    
    num_data = file_data
    # for em in file_data:
    #     #! try to convert elements to "float" to do computation
    #     #? due to nature of signal
    #     #? A near 0 in signal is "1" for morse, and 0.2 is "0" for morse
    #     try:
    #         comp = float(em)
    #     except:
    #         break
    #     if (comp < 0.10):
    #         num_data.append(1)
    #     else:
    #         num_data.append(0)

    #print(len(num_data))

    # #? getting rid of the not important 0's at the beginning

    # for i in range(len(num_data)):
    #     if num_data[i] == 1:
    #         num_data = num_data[i:]
    #         break
        
    # print(len(num_data))

    # #* process the data, should expect around 118 samples per unit for dec 128
    # #* 59 samples per unit for dec 256
    # #! need to give it plenty of margin

    # morse_message = ""
    # cnt = 0
    # margin = 85

    # for i in range(1, len(num_data)):
    #     if (num_data[i] != num_data[i - 1]):

    #         #* for a single unit
    #         if cnt < margin:
    #             morse_message += str(num_data[i - 1])
    #             cnt = 0
    #         #* for 3 unit
    #         elif margin < cnt < margin * 3:
    #             morse_message += 3 * str(num_data[i - 1])
    #             cnt = 0
    #         #* handles 7 unit, the gap between words
    #         elif cnt < margin * 7:
    #             morse_message += "0000000"
    #             cnt = 0
    #         else:
    #             morse_message += "000"
    #             cnt = 0
    #             continue
    #     else:                
    #         cnt += 1

    #* this is the morse encoded message transmitted by signal
    morse_message = num_data
    print(len(morse_message))
    print(morse_message)
    
    ctext_list = morse_message.split("0000000")

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

    return plaintext_list