num="10"
guess=""
guess_count=0
guess_limit=3
out_of_guesses=False

print("hello there let the game start")
while guess != num and not(out_of_guesses):
    if guess_count<guess_limit:
        guess=input("enter the guess ")
        guess_count+=1
    else:
        out_of_guesses=True
if out_of_guesses:
            print("you lost")
else:
          print("you won")
   
