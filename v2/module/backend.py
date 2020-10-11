from .interface import clear, bar, wait, query, generate_text_box

class AbstractPrompt:
    def build(self):
        self.options = []
        self.stops = []

    def ask(self):
        return query()

class Prompt:
    def __init__(self, prompt):
        self.prompt = prompt
        self.prompt.build()
        if hasattr(prompt, 'head'):
            self.head = self.prompt.head
        if hasattr(prompt, 'foot'):
            self.foot = self.prompt.foot

    def head(self):
        pass

    def foot(self):
        pass

    def run(self):
        num_options = len(self.prompt.options)
        availables = [str(_ + 1) for _ in range(num_options)]

        continue_ask = True
        while continue_ask:
            clear()
            self.head()
            
            opt = self.prompt.ask()
            if opt not in availables:
                self.repeat(opt)
                continue

            for i in range(num_options):
                if opt == availables[i]:
                    self.prompt.options[i]()
                    continue_ask = (self.prompt.options[i]
                        not in self.prompt.stops)
            
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
