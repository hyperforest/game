import os

def clear():
    os.system('cls')

def bar(char='-', num=40, show=True):
    if show:
        print(char * num)
        return
    return char * num

def wait():
    _ = input()

def wrap(message, clr=False, newline=False):
    if clr:
        clear()
    if newline:
        print()
    
    bar()
    print(message)
    bar()

def simple_query(message):
    return input(f"> {message}: ")

def numbered_query(num):
    if num > 3:
        num = f"1/2/.../{num}"
    else:
        num = [str(x + 1) for x in range(num)]
        num = '/'.join(num)
    return simple_query(f'Choose option ({num})')

def query(header=None, message=None, num=None):
    if header == None:
        header = ''
    else:
        header += '\n'
    print(header)
    
    if num == None:
        assert(message != None)
        return simple_query(message)
    else:
        return numbered_query(num)

def generate_text_box(texts, h_margin=1, v_margin=1,
    h_border='|', v_border='-', h_width=1, v_width=1):
    
    if isinstance(texts, str):
        texts = texts.split('\n')

    inner_width = max(map(len, texts))
    inner_width += (2 * h_margin)
    width = inner_width + (2 * h_width * len(h_border))

    def add_vmargin(text):
        for _ in range(v_margin):
            text += (h_border * h_width)
            text += (' ' * inner_width)
            text += (h_border * h_width)
            text += '\n'
        return text

    # start decorating
    result = '\n'.join([v_border * width] * v_width)
    result += '\n'
    
    result = add_vmargin(result)
    for _ in range(len(texts)):
        l_margin = (inner_width - len(texts[_])) // 2
        r_margin = inner_width - (len(texts[_]) + l_margin)

        result += (h_border * h_width)
        result += (' ' * l_margin)
        result += texts[_]
        result += (' ' * r_margin)
        result += (h_border * h_width)
        result += '\n'
    result = add_vmargin(result)

    result += '\n'.join([v_border * width] * v_width)
    return result

class Prompt:
    def __init__(self, prompt):
        self.prompt = prompt
        self.functions = []
        self.stop = []

        if hasattr(prompt, 'head'):
            self.head = self.prompt.head
        if hasattr(prompt, 'foot'):
            self.foot = self.prompt.foot

    def __call__(self):
        return self

    def head(self):
        pass

    def foot(self):
        pass

    def run(self):
        num_options = len(self.prompt.functions)
        availables = [str(_ + 1) for _ in range(num_options)]

        clear()
        continue_ask = True
        while continue_ask:
            opt = self.prompt.ask()
            if opt not in availables:
                self.repeat(opt)
                continue

            self.head()

            for i in range(num_options):
                if opt == availables[i]:
                    self.prompt.functions[i]()
                    continue_ask = (self.prompt.functions[i]
                        not in self.prompt.stop)
                    done = True
            
            if not continue_ask:
                break
            
            self.foot()

    def repeat(self, opt):
        clear()
        print()              
        print(generate_text_box(
            'OPTION %s IS NOT AVAILABLE!\n'
            'Please choose the other option.' % opt)
        )
