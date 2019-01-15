# See the assignment in the pdf-file 'Assignment1.docx'.
class MaxSizeList:
    def __init__(self, max_size):
        self.max_size = max_size
        self.string_list = []

    def push(self, string):
        '''Pushes a new string into the list. In the case of an list overflow
           the oldest element of the list is discarded.'''
        if len(self.string_list) < self.max_size:
            self.string_list += [string]
        else:
            self.string_list = self.string_list[1:] + [string] 
        print(f"Pushed '{string}' into string_list.\n"
              f"New list is {self.string_list}")

    def get_list(self):
        return self.string_list

# Testing

a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")

b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")

print(a.get_list())
print(b.get_list())
