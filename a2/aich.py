

# Encrypt
# ================
def aichin(search_word):
    
    phrase = search_word.split(' ')
    words = {}
    ctr = 0
    encrypted = ''
    with open('a2/dict.txt') as f:
            lines = [line.rstrip('\n') for line in f]
    for line in lines:  
            words[line.lower()] = ctr
            ctr = ctr + 1
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
    words2 = {}
    ctr2 = 0
    decrypted = ''
    with open('a2/dict.txt') as f:
            lines2 = [line2.rstrip('\n') for line2 in f2]
    for line2 in lines2:  
            words2[ctr2] = line2.lower()
            ctr2 = ctr2 + 1
            

    # print (phrase)
    for p2 in phrase2:        
            if (int(p2, 16)):
                    position2 = words2[int(p2, 16)]
            decrypted = decrypted + str(position2) + ' '        
    return (decrypted)