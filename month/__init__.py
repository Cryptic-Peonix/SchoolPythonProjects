def main():
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"

    n = eval(input("Enter a month number 1-12: "))

    pos = (n - 1) *  3

    monthAbbrev = months[pos:pos+3]

    print("THe abbrev is:", monthAbbrev)


def stringstuff():
    message = input("Enter a message: ")
    newMessage = ""

    for c in message:
        newC = chr(ord(c) + 256)
        newMessage += newC

    print("Secret: ", newMessage)


stringstuff()
