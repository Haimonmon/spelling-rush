import random #random.shuffle(list_name)
import tkinter as tk
import time 

from gamemode import GameMode
from widget_generator import WidgetGenerator

        
class GameUserInterface: 
    def __init__(self):
        self.game_mode = GameMode()
        self.widget = WidgetGenerator()
   
        self.__window = tk.Tk() #Implement Encapsulation
        self.__width = 450
        self.__height = 530
        self.__window.geometry(f"{self.__width}x{self.__height}") #Fixed Size
        self.__window.maxsize(self.__width,self.__height) 
        self.frame = []
        self.history = [] #Wanna see How Powerfull you are ;) (On Development)
        self.run_time = False #For Timer to aware if time is Running

        self.difficulty_name = None
        self.word = None #word = []
        self.current_index = 0
        self.current_word = None
        self.mistake_cap = None

        self.current_score = 0
        self.current_mistake = 0
        self.time_limit = None
        self.gameplay_effect = None #effect = []

    def display_main_menu(self):
        if self.__width == 620:
            self.__width -= 170
            self.__height +=26
            self.__window.geometry(f"{self.__width}x{self.__height}")
            
        self.__window.title("Spelling Rush | Game Speller Homes ")
        self.widget.clear_frames(self.frame)
      
        home_frame = self.widget.create_frame(None,None,"both",True,None,None,None,None)
        self.frame.append(home_frame)
        self.widget.create_background_img(home_frame,"img\\bg_image(1)-0 (1).png")
        self.widget.create_label(home_frame,None,">>SPELLING  >RUSH","white","#007FFF",20,200,None,None,None)
        self.widget.create_button(home_frame,"START","#FFFAFA","yellowgreen",20,10,None,None,20,self.display_game_modes)
        self.widget.create_button(home_frame,"ABOUT US","#FFFAFA","yellowgreen",20,10,None,None,20,self.display_about_us)
        self.widget.create_button(home_frame,"EXIT","#FFFAFA","yellowgreen",20,10,None,None,20,self.exit)
       
           
    def display_game_modes(self):
        self.widget.clear_frames(self.frame)
        self.__window.title("Spelling Rush | Select GameMode")
        gamemode_frame = self.widget.create_frame(None,None,"both",True,None,None,None,None)
        self.frame.append(gamemode_frame)
        self.widget.create_background_img(gamemode_frame,"img\\gamemode.png")
        self.widget.create_button(gamemode_frame,f"Easy {"\U0001F604"}","#FFFAFA","#B23AEE",20,10,None,None,15,lambda: self.set_gamemode("Easy Mode"))
        self.widget.create_button(gamemode_frame,f"Medium {"\U0001F642"}","#FFFAFA","#B23AEE",20,10,None,None,15,lambda: self.set_gamemode("Medium Mode"))
        self.widget.create_button(gamemode_frame,f"Hard {"\U0001F610"}","#FFFAFA","#B23AEE",20,10,None,None,15,lambda: self.set_gamemode("Hard Mode"))
        self.widget.create_button(gamemode_frame,f"Expert {"\U0001F60E"}","#FFFAFA","#B23AEE",20,10,None,None,15,lambda: self.set_gamemode("Expert Mode"))
        self.widget.create_button(gamemode_frame,f"Back","#FFFAFA","#B23AEE",20,12,None,None,20,self.display_main_menu)

      
    def display_about_us(self):
        self.__window.title("Spelling Rush | About Us")
        self.widget.clear_frames(self.frame)

        about_us_frame = self.widget.create_frame(None,None,"both",True,None,None,None,None)
        self.frame.append(about_us_frame)
        self.widget.create_background_img(about_us_frame,"img\\(Developed By (1).png")
        self.widget.create_button(about_us_frame,"Home","white","#8FA2B3",20,5,None,None,None,self.display_main_menu)

    def set_gamemode(self,gamemode): #Starter Countdown to make the Player Ready and Information about the Level
        if self.__width == 450:
            self.__width += 170
            self.__height -= 26
            self.__window.geometry(f"{self.__width}x{self.__height}") #Fixed Size
            self.__window.maxsize(self.__width,self.__height) 
           
        self.widget.clear_frames(self.frame)
        if self.game_mode.Easy().difficulty == gamemode:
            mode = self.game_mode.Easy()
        elif self.game_mode.Medium().difficulty == gamemode:
            mode = self.game_mode.Medium()
        elif self.game_mode.Hard().difficulty == gamemode:
            mode = self.game_mode.Hard()
        elif self.game_mode.Expert().difficulty == gamemode:
            mode = self.game_mode.Expert()
        
        countdown_frame = self.widget.create_frame("#EEDC82",None,"both",True,None,None,None,None)  
        label = self.widget.create_label(countdown_frame,None,None,"#292421","#EEDC82",100,None,None,None,50)
        loading_line = self.widget.create_label(countdown_frame,None,None,"#292421","#EEDC82",50,None,None,None,None)
        self.frame.append(countdown_frame)

        i = 3
        while i >=0:
            if i == 3:
                label["text"] =f"Ready"
                loading_line["text"] = "● ● ● ● ●"
                loading_line["foreground"] = "#EE2C2C"
                label["foreground"] = "#EE2C2C"
            elif i <= 2:
                label["text"] =f"Get Set"
                loading_line["text"] = "● ● ● "
                loading_line["foreground"] = "#FF7F00"
                label["foreground"] = "#FF7F00"
            if i == 0:
                label["text"] =f"Go!"
                loading_line["text"] = "●"
                loading_line["foreground"] ="#7CFC00"
                label["foreground"] = "#7CFC00"
            self.__window.update()
            time.sleep(1.2)
            i -=1
        
        self.start_game(mode,string = None,string1 = None,check = False)
      
    def start_game(self,game_mode,string,string1,check):
        if check is False: #Setting Up the GameMode
            self.widget.clear_frames(self.frame)
            self.difficulty_name = game_mode.difficulty
            self.word = game_mode.word
            random.shuffle(self.word)
            self.current_word = self.word[self.current_index]
            self.time_limit = game_mode.time_limit
            self.mistake_cap = game_mode.mistake_cap
            self.gameplay_effect = game_mode.gameplay_effects
        else:
            self.next_word(string,string1)

        if game_mode.difficulty == "Easy Mode" or game_mode.difficulty == "Medium Mode":
            font_size = 87
        elif game_mode.difficulty == "Hard Mode":
            font_size = 25
        elif game_mode.difficulty == "Expert Mode":
            font_size = 20
       
       
        self.widget.clear_frames(self.frame)
        self.__window.title(f"Spelling Rush | {game_mode.difficulty}")
        
        board = self.widget.create_frame("yellow",tk.TOP,"both",True,None,None,None,None)
        self.frame.append(board)
        self.widget.create_background_img(board,game_mode.bg_image)
    
        string = self.widget.create_label(board,None,self.current_word,"white","#8E388E",font_size,None,None,None,65)
        str1_entry = self.widget.create_entry(board,23,None,"center",13,None,None,None,"center")
        #button = self.widget.create_button(board,"Rush!","black",None,15,24,2,None,10,lambda: self.check_word(str1_entry,self.current_word,string,game_mode))

        str1_entry.bind("<Button-1>",self.set_cursor(str1_entry))
        str1_entry.bind("<Return>",lambda event: self.check_word(str1_entry,self.current_word,string,game_mode)) # For Enter Key

        status = self.widget.create_frame("#483D8B",tk.BOTTOM,"both",False,None,None,None,45)
        self.frame.append(status)
        self.score_label = self.widget.create_label(status,None,f"Score: {self.current_score}","#FF7F50","#483D8B",15,None,None,20,None)
        self.time_label = self.widget.create_label(status,None,f"Time: {self.time_limit}","#FF7F50","#483D8B",15,None,None,20,None)
        self.star_timer()
        self.mistake_label = self.widget.create_label(status,None,f"Mistake: {self.current_mistake}/{self.mistake_cap}","#FF7F50","#483D8B",15,None,None,20,None)
       
    
    def display_game_over(self,reason):
        if self.__width == 620:
            self.__width -= 170
            self.__height +=26
            self.__window.geometry(f"{self.__width}x{self.__height}")
        
        self.__window.title(f"Spelling Rush | Game Result")
        self.widget.clear_frames(self.frame)
        game_over_frame = self.widget.create_frame("#EEDC82",None,"both",True,None,None,None,None)
        self.frame.append(game_over_frame)
        self.widget.create_label(game_over_frame,None,"Game Over!","#FF3030","#EEDC82",50,None,None,None,2)
        self.widget.create_label(game_over_frame,None,f"( {reason} )","#EE9A00","#EEDC82",23,None,None,None,2)
        self.widget.create_label(game_over_frame,None,f"Highest Score: {self.current_score}","#EE9A00","#EEDC82",20,None,None,None,10)
        self.widget.create_label(game_over_frame,None,f"Mistake Taken: {self.current_mistake}","#EE9A00","#EEDC82",20,None,None,None,10)
        self.widget.create_label(game_over_frame,None,f"Difficulty: {self.difficulty_name}","#EE9A00","#EEDC82",20,None,None,None,10)
        self.widget.create_button(game_over_frame,"Back to Main Menu","#F5F5DC","#E3CF57",20,18,None,None,10,self.stop_game)
        
    def set_cursor(self,entry):
        entry.focus_set()

    
    def star_timer(self):
        if self.run_time is False:
            self.run_time = True
            self.update_label_time()
            self.start_countdown()

    def update_label_time(self):
            self.time_label.config(text=f"Time: {self.time_limit}")
    
    def start_countdown(self):
        if self.run_time:
            self.time_limit-=1
            #print(self.time_limit)
            if self.time_limit <=0:
                self.run_time = False #Stopping the Time or Clock
                self.display_game_over("Youve Run out of Time")
            else:
                self.update_label_time()
                self.__window.after(1000,self.start_countdown) #Recursion

    def stop_game(self): #Reset Mode
        self.difficulty_name = None
        self.word = None #word = []
        self.current_index = 0
        self.current_word = None
        self.run_time = False

        self.current_score = 0
        self.time_limit = None
        self.mistake_cap = None
        self.current_mistake = 0
        self.gameplay_effect = None #effect = []
        self.display_main_menu()

    def check_word(self,string1,str2,string,game_mode):
        
        str1 = string1.get().upper()
        result = self.EditDistance(str1,str2)
     
        if result == 0:
            self.current_score += len(str2) * self.gameplay_effect[0]
            self.time_limit += self.gameplay_effect[1]
            self.score_label.config(text=f"Score: {self.current_score}")
        else:
            self.time_limit -=self.gameplay_effect[1]
            self.current_mistake +=result 
            self.mistake_label.config(text=f"Mistake:" + " " + str(self.current_mistake) + "/" + str(self.mistake_cap))
        self.start_game(game_mode, string, string1, check=True)
        if self.current_mistake >= self.mistake_cap:
            self.run_time = False
            self.display_game_over("Mistake Reached Limit")

    def EditDistance(self,str1,str2): #This will be base from the score and Deduction of the Player
        
        len1 = len(str1)
        len2 = len(str2)
        
        dp = [ [0] * (len2 + 1) for x in range(len1 + 1)]
        
        for i in range(len1 + 1):
            for j in range(len2 + 1):

                if i == 0:
                    dp[i][j] = j
                
                elif j == 0:
                    dp[i][j] = i

                elif str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1]

                else:
                    dp[i][j] = 1 + min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])

        return dp[len1][len2]

    def next_word(self,string,entry):
        self.current_index+=1
        if self.current_index < len(self.word):
            string["text"] = self.current_word
            self.current_word = self.word[self.current_index]
            entry.delete(0,tk.END)

    def exit(self):
        self.__window.destroy()
        print(" Thank You for Gaming :) . . . ")
        
    def run(self):
        self.display_main_menu()
        self.__window.mainloop()
           
            
if __name__ == "__main__":
    game_app = GameUserInterface()
    game_app.run()