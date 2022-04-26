from a2.aich import aichin, aichout

search_word = input('Enter your encryption phrase:') 
encrypted = aichin(search_word)
decrypted = aichout(encrypted) 
print (encrypted)
print ('\n')
print (decrypted)
