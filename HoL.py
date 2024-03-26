from tkinter import *

def main():
    window = Tk()
    window.title("Higher or Lower")
    window.geometry("200x200")

    currentNum = Label(window,"69"font=("Lucida Sans Typewriter","16","italics")))
    currentNum.grid(column=1,row=0,columnspan=1)

    higherButton = Label(window,"H",font=("Lucida Sans Typewriter","16"))

    window.mainloop()


if __name__ == "__main__":
    main()