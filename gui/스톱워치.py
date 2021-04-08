from tkinter import *
window = Tk()

counter = 0

def clicked():
    global counter
    counter +=1
    label['text']='버튼 클릭 횟수: '+str(counter)
    
def initial():
    global counter
    counter = 0
    label['text']='버튼 클릭 횟수: 0'
    
label=Label(window, text="아직 눌려지지 않음")
label.pack()


button = Button(window, text="증가", command=clicked).pack()
buttonw = Button(window, text="리셋", command=initial).pack()

window.mainloop()