from .interface import clear, wait, query, generate_text_box

class Prompt:
    def __init__(self):
        self.built = False

    def build(self):
        self.built = True
        self.options = []
        self.stops = []

    def ask(self):
        return query()

    def head(self):
        pass

    def foot(self):
        pass

    def run(self):
        clear()
        if not self.built:
            self.build()
            self.num_options = len(self.options)
            self.availables = [str(_ + 1) for _ in range(self.num_options)]

        continue_ask = True
        while continue_ask:
            clear()
            self.head()
            
            opt = self.ask()
            if opt not in self.availables:
                self.repeat(opt)
                continue

            for i in range(self.num_options):
                if opt == self.availables[i]:
                    self.options[i]()
                    continue_ask = (self.options[i] not in self.stops)
            
            if not continue_ask:
                break
            
            self.foot()

    def repeat(self, opt):
        clear()          
        print(generate_text_box(
            'OPTION %s IS NOT AVAILABLE!\n'
            'Please choose the other option.' % opt)
        )
