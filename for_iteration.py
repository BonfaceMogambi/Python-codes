class MyNumbers:
    def __iter__(self):
        self.numbers = 0
        return self
    def __next__(self):
        if self.numbers <= 10:
            result = self.numbers
            self.numbers += 1
            return result
        else:
            raise StopIteration

myClass = MyNumbers()
myIterator = iter(myClass)

for result in myIterator:
    print(result)  # Output: 0, 1, 2, ..., 10