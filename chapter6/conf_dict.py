# See the assignment in the 'Assignment4.docx'-file.

from sys import exit
from os import access, W_OK

class ConfigKeyError(Exception):
    
    def __init__(self, cd_object, missing_key):
        self.missing_key = missing_key
        self.keys_avail = ()
        for k in cd_object.keys():
            self.keys_avail += (k,)

    def __str__(self):
        return(f'Key "{self.missing_key}" not found.\n'
               f'Available keys: {self.keys_avail}') 

class ConfigDict(dict):

    def __init__(self, filename):
        self.filename = filename
        # Raise an exception if the file is not writeable.
        if not access(self.filename, W_OK):
            raise IOError(f'File "{self.filename}" has no write permission.')
            exit()
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

    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            raise ConfigKeyError(self, key)

    def __repr__(self):
        big_str = '\nConfigDict with the following contents:\n\n'
        for k, v in self.items():
            big_str += f'\t{k} = {v}\n'
        return big_str

        
# Testing
cd = ConfigDict('data.txt')
#print(cd)
#cd['Jari'] = 'Mutikainen'
#print(cd)
#print(cd['Jari'])
print(cd['Kari'])
