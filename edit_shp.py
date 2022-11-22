
import geopandas as gpd
import pandas as pd
from pandas import MultiIndex, Int16Dtype
import os
import numpy as np
import fiona
from shapely.geometry import mapping, shape
from googletrans import Translator
from geopandas import GeoDataFrame
import googletrans
from pathlib import Path
import glob
import matplotlib
from deep_translator import GoogleTranslator
import sys


# -ης, ων, 

translator = Translator()

def grklsh_to_gr():

    char_to_gr= {
        'th': 'θ',
        'TH': 'Θ',
        'ps': 'ψ',
        'PS': 'Ψ',
        'KS': 'Ξ',
        'ks': 'ξ',
        'ch': 'χ',
        'CH': 'Χ',
        'ph': 'φ',
        'PH': 'Φ',
        'sfin': 'ς',
        'A': 'Α',
        'a': 'α',
        'B': 'Β',
        'b': 'β',
        'C': 'Γ',
        'c': 'γ',
        'D': 'Δ',
        'd': 'δ',
        'E': 'Ε',
        'e': 'ε',
        'F': 'Φ',
        'f': 'φ',
        'G': 'Γ',
        'g': 'γ',
        'H': 'Η',
        'h': 'η',
        'I': 'Ι',
        'i': 'ι',
        'K': 'Κ',
        'k': 'κ',
        'L': 'Λ',
        'l': 'λ',
        'M': 'Μ',
        'm': 'μ',
        'N': 'Ν',
        'n': 'ν',
        'O': 'Ο',
        'o': 'ο',
        'P': 'Π',
        'p': 'π',
        'R': 'Ρ',
        'r': 'ρ',
        'S': 'Σ',
        's': 'σ',
        'T': 'Τ',
        't': 'τ',
        'U': 'Υ',
        'u': 'υ',
        'V': 'B',
        'v': 'β',
        'W': 'Ω',
        'w': 'ω',
        'X': 'Ξ',
        'x': 'ξ',
        'y': 'υ',
        'Y': 'Υ',
        'Z': 'Ζ',
        'z': 'ζ',
        'í': 'ί',
        'Ì': 'Ί',
        'ò': 'ό',
        'Ò': 'Ό',
        'à': 'ά',
        'á': 'ά',
        'À': 'Ά',
        'Á': 'Ά',
        'Ù': 'ύ',
        'ó': 'ό',
        'ú': 'ύ',
        'ý': 'ύ',
        'ï': 'ϊ',
        'é': 'έ',
        'É': 'Έ',
        'w_accent': 'ώ'



    }
    
    return char_to_gr

