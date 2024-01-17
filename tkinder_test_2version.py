from tkinter import *
import tkinter.messagebox


def check_answer():
    global number_of_button
    if number_of_button == 1:
        answer = selected1.get()
        button1.config(state='disabled')
    if number_of_button == 2:
        answer = selected2.get()
        button2.config(state='disabled')
    if number_of_button == 3:
        answer = selected3.get()
        button3.config(state='disabled')
    number_of_button += 1
    if str(answer) in answers:
        tkinter.messagebox.showinfo('Result', 'Correct answer')
        global score
        score += 1
    else:
        tkinter.messagebox.showinfo('Result', 'Incorrect answer')


def get_result():
    tkinter.messagebox.showinfo('Result window', 'Your result is {}/{}'.format(score, 3))


window = Tk()
window.geometry('900x600')
window.title("Quiz Game")
score = 0
number_of_button = 1
answers = ['50', 'Ferdinand Magellan', 'Horse']


quastion1 = Label(window, text="How long is an Olympic swimming pool (in meters)?", font=30)  # 50
quastion1.grid(column=0, row=0)
selected1 = StringVar(value='0')
rad1 = Radiobutton(window, text='40', value='40', font=15, variable=selected1)
rad2 = Radiobutton(window, text='50', value='50', font=15, variable=selected1)
rad3 = Radiobutton(window, text='80', value='80', font=15, variable=selected1)
rad1.grid(column=0, row=1)
rad2.grid(column=0, row=2)
rad3.grid(column=0, row=3)
button1 = Button(window, text="Submit answers", font=18, command=check_answer)
button1.grid(column=0, row=4)


quastion2 = Label(window, text="Who named the Pacific Ocean?", font=25)  # Ferdinand Magellan
quastion2.grid(column=0, row=5)
selected2 = StringVar(value='1')
rad4 = Radiobutton(window, text='Christopher Columbus', value='Christopher Columbus', font=15, variable=selected2)
rad5 = Radiobutton(window, text='Ferdinand Magellan', value='Ferdinand Magellan', font=15, variable=selected2)
rad6 = Radiobutton(window, text='Vasco da Gama', value='Vasco da Gama', font=15, variable=selected2)
rad4.grid(column=0, row=6)
rad5.grid(column=0, row=7)
rad6.grid(column=0, row=8)
button2 = Button(window, text="Submit answers", font=18, command=check_answer)
button2.grid(column=0, row=9)


quastion3 = Label(window, text="Which animal can be seen on the Porsche logo?", font=25)  # horse
quastion3.grid(column=0, row=10)
selected3 = StringVar(value='2')
rad7 = Radiobutton(window, text='Falcon', value='Falcon', font=15, variable=selected3)
rad8 = Radiobutton(window, text='Lion', value='Lion', font=15, variable=selected3)
rad9 = Radiobutton(window, text='Horse', value='Horse', font=15, variable=selected3)
rad7.grid(column=0, row=11)
rad8.grid(column=0, row=12)
rad9.grid(column=0, row=13)
button3 = Button(window, text="Submit answers", font=18, command=check_answer)
button3.grid(column=0, row=14)


button4 = Button(window, text="Get Result", font=18, command=get_result)
button4.grid(column=0, row=15)


window.mainloop()