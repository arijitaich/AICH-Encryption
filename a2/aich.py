
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
        l = get_list()
     
        f1 = '_'.join(format(ord(x), 'x') for x in phrase)
        # print (f1)
        p1 = ""
        for s in f1:
                if s.isalpha() == True:
                        p1 = p1 + "" + s
                elif  s.isalpha != True and s != '_':
                        p1 = p1 + "" + l[s]
                else:
                        p1 = p1 + "" + l[s]
        # print (str(p1))
        return (p1)



# Decrypt
# ================
def aichout(phrase):
        phrase = str(phrase)
        l = get_list()
        
        l = {v: k for k, v in l.items()}
        
        l1 = phrase.split("j")
        # print (l)
         
        p2 = []
        hexlib = ['a', 'b', 'c', 'd', 'e', 'f']
        for l2 in l1:
            # print(l2)
            p1 = "" 
            for s in l2:

                if s not in hexlib and l[s] != '':
                    p1 = p1 + "" + l[s]
                else:
                    p1 = p1 + "" + s
            p2.append(format(int(p1, 16), 'd'))
        # print (p2)
        
        f1 = ''.join(chr(int(x)) for x in p2)
        # print (str(f1))
        return f1

# Mapper
def get_list():
    l = {'1': {'0':'h', '1':'o', '2':'x', '3':'r', '4':'w', '5':'z', '6':'u', '7':'s', '8':'g', '9':'v', '_':'j'}}
    return l['1']

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