import sys
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Caesar Cipher \n By Nitin")
print(ascii_banner)

err = " Usage: python3 Caesarcipher.py [command] [text] [shifts] \n Command: encode - [-e] decode - [-d] help - [-h]"
if len(sys.argv) < 4:
    print(err)
    sys.exit()

result = ""
func = sys.argv[1]
txt = sys.argv[2]
s = int(sys.argv[3])

if func == '-e':
    for i in range(len(txt)):
        char = txt[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)

        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    print("Text  : " + txt)
    print("Shift : " + str(s))
    print("Result: " + result)


elif func == '-d':
    s = 26 - s
    for i in range(len(txt)):
        char = txt[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)

        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    print("Text  : " + txt)
    print("Shift : " + str(s))
    print("Result: " + result)

else:
    print(err)
