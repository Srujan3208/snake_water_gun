import pyttsx3
import random
engine=pyttsx3.init()

user={"s":-1,"w":0,"g":1}
comp={-1:"snake",0:"water",1:"gun"}

you=input("enter your choice (s=snake,w=water,g=gun):").lower()
computer=random.choice([-1,0,1])
your=user.get(you)
print(f"your choice is={comp.get(your)}",f"\ncomputer choice is={comp.get(computer)}")
if you not in user:
    print("invalid choice")
    engine.say("invalid choice")
    exit()
elif computer==your:
    print("game draw")
    engine.say("game draw")
elif((computer==-1 and your==1)or(computer==0 and your==-1)or(computer==1 and your==0)):
    print("computer won the match")
    engine.say("computer won the match")
else:
    print("you won the match")
    engine.say("you won the match")
engine.runAndWait()    