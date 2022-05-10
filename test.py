from a2 import aich
#  aich.aichin(search_word)



search_word = input('Enter your encryption phrase:') 
encrypted = aich.aichin(search_word)
decrypted = aich.aichout(encrypted) 
print ('')
print ('AICH Encrypted Value: ')
print (encrypted)
print ('')
print ('AICH Decrypted Value: ')
print (decrypted)

# Test For All Printable Ascii Characters.

# Test For All Words Present Inside The Dictionary.

# Test For All Hindi Characters As 2nd Language Testing.