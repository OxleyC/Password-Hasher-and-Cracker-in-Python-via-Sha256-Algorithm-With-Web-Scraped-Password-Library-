from hasher import Hasher
from cracker import PasswordCracker
from scraper import Scraper

class Main:
    def __init__(self, passwordsToCrack):
        
        print("MAIN: Running Main")
        

        if not isinstance(passwordsToCrack, list):
            raise TypeError("Must be a list")
        
        self.passwordsToCrack = passwordsToCrack
        
        
        #    Hash the plain text passwords that are acting as our target hashes (The password hashes we wish to crack)
        hasher_ins = Hasher(passwordsToCrack)
        hashed_passes_to_crack = hasher_ins.hasher()
        
        print("MAIN: HASH INSTANCE 1 EXECUTED")
        
        
        scraper_ins = Scraper()
        scrapedPasswords = scraper_ins.scraper()
        
        print("MAIN: SCRAPED PASSWORDS LIST IS:", scrapedPasswords)
        
        
        hasher_ins_2 = Hasher(scrapedPasswords)
        hashed_scrapedList = hasher_ins_2.hasher()
        
        print("MAIN: HASH INSTANCE 2 EXECUTED")
        
        print("MAIN: Hashed passwords returned is:", hashed_passes_to_crack)
        
        
        cracker_ins = PasswordCracker(hashed_passes_to_crack, hashed_scrapedList, scrapedPasswords)
        
        try:
            matched_target_pass_indexes, matched_library_indexes = cracker_ins.cracker()
            print("\nMAIN: Returning Indexes of Matching Hashes")
            print("\n\tMAIN: Target Passwords Match Indexes:", matched_target_pass_indexes)
            print("\n\tMAIN: Scraped List Match Indexes::", matched_library_indexes)          
            
        except:
            print("No Password was Cracked")
    


#    In a real world application, we would not have the following passwords in plain text
#    The following "passwords" will be entered and hashed for us to use as our targets to crack
passwordsToCrack = ["Password123", "", " ", "test123", "john123"]

main = Main(passwordsToCrack)