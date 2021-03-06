# Find the assignment for this exercise in the 'Assignment2.docx'-file.

import datetime

class WriteFile:

    def __init__(self, filename):
        self.filename = filename

    def write_line(self, single_line):
        with open(self.filename, 'a') as fp:
            fp.write(single_line + '\n')

    def clear_file(self):
        with open(self.filename, 'w') as fp:
            pass

    def write(self):
        raise NotImplementedError

class LogFile(WriteFile):

    def write(self, message):
        time_str = datetime.datetime.now().strftime('%d/%m/%Y at %H:%M')
        self.write_line(time_str + '\t' + message)

class DeLimFile(WriteFile):

    def __init__(self, filename, delim):
        super().__init__(filename)
        self.delim = delim

    def write(self, value_list):
        fields = []
        for elem in value_list:
            if ',' in elem:
                elem = '"' + elem + '"' # Surround elem using double-quotes.
            fields += [elem]
        self.write_line(self.delim.join(fields))


# Testing
log = LogFile('log.txt')
#log.write('The first experiment')

csv = DeLimFile('values.csv', ',')
csv.write(['a', 'b', 'c', 'd'])
csv.write(['12', '2,3', '13', '14', 'Mikko'])
#csv.clear_file()
