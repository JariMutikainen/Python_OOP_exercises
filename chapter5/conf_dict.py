# See the assignment in the 'Assignment4.docx'-file.

class ConfigDict(dict):

    def __init__(self, filename):
        self.filename = filename
        try:
            with open(self.filename) as fp:
                for line in fp:
                    line = line[:-1] # Strip '\n' at the end
                    if line: # Disregard empty lines
                        k, v = line.split('=')
                        print(k + '---' + v)
        except FileNotFoundError:
            print(f'File "{self.filename}" does not exist yet.\n'
                  'It will be created when you insert data into the config.')


# Testing
cd = ConfigDict('data.txt')
