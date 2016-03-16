import sys

#Library used for converting letters
alphaDic = {
	'A': 'ALPHA' , 'B': 'BRAVO'   , 'C': 'CHARLIE',
	'D': 'DELTA' , 'E': 'ECHO'    , 'F': 'FOXTROT',
	'G': 'GOLF'  , 'H': 'HOTEL'   , 'I': 'INDIA',
	'J': 'JULIET', 'K': 'KILO'    , 'L': 'LIMA',
	'M': 'MIKE'  , 'N': 'NOVEMBER', 'O': 'OSCAR',
	'P': 'PAPA'  , 'Q': 'QUEBEC'  , 'R': 'ROMEO',
	'S': 'SIERRA', 'T': 'TANGO'   , 'U': 'Uniform',
	'V': 'VICTOR', 'W': 'WHISKEY' , 'X': 'X-RAY',
	'Y': 'YANKEE', 'Z': 'ZULU'
}

#Library for conververtin Numbers
numDic = {
	'0': 'ZEOR', '1':'ONE' , '2': 'TWO'  , '3': 'THREE', '4':'FOUR',
	'5': 'FIVE', '6': 'SIX', '7': 'SEVEN', '8': 'EIGHT', '9':'NINE'
}

"""
convertString(input)

Takes in an input string and calls dictionaries to translate each char in string.
Uses global dictionaries defined above. Returns string in format:
	"ALPHA BETA DELTA ONE TWO THREE ... ",
	if a non letter is put in then
"""
def convertString(stringInput):
	returnString = ""
	for char in stringInput:
		if(char.isalpha()):
			returnString += alphaDic[char.upper()] + "  "
		else:
			if(char.isdigit()):
				returnString += numDic[char] + "  "
			else:
				returnString += char + "  "

	return returnString


"""
main()
A function that checks for command line arguments and either initiates an input loop,
	or translates command line arguments into NATO phonetic alphabet.

Takes either input and called convertString to handle the conversion.

Capable of interpretting an infinite amount of command line arguments,
	and will loop over input infinitely until it reaches the end of input.

"""
def main():
	#Run input loop if no arguments are given
	if(len(sys.argv) == 1):
		while(True):
			print("Enter input to be translated, or 'exit'")
			stringInput = input("Input: ")
			if(stringInput == "exit"):
				break
			else:
				#call phonetic alphabet
				print( convertString(stringInput) )

	#Translate program command line arguments
	else:
		for x in range(1, len(sys.argv)):
			print( convertString( sys.argv[x] ) )

main()
