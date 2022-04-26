from a2 import aich

search_word = input('Enter your encryption phrase:') 
encrypted = aich.aichin(search_word)
decrypted = aich.aichout(encrypted) 
print (encrypted)
print ('\n')
print (decrypted)
