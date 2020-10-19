from .interface import clear, wait, query, generate_text_box

class Prompt:
    def __init__(self):
        self.built = False
        self.continue_ask = True

    def build(self):
        self.built = True
        self.options = []

    def ask(self):
        return query()

    def run(self):
        clear()
        self.continue_ask = True
        if not self.built:
            self.build()
            self.num_options = len(self.options)
            self.availables = [str(_ + 1) for _ in range(self.num_options)]
        
        while self.continue_ask:
            clear()
            
            opt = self.ask()
            if opt not in self.availables:
                self.repeat(opt)
                continue

            for i in range(self.num_options):
                if opt == self.availables[i]:
                    self.options[i]()
            
            if not self.continue_ask:
                break

    def repeat(self, opt):          
        print(generate_text_box(
            'OPTION %s IS NOT AVAILABLE!\n'
            'Please choose the other option.' % opt)
        )
        wait()
