from tkinter import *
from random import * 

gui = Tk() 
gui.title('Random CC Generator') 

window_width  = 350
window_height = 400
screen_width  = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()
window_width_percent  = 0.5
window_height_percent = 0.5

window_placement = str(window_width) + 'x' + str(window_height) + '+' + str(int(screen_width*window_width_percent) - window_width//2) + '+' + str(int(screen_height*window_height_percent) - window_height//2)

gui.geometry(window_placement) 
gui.resizable(False, False)


# Algorithm Written to Verify the Luhn's Algorithm for Credit Cards

def luhn_algo(cc):
    res, flag = 0, 0
    for i in str(cc)[::-1]: 
        if flag: res += int(i)
        else: res += (int(i)*2)%10 + ((int(i)*2)//10)%10
        flag ^= 1
    
    return res


# Returning the Complete CC Number 
def clickMain(*args):
    digits = 9
    random_cc = randint(int('1' + '0'*(digits-1)), int('9'*digits))

    last_digit = (10 - luhn_algo(random_cc)%10)%10
    actual_cc = str(random_cc) + str(last_digit)

    text1 = 'xxxxxx' + actual_cc
    text2 = 'Generating a Random 10 Digit CC Number'
    text3 = "adhering to Luhn's Algorithm"

    text4 = 'The first 6 digits depend on the CC Company'
    text5 = 'Click to Regenerate a Different CC Number'
    
    canvas.delete('all')
    canvas.create_text(window_width/2, window_height/4, font="cmr 25 bold", fill='#000000', text=text1)
    canvas.create_text(window_width/2, window_height/2, font="cmr 10 bold", fill='#000000', text=text2)
    canvas.create_text(window_width/2, window_height/1.75, font="cmr 10 bold", fill='#000000', text=text3)

    canvas.create_text(window_width/2, window_height/1.3, font="cmr 10 bold", fill='#000000', text=text4)
    canvas.create_text(window_width/2, window_height/1.1, font="cmr 8", fill='#000000', text=text5)

    print(random_cc, actual_cc)

gui.bind('<Button-1>', clickMain)

canvas = Canvas(gui, width=window_width, height=window_height)
canvas.pack()

entry_text = 'Click To Start'
canvas.create_text(window_width/2, window_height/4, font="cmr 30 bold", fill='#000000', text=entry_text)

gui.mainloop()
