#!/usr/bin/env python3

import mathpix
import json
import os

#
# Example using Mathpix OCR with multiple result formats. We want to recognize
# both math and text in the image, so we pass the ocr parameter set to
# ['math', 'text']. This example returns the LaTeX text format, which
# starts in text mode instead of math mode, the latex_styled format,
# the asciimath format, and the mathml format. We define custom
# math delimiters for the text result so that the math is surrounded
# by dollar signs ("$").
#

#array to store the LaTex code into a final string
latex_code=[]

r1 = mathpix.latex({
    'src': mathpix.image_uri('new_rotated1.png'),
    'ocr': ['math', 'text'],
    'skip_recrop': True,
    'formats': ['text', 'latex_styled'],
    'format_options': {
        'text': {
            'transforms': ['rm_spaces', 'rm_newlines'],
            'math_delims': ['$', '$']
        },
        'latex_styled': {
            'transforms': ['rm_spaces'],
            'math_delim': ['$$','$$']}
    }
})
r2 = mathpix.latex({
    'src': mathpix.image_uri('new_rotated2.png'),
    'ocr': ['math', 'text'],
    'skip_recrop': True,
    'formats': ['text', 'latex_styled'],
    'format_options': {
        'text': {
            'transforms': ['rm_spaces', 'rm_newlines'],
            'math_delims': ['$', '$']
        },
        'latex_styled': {
            'transforms': ['rm_spaces'],
            'math_delim': ['$$','$$']}
    }
})
r3 = mathpix.latex({
    'src': mathpix.image_uri('new_rotated3.png'),
    'ocr': ['math', 'text'],
    'skip_recrop': True,
    'formats': ['text', 'latex_styled'],
    'format_options': {
        'text': {
            'transforms': ['rm_spaces', 'rm_newlines'],
            'math_delims': ['$', '$']
        },
        'latex_styled': {
            'transforms': ['rm_spaces'],
            'math_delim': ['$$','$$']}
    }
})
r4 = mathpix.latex({
    'src': mathpix.image_uri('new_rotated4.png'),
    'ocr': ['math', 'text'],
    'skip_recrop': True,
    'formats': ['text', 'latex_styled'],
    'format_options': {
        'text': {
            'transforms': ['rm_spaces', 'rm_newlines'],
            'math_delims': ['$', '$']
        },
        'latex_styled': {
            'transforms': ['rm_spaces'],
            'math_delim': ['$$','$$']}
    }
})

#store the JSON object latex_styled into a variable so that we can replace key characters
answer1=json.dumps(r1['latex_styled'], indent=4, sort_keys=True)
answer2=json.dumps(r2['latex_styled'], indent=4, sort_keys=True)
answer3=json.dumps(r3['latex_styled'], indent=4, sort_keys=True)
answer4=json.dumps(r4['latex_styled'], indent=4, sort_keys=True)

#store all of the LaTex code into a list, concat the strings into one giant string
#intial code prints correct LaTex code, except for an extra '\' for every '\'
latex_code.append(answer1.replace("\\\\", "\\").replace('"',""))
latex_code.append(answer2.replace("\\\\", "\\").replace('"',""))
latex_code.append(answer3.replace("\\\\", "\\").replace('"',""))
latex_code.append(answer4.replace("\\\\", "\\").replace('"',""))

#print the string from the list
print(*latex_code)

#print out the final string into a text file incase of situation
with open('answer.txt', 'w') as f:
    for item in latex_code:
        f.write("%s\n" % item)

#print(answer1.replace("\\\\", "\\").replace('"',""))
#print('\n')
#print(answer2.replace("\\\\", "\\").replace('"',""))
#print('\n')
#print(answer3.replace("\\\\", "\\").replace('"',""))
#print('\n')
#print(answer4.replace("\\\\", "\\").replace('"',""))
#print('\n')

#remove the partitioned pieces of math paper
os.remove('new_rotated1.png')
os.remove('new_rotated2.png')
os.remove('new_rotated3.png')
os.remove('new_rotated4.png')