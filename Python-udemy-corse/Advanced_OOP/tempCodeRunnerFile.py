def __next__(self):
        try:
            return self.cores.pop()
        except:
            raise StopIteration()