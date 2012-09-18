#!/usr/bin/env python

import string

letters = [('A',".-"),   ('B',"-..."), ('C',"-.-."), ('D',"-.."), ('E',"."),
           ('F',"..-."), ('G',"--."),  ('H',"...."), ('I',".."),  ('J',".---"),
           ('K',"-.-"),  ('L',".-.."), ('M',"--"),   ('N',"-."),  ('O',"---"),
           ('P',".--."), ('Q',"--.-"), ('R',".-."),  ('S',"..."), ('T',"-"),
           ('U',"..-"),  ('V',"...-"), ('W',".--"),  ('X',"-..-"),('Y',"-.--"),
           ('Z',"--..")]

def morse(input):
    if input == "" :
        return [""]
    else:
        return [ letter + remaining
                 for letter, code in letters if input.startswith(code)
                 for remaining in morse(input[len(code):]) ]

def decode_morse(input):
    input = input.replace('I', '-')
    input = input.replace('i', '.')
    text = ""
    for m in input.split(' '):
        for r in morse(m):
            if len(r) == 1:
                text += r
    return text

if __name__ == '__main__':
    print decode_morse('II III iIi iii i ')
