#leson here
# https://www.youtube.com/watch?v=f6ji-QcOo_U&t=727s

number = 2
real = 2.2
word = "word"

print (number)
print (real)
print(word)

type (number)
type (real)
type (word)

one, two, three = 1, 'two', 3.0

print(one)
print(two)
print(three)

number = 1
str = 'string'
number = str
print(number)

#importing key words
import keyword
keyword.kwlist
print(keyword.kwlist)

print("We are working with comments") # this is a comment
print("Кирилица???")

'''
Multi
Line
Comment
'''

#Problem for genueses
print(3-3*6+2)

print(2**3) #power of
print(2^3)

#moving a number
#00001 becams 01000
print(1<<3)

#if statemet
passerby_speech='hello'
if passerby_speech == 'hello' or passerby_speech == 'hi':
	print ("Hi, how are you?")

#for continue
for i in range(1,11):
	if i ==5:
		continue
	print(i)

#funcions
def function():
	print("This is our first function!")

function()
function()
function()

def returning():
	return "I am a result!"
result = returning()
print(result)

def mulyival():
	return "this is a result, ", 2
print(mulyival())
 #Exception Handling

#print(5/0)

#fotmatted sting float numbr
fl=16.3569

print("the num is %1.2f " %fl)



