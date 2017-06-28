# https://www.youtube.com/watch?v=C49kY2DxaSo

name = 'ivan'
print(len(name)) #daljina
surName = 'vankov'
print(name + ' ' + surName) #concatination

for ch in name:
    print(ch) #ciklim bukvi ot stringa
    #print(ch, end='n')
print(name[0])
print(name[-3])
print(name.find('va'))
print(name.find('ov'))
print(name.find('an')) #returns index
print(name.index('iv'))
#print(name.index('ivwww')) #exception
print(name.upper())
print(name.startswith('i'))

randomText = '''
1
2
3
4
5
'''
print(randomText)

'''
multi line comment
1
2
3
4
5
'''
