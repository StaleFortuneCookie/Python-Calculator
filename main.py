from tkinter import *

# create root window
root = Tk()

# window title
root.title("Calculator")
# window dimensions
root.geometry('350x280')

# label to root window
welcomeLbl = Label(root, text = "Welcome to the Python Calculator.\nThis is a calculator made by StaleFortuneCookie (Dino).", 
            anchor="w", justify="left", font=('Arial', 8))

welcomeLbl.grid(row=0,column=0, sticky="w")

displayLbl= Label(root, text="", anchor="center", justify="center")
displayLbl.grid(row=7, column=0,)


# function for add
def addFunc(number1, number2):
    num1=number1.cget('text')
    num2=number2.cget('text')
    print(int(num1) + int(num2))

def getNumber(button):
    number=button.cget('text')
    number=int

def clicked(button):
    number=button.cget('text')
    print(number)

# num 0
numZeroBtn= Button(root, text="0", textvariable="num", anchor="w", justify="center")
numZeroBtn.grid(row=1,column=0, sticky="w",)
numZeroBtn.config(command=lambda: clicked(numZeroBtn))
numZeroBtn.config(command=lambda: displayLbl.config(text=numZeroBtn.cget("text")))

# number 1
numOneBtn= Button(root, text="1", anchor="center", justify="center",)   
numOneBtn.grid(row=1,column=0)
numOneBtn.config(command=lambda: clicked(numOneBtn))
numOneBtn.config(command=lambda: displayLbl.config(text=numOneBtn.cget("text")))

#number 2
numTwoBtn= Button(root, text="2", anchor="e", justify="center",)
numTwoBtn.grid(row=1, column=0, sticky="e")
numTwoBtn.config(command=lambda: clicked(numTwoBtn))

# number 3
numThreeBtn= Button(root, text="3", anchor="w", justify="center")
numThreeBtn.grid(row=2, column=0, sticky="w")
numThreeBtn.config(command=lambda: clicked(numThreeBtn))

# number 4
numFourBtn= Button(root, text = "4", anchor="center", justify="center",)   
numFourBtn.grid(row=2,column=0)
numFourBtn.config(command=lambda: clicked(numFourBtn))

#number 5
numFiveBtn= Button(root, text = "5", anchor="e", justify="center",)
numFiveBtn.grid(row=2, column=0, sticky="e")
numFiveBtn.config(command=lambda: clicked(numFiveBtn))

# number 6
numSixBtn= Button(root, text="6", anchor="w", justify="center")
numSixBtn.grid(row=3, column=0, sticky="w")
numSixBtn.config(command=lambda: clicked(numSixBtn))

# number 7
numSevenBtn= Button(root, text = "7", anchor="center", justify="center",)   
numSevenBtn.grid(row=3,column=0,)
numSevenBtn.config(command=lambda: clicked(numSevenBtn))

# number 8
numEightBtn= Button(root, text = "8", anchor="e", justify="center",)
numEightBtn.grid(row=3, column=0, sticky="e")
numEightBtn.config(command=lambda: clicked(numEightBtn))

# number 9
numNineBtn= Button(root, text="9", anchor="center", justify="center",)
numNineBtn.grid(row=4, column=0,)
numNineBtn.config(command=lambda: clicked(numNineBtn))

# add button
addBtn= Button(root, text="Add", anchor="w", justify="center" )
addBtn.grid(row=5, column=0, sticky="w")
addBtn.config(command=lambda: addFunc(numOneBtn, numThreeBtn))

# subtract button
subtractBtn= Button(root, text="Subtract", anchor="center", justify="center" )
subtractBtn.grid(row=5, column=0)


# add button
multiplyBtn= Button(root, text="Multiply", anchor="e", justify="center" )
multiplyBtn.grid(row=5, column=0, sticky="e")

# execute tkinter
root.mainloop()