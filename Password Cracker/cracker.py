

class PasswordCracker:
    def __init__ (self, hashedPasses, hashedScrapedPasses, scraped_password_library):
        print("\n\t CRACKER: Password Cracking Begun")
        self.hashedPasses = hashedPasses
        self.hashedScrapedPasses = hashedScrapedPasses
        self.scraped_password_library = scraped_password_library
        
        
    def cracker(self):
        
        #print("\nCRACKER: Cracking Passwords")

        hashed_passes_index_list = []
        hash_match_index_list = []
        
        
        password_index_counter = 1
        
        
        for item in self.hashedPasses:
            
            if item in self.hashedScrapedPasses:
                
                hashed_passes_index_list.append(self.hashedPasses.index(item))
                hash_match_index_list.append(self.hashedScrapedPasses.index(item))
                
                print("\nPassword", password_index_counter, "(", item, ")", "=", self.scraped_password_library[self.hashedScrapedPasses.index(item)])
                
                
            else:
                
                pass
        
            password_index_counter += 1
            
        return (hashed_passes_index_list, hash_match_index_list)
    