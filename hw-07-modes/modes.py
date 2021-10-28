# Given a list of three foods that occur multiple times such as:

# L = ['pizza','chocolate','chocolate','eggs','pizza','pizza','pizza','chocolate',...]
# Write a new version of modefast that calculates the most frequent food in the list.

# sort the array and get the last item of the array.

L = ['pizza','chocolate','chocolate','eggs','pizza','pizza','pizza','chocolate']
L1 = []
def modefast(L):
    L.sort()
    return L[-1]

print(modefast(L))

def modefast2(L):
    L.sort() 
    i = 0
    while i < len(L):
        L1.append(L[i])
        i += 1
    return L1[-1]
print(modefast2(L))
