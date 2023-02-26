def decode_from_list(signal):
    
    #! signal is a list of floating number

    #? data list has "str" type elements

    #print(type(data_list[0]))
    #print(data_list[0])


    num_data = []
    for em in signal:
        #? try to convert elements to "float" to do computation
        #? due to nature of signal
        #? A near 0 in signal is "1" for morse, and 0.2 is "0" for morse
        try:
            comp = em
        except:
            break
        if (comp < 0.10):
            num_data.append(1)
        else:
            num_data.append(0)

    #print(len(num_data))

    #? getting rid of the not important 0's at the beginning

    for i in range(len(num_data)):
        if num_data[i] == 1:
            num_data = num_data[i:]
            break
        
    #print(len(num_data))

    #* process the data, should expect around 118 samples per unit
    #! need to give it plenty of margin

    morse_message = ""
    cnt = 0
    
    margin = 85

    for i in range(1, len(num_data)):
        if (num_data[i] != num_data[i - 1]):

            #* for a single unit
            if cnt < margin:
                morse_message += str(num_data[i - 1])
                cnt = 0
            #* for 3 unit
            elif margin < cnt < margin * 3:
                morse_message += 3 * str(num_data[i - 1])
                cnt = 0
            #* handles 7 unit, the gap between words
            elif cnt < margin * 7:
                morse_message += "0000000"
                cnt = 0
            else:
                morse_message += "000"
                cnt = 0
                break

            
        cnt += 1

    #print(len(morse_message))

    #print(morse_message)
    
    return morse_message