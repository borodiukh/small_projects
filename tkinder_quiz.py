from tkinter import *
import tkinter.messagebox


def get_result():
    tkinter.messagebox.showinfo('Result window', 'Your result is {}/{}'.format(score, 3))


def send_answer_1():
    global score
    answer1 = input1.get()
    if int(answer1) == 45:
        score += 1
    button4.config(state='disabled')


def send_answer_2():
    global score
    answer2 = input2.get()
    if answer2.lower() == 'honey':
        score += 1
    print(answer2)
    button5.config(state='disabled')


def send_answer_3():
    global score
    answer3 = input3.get()
    if answer3.lower() == 'football':
        score += 1
    print(answer3)
    button6.config(state='disabled')


window = Tk()
window.geometry('700x700')
window.title("Quiz Game")
score = 0
number_of_button = 1


question4 = Label(window, text='What is the square root of 2025?', font=20)  # 45
question4.pack()
input1 = Entry(window, font=20)
input1.pack()
button4 = Button(window, text='Send answer', font=20, command=send_answer_1)
button4.pack()

question5 = Label(window, text='Which is the only edible food that never goes bad?', font=20)  # honey
question5.pack()
input2 = Entry(window, font=20)
input2.pack()
button5 = Button(window, text='Send answer', font=20, command=send_answer_2)
button5.pack()

question6 = Label(window, text='What sport is dubbed the "king of sports"?', font=20)  # football
question6.pack()
input3 = Entry(window, font=20)
input3.pack()
button6 = Button(window, text='Send answer', font=20, command=send_answer_3)
button6.pack()

result_button = Button(window, text="Get Result", font=18, command=get_result)
result_button.pack()

window.mainloop()