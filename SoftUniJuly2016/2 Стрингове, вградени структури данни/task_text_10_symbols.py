inp=input("Въведи поне 10 символа: ")
if  len(inp)<10:
    print('Въведи повече от 9 символа: ')
else:
    print(inp[:10] + "...")