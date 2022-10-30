SetA = {'Kiwi','apple','pine','20','25','28','python','java','AWS','Prince'}


SetA.remove('Kiwi')
print(SetA)
SetA.remove('20')
print(SetA)

print(type(SetA))


SetB = list(SetA)
SetA=SetB.clear()
SetA=set(SetB)
print(SetA)
