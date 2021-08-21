class RemoteController():
    def __init__(self):
        self.channels = ["a", "b", "c", "d", "e", "f", "g", "h"]
        self.channelIndex = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.channelIndex += 1
        if self.channelIndex == len(self.channels):
            raise StopIteration
        return self.channels[self.channelIndex]


rc = RemoteController()
itr = iter(rc)
print(next(itr))

print(rc.channels)
