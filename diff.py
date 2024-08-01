from colors import Bg_Colors
class Diff:
    def __init__(self, filename):
        self.data = ''
        self.old = ''
        self.new = ''
        self.bg_colors = Bg_Colors()

        self.load_file(filename)
        self.replace('\\n', '\n')

    def load_file(self, filename):
        with open(filename, 'r') as f:
            self.data = f.read()

        self.replace('\\n', '\n')

    def replace(self, old, new):
        self.data = self.data.replace(old, new)

    def show_old(self):
        print('Old:')
        self.red(self.old)

    def show_new(self):
        print('New:')
        self.green(self.new)

    def save_file(self, filename):

        with open(f'{filename}', 'w') as f:
            f.writelines(self.data)
    
    def red(self, text):
        return self.bg_colors.get_bg_color('FAIL') + text + self.bg_colors.get_bg_color('ENDC')
    
    def green(self, text):
        return self.bg_colors.get_bg_color('OKGREEN') + text + self.bg_colors.get_bg_color('ENDC')

    def show_together(self):
        temp_data = self.data.split('\n')

        for line in temp_data:
            if line.startswith('-'):
                print(self.red(line))
            elif line.startswith('+'):
                print(self.green(line))
            else:
                print(line)