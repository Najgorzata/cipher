import sys
import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(new_text, shift1):
        if direction == "decode":
                shift1= -shift1
        for i in range (0,a):
                if text[i] in alphabet:
                        place = alphabet.index(text[i])
                        if (place + shift1) < len(alphabet):
                                new_text[i] = alphabet[place+shift1]
                        else:
                                new_text[i] = alphabet[(place-len(alphabet))+shift1]

        new_text = "".join(new_text)
        
        print(F"The {direction}d text is {new_text}")

end=False

while not end:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction != "encode":
                if direction !="decode":
                        print("Please write encode or decode")
                        sys.exit()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift=shift%len(alphabet)

        text = list(text)
        a=len(list(text))


        ceasar(new_text=text, shift1=shift)

        again= input("Again? Type yes or no:\n")
        if again == "yes": 
               end=False 
        elif again == "no":
                end=True
                print("Goodbye")
        else:
                print("I don't understand")


