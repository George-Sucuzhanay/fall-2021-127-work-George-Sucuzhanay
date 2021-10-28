# Given a list of three foods that occur multiple times such as:

# L = ['pizza','chocolate','chocolate','eggs','pizza','pizza','pizza','chocolate',...]
# Write a new version of modefast that calculates the most frequent food in the list.

#sort the array and get the last item of the array.

L = ['pizza','chocolate','chocolate','eggs','pizza','pizza','pizza','chocolate']
def modefast(L):
    L.sort()
    return L[-1]

print(modefast(L))
