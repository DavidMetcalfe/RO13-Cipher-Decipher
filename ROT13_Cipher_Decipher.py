import argparse

parser = argparse.ArgumentParser(description="Cipher and decipher ROT13.")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-c', action='store_true',
                   help="ROT13 cipher is applied to normal input text.")
group.add_argument('-d', action='store_true',
                   help="ROT13 text is deciphered to normal text.")

args = parser.parse_args()


def ROT13(text, cipher):
    print(text.translate(cipher))


if args.c:
    CIPHER = str.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
                           "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
    ROT13(input("Please enter text to be ciphered: "), CIPHER)

elif args.d:
    DECIPHER = str.maketrans("NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm",
                             "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz")
    ROT13(input("Please enter text to be deciphered: "), DECIPHER)
