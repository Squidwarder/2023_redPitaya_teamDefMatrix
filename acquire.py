# The burst signals tend to end quickly. So, to capture them you need to set the acquisition 
# trigger first and then trigger the generation. This is the same as trying to capture a signal 
# while your Oscilloscope is in Single mode. Otherwise, you are just waiting for an event that 
# is not going to happen.

import numpy as np
import math
import time
from matplotlib import pyplot as plt

import redpitaya_scpi as scpi

IP = "169.254.138.35"

rp_s = scpi.scpi(IP)

func_dct = {1:"SQUARE", 2:"TRIANGLE", 3:"SAWU",
            4:"SAWD", 5:"PWM", 6:"SINE", 7:"ARBITRARY",
            8:"DC", 9:"DC_NEG"}

#wave_form1 = "SQUARE"
#freq = 57600
#ampl = 1


rp_s.tx_txt('ACQ:RST')

# ? This should give us 3 samples per pulse of the square signal
# ? at dec of 128, the output frequency is roughly 118 samples per unit
# ? each unit takes 7 / (57.6 k) seconds
dec = "128"

trig_level = "0.1"
trig_delay = 7000

rp_s.tx_txt('ACQ:DATA:FORMAT ASCII')        # Format of the data (ASCII or BIN)
rp_s.tx_txt('ACQ:DATA:UNITS VOLTS')         # VOLTS or RAW
rp_s.tx_txt('ACQ:DEC '+ dec)                     # Decimation factor
rp_s.tx_txt('ACQ:TRIG:LEV '+trig_level)             # Trigger level in volts
rp_s.tx_txt(f'ACQ:TRIG:DLY {trig_delay}')

rp_s.tx_txt('ACQ:START')                    # Start acquiring data
time.sleep(4)
rp_s.tx_txt('ACQ:TRIG CH1_NE')              # Set the trigger

# Wait for the trigger
while 1:
    rp_s.tx_txt('ACQ:TRIG:STAT?')           # Get Trigger Status
    if rp_s.rx_txt() == 'TD':               # Triggered?
        break

rp_s.tx_txt('ACQ:SOUR1:DATA?')              # Read full buffer (source 1)
data_string1 = rp_s.rx_txt()                 # data into a string

# Remove brackets and empty spaces + string => float
data_string1 = data_string1.strip('{}\n\r').replace("  ", "").split(',')
data1 = list(map(float, data_string1))        # transform data into float

plt.plot(data1)
plt.show()

with open("received_signal.txt", "w") as text_file:
    text_file.truncate(0)
    for em in data1:
        text_file.write(str(em))
        text_file.write("\n")