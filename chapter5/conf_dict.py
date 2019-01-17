# See the assignment in the 'Assignment4.docx'-file.

class ConfigDict(dict):

    def __init__(self, filename):
        #super().__init__()
        self.filename = filename
        try:
            with open(self.filename) as fp:
                for line in fp:
                    line = line[:-1] # Strip '\n' at the end
                    if line: # Disregard empty lines
                        k, v = line.split('=')
                        super().__setitem__(k, v)
        except FileNotFoundError:
            print(f'File "{self.filename}" does not exist yet.\n'
                  'It will be created when you insert data into the config.')


    def __setitem__(self, key, value):
        super().__setitem__(str(key), str(value))
        print(f'Added {key}: {value}')
        with open(self.filename, 'w') as fp:
            for k, v in self.items():
                fp.write(f'{k}={v}\n')

    def __repr__(self):
        big_str = '\nConfigDict with the following contents:\n\n'
        for k, v in self.items():
            big_str += f'\t{k} = {v}\n'
        return big_str

        
# Testing
cd = ConfigDict('data.txt')
print(cd)
cd['Hannu'] = 'Hopo'
print(cd)
