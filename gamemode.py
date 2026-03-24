
class GameMode:
    def __init__(self):
        self.difficulty = None
        self.time_limit = None
        self.mistake_cap = None # Limited Wrong of the Player
        self.gameplay_effects = None

        self.word = None #word = []
        self.current_index = 0
        self.current_word = None
        self.bg_image = None

    def set_difficulty(self,difficulty,time_limit,mistake_cap,gameplay_effects,word,bg_image):
        self.difficulty = difficulty
        self.time_limit = time_limit
        self.mistake_cap = mistake_cap
        self.gameplay_effects = gameplay_effects
        self.word = word
        self.bg_image = bg_image
        self.current_word = self.word[self.current_index]
      
    def Easy(self):
        word = ["DOG","CAT","SUN","HAT","BED","CUP","CUT","RUN","BALL","FISH","BOOK","TREE","CHAIR","DUCK","DOOR","CAKE","MOON","PEN","STAR","BIRD"]
        gameplay_effects = [200,5] #0: 2x Score points , 5 add and deduct on timee , deduction mistake will depend on edit distance
        bg_image = "img\\bg_image-1-0.png"
        self.set_difficulty("Easy Mode",10,15,gameplay_effects,word,bg_image)
        return self
        
          
    def Medium(self):
        word = ["ELEPHANT","CEREMONY","SYMPHONY","PARALLEL","ADVERTISE","UNLEASH","RUSTED","ILLUMINATE","MAJESTIC","TOLERANCE","AMBULANCE","SYMPATHY","MOMENTUM","MANDOLIN","SPLENDID"]
        gameplay_effects = [250,8] #2.5x Score points , 8 add and deduction on time , deduction mistake will depend on edit distance
        bg_image = "img\\bg_image-1-0.png"
        self.set_difficulty("Medium Mode",15,12,gameplay_effects,word,bg_image)
        return self 
       
       
    def Hard(self):
        word = ["EXQUISITE","ECCENTRICITY","ENTREPRENURIAL","UNPRECEDENTED","IDIOCRACY","MISCHIEVOUS","INQUISITIVE","ACCOMODATE","CONNOISSEUR","EXTRAVAGANT"]
        gameplay_effects = [100,10] #1x Score points , 10 add and deduction time, deduction mistake will depend on edit distance
        bg_image = "img\\bg_image-1-0.png"
        self.set_difficulty("Hard Mode",20,9,gameplay_effects,word,bg_image)
        return self
    
       
    def Expert(self):
        word = ["ANACHRONISTIC",  "OPHTHALMOLOGIST",  "ANTIDISESTABLISHMENTARIANISM",  "PSEUDOPSEUDOHYPOPARATHYROIDISM",  "HIPPOPOTOMONSTROSESQUIPEDALIAN",  "FLOCCINAUCINIHILIPILIFICATION",  "SUPERCALIFRAGILISTICEXPIALIDOCIOUS",  "ANTIESTABLISHMENTARIANISM",  "PNEUMONOULTRAMICROSCOPICSILICOVOLCANOCONIOSIS",  "DICHLORODIPHENYLTRICHLOROETHANE"] # long Words
        gameplay_effects = [75,15] #0.75x Score Points, 15 add and deduction time , deduction will still depend on edit distance
        bg_image = "img\\bg_image-1-0.png"
        self.set_difficulty("Expert Mode",25,5,gameplay_effects,word,bg_image)
        return self

    def restart(self):
        current_mistake = 0
        current_score = 0
        correct_words = 0

if __name__ == "__main__":
    mode = GameMode()
