import tkinter
import random

def main():
    global a, b, score, prevNums
    a = random.randint(1,20)
    b = random.randint(1,20)
    score = 0
    prevNums = [a]

    window = tkinter.Tk()
    window.title("Higher or Lower")
    window.geometry("200x200")
  
    currentNumDisplay = tkinter.Label(window,text=a,font=("Lucida Sans Typewriter","16","bold"))
    currentNumDisplay.grid(column=1,row=0,columnspan=1)

    higherButton = tkinter.Button(window,text="H",font=("Lucida Sans Typewriter","16"),command=lambda: resultDisplay.config(text=str(test(True,currentNumDisplay,streakDisplay,prevNumsDisplay))))
    higherButton.grid(column=0,row=0,columnspan=1)

    lowerButton = tkinter.Button(window,text="L",font=("Lucida Sans Typewriter","16"),command=lambda: resultDisplay.config(text=str(test(False,currentNumDisplay,streakDisplay,prevNumsDisplay))))
    lowerButton.grid(column=2,row=0,columnspan=1)

    resultDisplay = tkinter.Label(window,text="Pick Higher (H) or Lower (L).")
    resultDisplay.grid(column=0,row=1,columnspan=4)

    streakDisplay = tkinter.Label(window,text="Streak:0")
    streakDisplay.grid(column=0,row=2,columnspan=4)

    prevNumsDisplay = tkinter.Label(window,text=", ".join(map(str, prevNums)))
    prevNumsDisplay.grid(column=0,row=3,columnspan=4)
  
    window.mainloop()

def swap():
  global a, b, prevNums
  prevNums.append(b)
  a = b
  b = random.randint(1,20)
  

def test(higher,display,sDisplay,pDisplay):
  global score, prevNums
  correct = check(higher,display)
  sDisplay.config(text=f"Streak:{score}")
  pDisplay.config(text=", ".join(map(str, prevNums)))
  if correct:
     return "Correct!"
  else:
     return "Incorrect."

def check(higher,display):
    global a, b, score
    print(a,b,score)
    if (higher and b >= a) or (not higher and b <= a):
        swap()
        display.config(text=a)
        score += 1
        return True 
    else:
        score = 0
        return False
if __name__ == "__main__":
    main()