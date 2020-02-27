import sys

def permute1(seq):
    if not seq:
        return [seq]
        #return seq
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i + 1:]
            for x in permute1(rest):
                res.append(seq[i:i+1] + x)

        return res

def permute2(seq):
    if not seq:
        yield seq
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in permute2(rest):
                yield seq[i:i+1] + x


print('\n'.join(str(i) for i in list(permute2([1, 2, 3]))))
sys.exit()

print(permute1([]))
print('--')
print(permute1([1]))
print('--')
print('\n'.join(str(i) for i in permute1([1, 2])))
print('--')
print('\n'.join(str(i) for i in permute1([1, 2, 3])))
