class Countdown:
    def __iter__(self):
        self.curr = 10
        return self
    
    def __next__(self):
        if self.curr > 0:
            self.curr -= 1
            return self.curr
        else:
            raise StopIteration
    
for i in Countdown():
    print(i)