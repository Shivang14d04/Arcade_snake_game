from turtle import*
ALIGNMENT = "center"
FONT = ("Courier" , 14 , "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score =0
        with open("data" , "r") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.update_scoreboard()
        self.hideturtle()  # to hide the little turtle that shows up
    def update_scoreboard(self):
        self.write(f"Score : {self.score}   High Score : {self.highscore}", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()
 #   def game_over(self):
 #     self.goto(0,0)
 #      self.write(" GAME OVER " , align= ALIGNMENT, font= FONT)
 # now we are maintaining a high score so don't need to game over

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data" , mode= "w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()


