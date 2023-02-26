import numpy as np
import math
import time
from matplotlib import pyplot as plt
import redpitaya_scpi as scpi
from morseEncoder import *

#IP = "169.254.138.35"

IP = "169.254.6.210"

rp_s = scpi.scpi(IP)

def run(sentence):
    plaintext = sentence.upper()
    ptext_list = plaintext.split(" ")

    '''
    #### Creating arbitrary signal ##### 
    N = 16384    # Signal length in Samples (16384 = buffer) 
    t = np.linspace(0, 1, int(N))*2*np.pi  # Sample vector 
    x = 1/2*np.sin(t) + 1/2*np.sin(2*t)		  # One period of custom signal

    waveform_ch_10 = [] 

    for n in x: # Transforming custom signal into a string (appropriate shape for SCPI commands) 
        waveform_ch_10.append(f"{n:.5f}") 
    waveform = ", ".join(map(str, waveform_ch_10))
    '''

    # func_dct = {1:"SQUARE", 2:"TRIANGLE", 3:"SAWU",
    #             4:"SAWD", 5:"PWM", 6:"SINE", 7:"ARBITRARY",
    #             8:"DC", 9:"DC_NEG"}

    N = 16384
    t = np.linspace(0, 1, int(N))*2*np.pi  # Sample vector
    wave_form1 = "ARBITRARY"
    freq = 57600 * (2/16384) #Set number of samples to be 10
    ampl = 1
    waveform  = pulse(add_signal(encode(ptext_list)))
    waveform1 = np.zeros(16384, dtype = float)
    idx = 0
    for i in waveform:
        waveform1[idx] = float(i)
        idx= idx+1
    waveform = ", ".join(waveform)
    waveform = list(map(float,waveform.split(", ")))
    #plt.plot(waveform1)
    #plt.show()
    #print(waveform)



    waveform  = pulse(add_signal(encode(ptext_list)))
    waveform = ", ".join(map(str,list(waveform)))

    rp_s.tx_txt('GEN:RST')  # Reset generator 
    rp_s.tx_txt('SOUR1:FUNC ' + str(wave_form1).upper()) # Signal shape 
    rp_s.tx_txt('SOUR1:FREQ:FIX ' + str(freq))  # Frequency (frequency  
    rp_s.tx_txt('SOUR1:VOLT ' + str(ampl))  # Amplitude 
    rp_s.tx_txt('SOUR1:TRAC:DATA:DATA '+waveform)

    rp_s.tx_txt('SOUR1:BURS:STAT BURST')     # Turn ON Burst mode 
    rp_s.tx_txt('SOUR1:BURS:NCYC 1')    # Number of periods in a Burst 
    rp_s.tx_txt('SOUR1:BURS:NOR 1')     # Number of repeated Bursts 
    rp_s.tx_txt('SOUR1:BURS:INT:PER 100')   # Period between bursts in microseconds (1 burst + delay) 

    rp_s.tx_txt('SOUR1:TRIG:SOUR INT')  # Triger Source internal 
    rp_s.tx_txt('OUTPUT1:STATE ON')     # Output 1 turned ON 
    rp_s.tx_txt('SOUR1:TRIG:INT')
    print("Success")    