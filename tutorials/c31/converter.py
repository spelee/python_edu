import sys

class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        while True:
            data = self.reader.readline()
            if not data: break
            data = self.converter(data)
            self.writer.write(data)

    def converter(self, data):
        assert False, 'converter must be defined'


class DummyReader:
    lines = ['once there was a boy',
             'who lived on a farm',
             'and grew corn.']

    def __init__(self):
        self.i = iter(range(len(DummyReader.lines)))

    def readline(self):
        try:
            idx = next(self.i)
            #print(idx)
            return DummyReader.lines[idx]
        except StopIteration as e:
            return ''

d = DummyReader()
input = d
output = sys.stdout

p = Processor(input, output)
p.process()
