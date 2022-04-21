
# File Processor
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



# Encrypt
# ================
def aichin(search_word):
    words = {}
    phrase = search_word.split(' ')
    encrypted = ''
    words = readictionary('enc')
#     with open('a2/dict.txt') as f:
#             lines = [line.rstrip('\n') for line in f]
#     for line in lines:  
#             words[line.lower()] = ctr
#             ctr = ctr + 1
    
    for p in phrase:
            if p.lower() in words:
                position = hex(words.get(p.lower()))
            else:
                    position = p
            encrypted = encrypted + str(position) + '.'        
    return (encrypted)



# Decrypt
# ================
def aichout(search_word2):
        phrase2 = search_word2.split('.')
        words2 = readictionary('dec')
        # ctr2 = 0
        decrypted = ''
        # with open('Work/words.txt') as f2:
        #         lines2 = [line2.rstrip('\n') for line2 in f2]
        # for line2 in lines2:  
        #         words2[ctr2] = line2.lower()
        #         ctr2 = ctr2 + 1

        for p2 in phrase2:
                try:
                        tmp = words2[int(p2, 16)]
                except:
                        tmp = p2
                decrypted = decrypted + str(tmp) + ' '        
        print (decrypted)