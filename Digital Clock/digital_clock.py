from tkinter import Label, Tk 
import time

gui = Tk() 
gui.title("Live Digital Clock") 

window_width  = 420 
window_height = 240
screen_width  = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()
window_width_percent  = 0.5
window_height_percent = 0.2

window_placement = str(window_width) + 'x' + str(window_height) + '+' + str(int(screen_width*window_width_percent) - window_width//2) + '+' + str(int(screen_height*window_height_percent) - window_height//2)

gui.geometry(window_placement) 
gui.resizable(False, False)

text_font1 = ("Boulder", 68, 'bold')
text_font2 = ("Boulder", 21, 'bold')

background = "#cdbae8"
foreground = "#363529"
border_width = 25

lbl01 = Label(gui, font=text_font1, bg=background, fg=foreground, bd=border_width)
lbl02 = Label(gui, font=text_font2, bg=background, fg=foreground, bd=border_width)
lbl01.grid(row=0, column=1)
lbl02.grid(row=1, column=1)

def digital_clock(): 
   time_live = time.strftime("%H:%M:%S")
   date_live = time.strftime("%d %B, %Y - %A")
   lbl01.config(text=time_live) 
   lbl02.config(text=date_live)
   lbl01.after(200, digital_clock)

digital_clock()
gui.mainloop()