import os
import sys

LOGO = '''
  ____                  _     _       
 |  _ \ _   _ _ __ ___ | |__ | | ___  
 | |_) | | | | '_ ` _ \| '_ \| |/ _ \ 
 |  _ <| |_| | | | | | | |_) | |  __/ 
 |_| \_\\\\__,_|_| |_| |_|_.__/|_|\___| 
                                      
                    (c) hyperforest 2020
'''

HOME = '''
(1) New game
(2) Continue
(3) Exit
'''

CHOOSE_ROLE = '''
------------------------------
|      Choose Your Role      |
------------------------------

(1) Knight
'''

BATTLE = '''
(1) Player details
(2) Player location
(3) Quit battle
'''

_CLEAR_ = 'cls' if sys.platform == "win32" else 'clear'

def clear():
    os.system(_CLEAR_)

def wait():
    _ = input()

def simple_query(message=None, return_int=False):
    if message == None:
        message = 'Choose option'

    result = input(f"> {message}: ")
    if return_int:
        return int(result)
    return result

def numbered_query(message=None, num=2, return_int=False):
    if message == None:
        message = 'Choose option'

    if num > 3:
        num = f"1/2/.../{num}"
    else:
        num = [str(x + 1) for x in range(num)]
        num = '/'.join(num)

    message = f'{message} ({num})'
    return simple_query(message, return_int=return_int)

def query(message=None, header=None, num=None, return_int=False):
    if header != None:
        print(header)

    if num == None:
        return simple_query(message=message, 
            return_int=return_int)
    else:
        return numbered_query(num=num, 
            return_int=return_int)

def generate_text_box(texts, h_margin=5, v_margin=1, h_width=1, v_width=1,
    align='center'):
    if isinstance(texts, str):
        texts = texts.split('\n')

    inner_width = max(map(len, texts))
    inner_width += (2 * h_margin)
    width = inner_width + (2 * h_width)

    def add_vmargin(text):
        for _ in range(v_margin):
            text += ('|' * h_width)
            text += (' ' * inner_width)
            text += ('|' * h_width)
            text += '\n'
        return text

    # start decorating
    result = '\n'.join(['-' * width] * v_width)
    result += '\n'
    
    result = add_vmargin(result)
    for _ in range(len(texts)):
        if align == 'center':
            l_margin = (inner_width - len(texts[_])) // 2
            r_margin = inner_width - (len(texts[_]) + l_margin)
        elif align == 'left':
            l_margin = 1
            r_margin = inner_width - len(texts[_]) - 1

        result += ('|' * h_width)
        result += (' ' * l_margin)
        result += texts[_]
        result += (' ' * r_margin)
        result += ('|' * h_width)
        result += '\n'
    result = add_vmargin(result)

    result += '\n'.join(['-' * width] * v_width)
    return result + '\n'
