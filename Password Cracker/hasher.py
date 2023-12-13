import hashlib

class Hasher:
    def __init__ (self, passwords):
        
        #print("HASHER: Hashing passwords")
        
        self.passwords = passwords
        self.hashedPassList = []
        

    def hasher(self):
        
        for password in self.passwords:
            
            hasher = hashlib.sha256(password.encode('utf-8'))
            hashedValue = hasher.hexdigest()

            self.hashedPassList.append(hashedValue)
            
            
        #print("HASHER: Printing hashed password list: ", self.hashedPassList)
        
        return self.hashedPassList