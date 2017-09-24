# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 10:16:18 2017

@author: Benoit Brizard
"""
import numpy as np
from toimport import hex
key=np.fromstring('ICE', dtype=np.uint8)
input =np.fromstring( "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal", dtype=np.uint8)
output=[0]*len(input)
fin=[0]*2*len(input)
hex.xorRepeatingKey(input,output,key,len(input))
hex.encodeHex(output,fin,len(output))
fin_str = ''.join(map(str, fin))
print fin_str