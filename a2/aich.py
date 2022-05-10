
# File Processor
# ==============
def readictionary(handle):
    filename = 'a2/dict.txt'
    words = {}
    ctr = 0
    with open(filename) as f:
        lines = [line.rstrip('\n') for line in f]
    for line in lines:  
                if(handle == 'enc'):
                        words[line.lower()] = ctr
                else:
                        words[ctr] = line.lower()

                ctr = ctr + 1
    return words


# Word Finder
# ==============
def find_word(start_letter, end_letter, length):
        words = readictionary('enc')
        rt = [w for w in words if str(w)[0].lower() == start_letter.lower() and str(w)[len(w) - 1].lower() == end_letter.lower() and len(w) == length]
        return rt

# Encrypt
# ================
def aichin(phrase):
        map_list = get_list()
     
        hex_string = '_'.join(format(ord(x), 'x') for x in phrase)
        # print (f1)
        encrypted_value = ""
        for letter_in_hex in hex_string:
                if letter_in_hex.isalpha() == True:
                        encrypted_value = encrypted_value + "" + map_list[letter_in_hex]
                elif  letter_in_hex.isalpha != True and letter_in_hex != '_':
                        encrypted_value = encrypted_value + "" + map_list[letter_in_hex]
                else:
                        encrypted_value = encrypted_value + "" + map_list[letter_in_hex]
        # print (str(p1))
        return (encrypted_value)



# Decrypt
# ================
def aichout(phrase):
        phrase = str(phrase)
        map_list = get_list()
        
        map_list = {v: k for k, v in map_list.items()}
        
        words_in_phrase = phrase.split(list(map_list.keys())[-1])
        # print (l)
         
        p2 = []
        hexlib = ['a', 'b', 'c', 'd', 'e', 'f']
        for each_word in words_in_phrase:
            # print(l2)
            p1 = "" 
            for letter_in_word in each_word:
                letter_in_word = str(letter_in_word)
                if letter_in_word not in hexlib and map_list[letter_in_word] != '':
                    p1 = p1 + "" + map_list[letter_in_word]
                else:
                    p1 = p1 + "" + letter_in_word
            p2.append(format(int(p1, 16), 'd'))
        # print (p2)
        
        decrypted_value = ''.join(chr(int(x)) for x in p2)
        # print (str(f1))
        return decrypted_value

# Mapper
def get_list():
    l = {'1': {'0':'h', '1':'o', '2':'x', '3':'r', '4':'w', '5':'z', '6':'u', '7':'s', '8':'g', '9':'v', '_':'j'},
                '2': {'0':'म', '1':'ण', '2':'य', '3':'क', '4':'न', '5':'ष', '6':'द', '7':'ख', '8':'प', '9':'श', 'a':'ह','b':'ज','c':'ट','d':'त','e':'ए','f':'ग', '_':'फ'}}

    return l['2']

# Mapping Key Date Handler
def date_add(ini_date):
    y = 0
    l = []
    for id in ini_date:
        y = y + int(id)
    
    
    while len(str(y)) > 1:
        x = 0
        for y1 in str(y):
            x = x + int(y1)
            # print (x)
        y = x

        return y