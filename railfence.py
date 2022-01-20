import sys
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Rail Fence Cipher \n By Nitin")
print(ascii_banner)

err = " Usage: python3 railfence.py [command] [text] [key] \n Command: encode - [-e] decode - [-d] help - [-h]"
if len(sys.argv) < 4:
    print(err)
    sys.exit()

result = []
func = sys.argv[1]
txt = sys.argv[2]
key = int(sys.argv[3])


def encrypt(txt, key):
    rail = [['\n' for i in range(len(txt))]
            for j in range(key)]

    dir_down = False
    row, col = 0, 0

    for i in range(len(txt)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down

        rail[row][col] = txt[i]
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    result = []
    for i in range(key):
        for j in range(len(txt)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("".join(result))


def decrypt(cipher, key):
    rail = [['\n' for i in range(len(cipher))]
            for j in range(key)]

    dir_down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        rail[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False

        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1

        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))


if func == '-e':
    print(encrypt(txt, key))

elif func == '-d':
    print(decrypt(txt, key))

else:
    print(err)
