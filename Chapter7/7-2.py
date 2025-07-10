def remove_evenindex(ln):
    return ln[1:7:2]
print(remove_evenindex(['a', 'b', 'c', 'd', 'e', 'f', 'g']) == ['b', 'd', 'f'])
print(remove_evenindex([1, 2, 3, 4, 5]) == [2, 4])

print(remove_evenindex(['a', 'b', 'c', 'd', 'e', 'f', 'g']))
print(remove_evenindex([1, 2, 3, 4, 5]))