# AICH-Encryption
 Encryption Algorithm for All Languages. 

# Installation
sudo pip install aich

# Usage
from a2 import aich

search_word = input('Enter your encryption phrase:')

encrypted = aich.aichin(search_word)

print (encrypted)

search_word = input('Enter your decryption phrase:')

encrypted = aich.aichout(search_word)

print (encrypted)

# Encryption Example
{Inputs: ये है आज़ादी , Outputs: vxfjvwsjxhjvrvjvwgjxhjvhujvocjvrcjvrejvxujvwh}
{Inputs: this is freedom , Outputs: swjugjuvjsrjxhjuvjsrjxhjuujsxjuzjuzjuwjufjud}

# Decryption Example
{Inputs: vxfjvwsjxhjvrvjvwgjxhjvhujvocjvrcjvrejvxujvwh, Outputs: ये है आज़ादी}
{Inputs: swjugjuvjsrjxhjuvjsrjxhjuujsxjuzjuzjuwjufjud , Outputs: this is freedom}

