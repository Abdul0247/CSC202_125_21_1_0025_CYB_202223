# Prime number checker

alphabet = [ "a","b","c" ,"d" ,"e","f","g" ,"h" ,"i","j","k" ,"l" ,"m","n", "o","p" ,"q" ,"r","s","t" ,"u" ,"v","w", "x", "y" ,"z","a","b","c" ,"d" ,"e","f","g" ,"h" ,"i","j","k" ,"l" ,"m","n", "o",
 "p" ,"q" ,"r","s","t" ,"u" ,"v","w","x","y","z"]
direct = input(f"insert 'encode' to encrypt your message, insert 'decode' to decrypt to decrypt ypur message\n").lower()
tech = input("Type Message\n").lower()
skip =int(input("Type your skip number\n"))

def primeNoCheck(start_letter, sum_num, cipherText) :
     end_letter= " "
     for letter in start_letter :
          position = alphabet.index(letter)


          if cipherText == "decode" :
            sum_num *= -1
            new_pos = position + sum_num
            end_letter += alphabet[new_pos]

          elif cipherText == "encode" :
          # new_pos = position + sh_num
           sh_num *= 1
           new_pos = position + sum_num
           end_txt += alphabet[new_pos]

     print(f" The {cipherText}d text is {end_txt}")

primeNoCheck( start_letter= tech, sum_num= skip, cipherText=direct)
  