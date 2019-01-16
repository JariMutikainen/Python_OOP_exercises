# Find the assignment for this exercise in the 'Assignment2.docx'-file.

import datetime

class WriteFile:

    def __init__(self, filename):
        self.filename = filename

    def write_line(self, single_line):
        with open(self.filename, 'a') as fp:
            fp.write(single_line + '\n')

    def write(self):
        raise NotImplementedError

class LogFile(WriteFile):

    def write(self, message):
        time_str = datetime.datetime.now().strftime('%d/%m/%Y at %H:%M')
        self.write_line(time_str + '\t' + message)


# Testing
log = LogFile('log.txt')
log.write('The first experiment')
