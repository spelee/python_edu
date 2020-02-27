

def countLines(name):
    with open(name) as f:
        return len(f.readlines())

def countChars(name):
    with open(name) as f:
        return len(f.read())

def countLines2(name):
    name.seek(0)
    return len(name.readlines())

def countChars2(name):
    name.seek(0)
    return len(name.read())

def test(name):
    print(countLines(name))
    print(countChars(name))

def test2(name):
    with open(name) as f:
      print(countLines2(f))
      print(countChars2(f))


if __name__ == '__main__':
    print(countLines(r'.\mymod.py'))
    print(countChars(r'.\mymod.py'))
