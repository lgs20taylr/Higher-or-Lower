import tkinter
import random

def main():
    global a, b, score
    a = random.randint(1,20)
    b = random.randint(1,20)
    score = 0
  
    window = tkinter.Tk()
    window.title("Higher or Lower")
    window.geometry("200x200")
  
    currentNumDisplay = tkinter.Label(window,text=a,font=("Lucida Sans Typewriter","16","bold"))
    currentNumDisplay.grid(column=1,row=0,columnspan=1)

    higherButton = tkinter.Button(window,text="H",font=("Lucida Sans Typewriter","16"),command=lambda: resultDisplay.config(text=str(test(True,currentNumDisplay))))
    higherButton.grid(column=0,row=0,columnspan=1)

    lowerButton = tkinter.Button(window,text="L",font=("Lucida Sans Typewriter","16"),command=lambda: resultDisplay.config(text=str(test(False,currentNumDisplay))))
    lowerButton.grid(column=2,row=0,columnspan=1)

    resultDisplay = tkinter.Label(window,text="Pick Higher (H) or Lower (L).")
    resultDisplay.grid(column=0,row=1,columnspan=4)
  
    window.mainloop()

def swap():
  global a, b
  a = b
  b = random.randint(1,20)
  return a,b
def test(higher,display):
  global a, b, score
  print(a,b,score)
  if (higher and b >= a) or (not higher and b <= a):
    swap()
    display.config(text=a)
    score += 1
    return True
  else:
    return False
if __name__ == "__main__":
    main()