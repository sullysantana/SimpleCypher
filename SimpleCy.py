#The following program can take text from a text file feed it through a custom cypher
#and then place the output in another text file, the program can also de-cypher back
key13 = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u','i':'v', 'j':'w', 'k':'x', 
    'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c','q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 
    'x':'k','y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S','G':'T', 'H':'U', 'I':'V', 
    'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A','O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 
    'V':'I','W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

def rot(stringToProcess, key):
    result = ""

    for char in stringToProcess:
        try:
            result += key[char]
        except Exception:
            result += char
    return result

def DaKey(rotator, letter):
    DaAlphabet = "abcdefghijklmnopqrstuvwxyz"
    shiftAlpha = "abcdefghijklmnopqrstuvwxyz"

    if letter == "e":
        for i in range(0, rotator, 1):
            shiftAlpha = shiftAlpha[1:26]+shiftAlpha[0:1]
    else:
        for i in range(0, rotator, 1):
            shiftAlpha = shiftAlpha[25:26]+shiftAlpha[0:25]

    elDiccionario = {}

    for i in range(0, len(DaAlphabet), 1):
        elDiccionario[DaAlphabet[i]] = shiftAlpha[i]
        elDiccionario[DaAlphabet[i].upper()] = shiftAlpha[i].upper()

    return elDiccionario
#all of the code above does the rotating and matching all the letters accordingly

import argparse
parser = argparse.ArgumentParser(description= "Encrypt/Decrypt text file using ROT-13")

#If there is no -r argument given, the program will default to rotating each letter by 13 letters in the alphabet

group = parser.add_mutually_exclusive_group()
group.add_argument("-e", "--encode", action= "store_true", help= "encode the input file")
group.add_argument("-d", "--decode", action= "store_true", help= "decode the input file")

parser.add_argument("-i", "--inputfile", action= "store", help= "input file")
parser.add_argument("-o", "--outputfile", action= "store", help= "output file")
parser.add_argument("-r", "--rotate", action= "store", help= "rotate amount")

#the proram requires an input text from a txt file with the text to be scrambled and a blank output txt file.
#the CLI command should look something like this: 
#"python SimpleCy.py -i inputfile.txt -o outputfile.txt -e/-d -r {number}"
#'e' meaning 'encode' and 'd' meaning 'decode'
args = parser.parse_args()

if args.encode:
    EorD = "e"
    print("...Encoding file {} and saving to file {}...".format (args.inputfile, args.outputfile))
    print(" ")
    o = open(args.inputfile, 'r')
    stringToCaeser = o.read()
    a = open(args.outputfile, 'a')

    if args.rotate:
        a.write(rot(stringToCaeser, DaKey(int(args.rotate), EorD)))
        print(rot(stringToCaeser, DaKey(int(args.rotate), EorD)))
    else:
        a.write(rot(stringToCaeser, key13))
        print(rot(stringToCaeser, key13))

    o.close()
    a.close()
else:
    EorD = "d"
    print("...Decoding file {} and saving to file {}...".format (args.inputfile, args.outputfile))
    print(" ")
    o = open(args.inputfile, 'r')
    stringToCaeser = o.read()
    a = open(args.outputfile, 'a')

    if args.rotate:
        a.write(rot(stringToCaeser, DaKey(int(args.rotate), EorD)))
        print(rot(stringToCaeser, DaKey(int(args.rotate), EorD)))
    else:
        a.write(rot(stringToCaeser, key13))
        print(rot(stringToCaeser, key13))

    o.close()
    a.close()