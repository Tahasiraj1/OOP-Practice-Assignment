class Counter:
    count = 0

    @classmethod
    def display_count(cls):
        cls.count += 1
        return cls.count
    

print(Counter.display_count())
print(Counter.display_count())