def translate2gr():
    tmp= [None] * 7000 #list with placeholder for 7000 items

    for i in range(len(my_input)):
        char_input=my_input[i]
        char_dict=grklsh_to_gr()

        if char_input in grklsh_to_gr(): 
            if(char_input == 'p' and (my_input[i + 1]) == 's'): # all those elif are for the double latin letters that create one greek letter
                tmp[i] = char_dict.get('ps')
                
            elif(char_input == 's' and my_input[i-1] == 'p'):
                continue
            elif(char_input == 'P' and (my_input[i + 1]) == 's'):
                tmp[i] = char_dict.get('PS')
                
            elif(char_input == 's' and my_input[i-1] == 'P'):
                continue
            elif(char_input == 'K' and (my_input[i + 1]) == 's'):
                tmp[i] = char_dict.get('KS')
                
            elif(char_input == 's' and my_input[i-1] == 'K'): #KS,PS,TH,CH, PH
                continue

            elif(char_input == 'P' and (my_input[i + 1]) == 'S'):
                tmp[i] = char_dict.get('PS')
            elif(char_input == 's' and (char_input == my_input[-1] or my_input[i + 1] == '\s')):
                tmp[i] = char_dict.get('sfin')
                
                
            elif(char_input == 'S' and my_input[i-1] == 'P'):
                continue
            elif(char_input == 'k' and (my_input[i + 1]) == 's'):
                tmp[i] = char_dict.get('ks')
                
            elif(char_input == 's' and my_input[i-1] == 'k'):
                continue
            elif(char_input == 'K' and (my_input[i + 1]) == 'S'):
                tmp[i] = char_dict.get('KS')
                
            elif(char_input == 'S' and my_input[i-1] == 'K'):
                continue
            elif(char_input == 't' and (my_input[i + 1]) == 'h'):
                tmp[i] = char_dict.get('th')
                
            elif(char_input == 'h' and my_input[i-1] == 't'):
                continue
            elif(char_input == 'T' and (my_input[i + 1]) == 'h'):
                tmp[i] = char_dict.get('TH')
                
            elif(char_input == 'h' and my_input[i-1] == 'T'):
                continue
            elif(char_input == 'T' and (my_input[i + 1]) == 'H'):
                tmp[i] = char_dict.get('TH')
                
            elif(char_input == 'H' and my_input[i-1] == 'T'):
                continue
            elif(char_input == 'c' and (my_input[i + 1]) == 'h'):
                tmp[i] = char_dict.get('ch')
                
            elif(char_input == 'h' and my_input[i-1] == 'c'):
                continue
            elif(char_input == 'C' and (my_input[i + 1]) == 'H'):
                tmp[i] = char_dict.get('CH')
                
            elif(char_input == 'H' and my_input[i-1] == 'C'):
                continue

            elif(char_input == 'C' and (my_input[i + 1]) == 'h'):
                tmp[i] = char_dict.get('CH')
                
            elif(char_input == 'h' and my_input[i-1] == 'C'):
                continue

            elif(char_input == 'P' and (my_input[i + 1]) == 'H'):
                tmp[i] = char_dict.get('PH')
                
            elif(char_input == 'H' and my_input[i-1] == 'P'):
                continue
            elif(char_input == 'p' and (my_input[i + 1]) == 'h'):
                tmp[i] = char_dict.get('ph')
                
            elif(char_input == 'h' and my_input[i-1] == 'p'):
                continue
            elif(char_input == 'P' and (my_input[i + 1]) == 'h'):
                tmp[i] = char_dict.get('PH')
                
            elif(char_input == 'h' and my_input[i-1] == 'P'):
                continue
            
            elif(char_input == 'n' and (my_input[i - 1]) == 'o' and char_input == my_input[len(my_input) - 1]):
                tmp[i - 1] = char_dict.get('w')
                tmp[i] = char_dict.get('n')
             
            elif(char_input == 's' and (my_input[i - 1]) == 'i' and char_input == my_input[len(my_input) - 1] ):
                tmp[i - 1] = char_dict.get('h')
                tmp[i] = char_dict.get('s')

            else:
                tmp[i]=char_dict.get(char_input) #if you find char in dict return the value
            
        else :
            tmp[i] = my_input[i] #if char not in dict return it as it is
        
    
    final_list= list(filter(None,tmp)) #filter out None values
    
    
    return final_list


x=[]

#for path in pathlist:
pathlist = Path("COMPLETE_REGIONS").glob('**/*.shp')

for path in pathlist:
    
    x.append(path)

           


for filename in x:
    
    data = gpd.read_file(filename)
    
    #df = pd.DataFrame(data)
    
    i=0
    for row in data.itertuples():
    
        my_input= row.name
        data.at[i , 'GrklshL'] = row.name.lower()
        data.at[i, 'GrklshU'] = row.name.upper()
        data.at[i, 'GreekL'] = ''.join(translate2gr()).lower()
        data.at[i, 'GreekU'] = ''.join(translate2gr()).upper()

        translated = GoogleTranslator(source='auto', target='it').translate(row.name) 
        
        data.at[i, 'Italian'] = translated 
        
        i+=1

    
    data.to_file(filename,encoding='iso-8859-7')
    
