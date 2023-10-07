S1 = input('Enter first string:')
S2 = input('Enter second string:')

L1 = list(S1)
L2 = list(S2)

L1.sort()
L2.sort()

if L1 == L2:
    print('Yes!These are Anagrams')
else:
    print('These are not Anagrams!')
