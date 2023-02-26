# The burst signals tend to end quickly. So, to capture them you need to set the acquisition 
# trigger first and then trigger the generation. This is the same as trying to capture a signal 
# while your Oscilloscope is in Single mode. Otherwise, you are just waiting for an event that 
# is not going to happen.

import numpy as np
import math
import time
from matplotlib import pyplot as plt
import decode_text

import redpitaya_scpi as scpi

#IP = "169.254.138.35"

IP = "169.254.6.210"

rp_s = scpi.scpi(IP)

func_dct = {1:"SQUARE", 2:"TRIANGLE", 3:"SAWU",
            4:"SAWD", 5:"PWM", 6:"SINE", 7:"ARBITRARY",
            8:"DC", 9:"DC_NEG"}

#wave_form1 = "SQUARE"
#freq = 57600
#ampl = 1


rp_s.tx_txt('ACQ:RST')

# ? at dec of 128, the output frequency is roughly 118 samples per unit
# ? at dec of 256, roughtly 60 samples per unit
# ? each unit takes 7 / (57.6 k) seconds
dec = "256"

trig_level = "0.1"
trig_delay = 7600

#! the end of a message is denoted by an ending signal:
#! "111010111" - "K" end of first contact
#! "101010111010111" - "End of work"
#! basically we stop processing package after reaching either of the two

reps = 10                                               # how many times the acquisition process takes place
#? proabably not going to take that much 
buff = np.zeros((reps,16384))                           # space for the acquired data

rp_s.tx_txt('ACQ:DATA:FORMAT ASCII')                    # Format of the data (ASCII or BIN)
rp_s.tx_txt('ACQ:DATA:UNITS VOLTS')                     # VOLTS or RAW
rp_s.tx_txt('ACQ:DEC '+ dec)                            # Decimation factor

rp_s.tx_txt(f'ACQ:TRIG:DLY {trig_delay}')

true_buff_num = 0

for i in range(reps):
    rp_s.tx_txt('ACQ:TRIG:LEV '+trig_level)             # Trigger level in volts
    rp_s.tx_txt('ACQ:START')                            # Start acquiring data
    time.sleep(1)
    rp_s.tx_txt('ACQ:TRIG CH1_NE')                      # Set the trigger

    # Wait for the trigger
    while 1:
        rp_s.tx_txt('ACQ:TRIG:STAT?')                   # Get Trigger Status
        if rp_s.rx_txt() == 'TD':                       # Triggered?
            break

    rp_s.tx_txt('ACQ:SOUR1:DATA?')                      # Read full buffer (source 1)
    data_string1 = rp_s.rx_txt()                        # data into a string

    # Remove brackets and empty spaces + string => float
    data_string1 = data_string1.strip('{}\n\r').replace("  ", "").split(',')
    buff[i, :] = list(map(float, data_string1))         # transform data into float
    data1 = buff[i, :]

    curr_buff_morse = decode_text.decode_from_list(data1)
    
    print(len(curr_buff_morse))
        
    if curr_buff_morse[len(curr_buff_morse)-9: len(curr_buff_morse)] == "111010111":
        true_buff_num = i + 1
        break

for j in range(true_buff_num):
        
    if j == 0:
        with open("received_signal_long.txt", "w") as text_file:
            for em in buff[j]:
                text_file.writelines(str(em))
                text_file.write("\n")
    else:
        with open("received_signal_long.txt", "a") as text_file:
            for em in buff[j]:
                text_file.writelines(str(em))
                text_file.write("\n")



######## PLOTTING THE DATA #########
fig, axs = plt.subplots(reps, sharex = True)            # plot the data (n subplots)
fig.suptitle("Measurements")

for i in range(0,reps,1):                               # plotting the acquired buffers
    axs[i].plot(buff[i])

plt.show()