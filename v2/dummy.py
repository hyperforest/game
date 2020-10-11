from module.backend import Prompt

@Prompt
class dummy:
    def ask():
        _ = input('> Enter char: ')
    def go():
        print('go')
    def stop():
        print('stop')

    options = [go, stop]
    stops = [stop]