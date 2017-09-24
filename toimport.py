# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 10:11:31 2017

@author: Benoit Brizard
"""
import numpy as np
class hex :
    
    @staticmethod
    def xorRepeatingKey(input, output, key, length):

	for i in range(length):
	
		output[i] = np.bitwise_xor(input[i],key[i % 3]);
		
    @staticmethod
    def encodeHex(input, output,  length):

	  for i in range(length):
	
           hex.encodeByteHex(input[i], output,i);
	
    @staticmethod    
    def encodeByteHex(input, output,i):
	valeur_hex = "0123456789abcdef";
	index1=np.right_shift(input, 4)
	index2=input & 15
	output[2*i] = valeur_hex[index1];
	output[2*i+1] = valeur_hex[index2];

