import tkinter as tk
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
count=1
current_card={}
try:
    df=pandas.read_csv("/home/jenin/Desktop/Fash_card/data/to_learn_words.csv")
except FileNotFoundError:
    df=pandas.read_csv("/home/jenin/Desktop/Fash_card/data/french_words.csv")
    data = df.to_dict(orient="records")
else:
    data = df.to_dict(orient="records")



#animaton
def animation():
    global card_img_back
    canva.itemconfig(image,image= card_img_back)
    english=data_setting()["English"]
    canva.itemconfig(title,text="English",fill="white")
    canva.itemconfig(word,text=english,fill="white")

#data setting
def data_setting():
    global current_card
    number= random.randint(0,len(current_card))
    current_card= data[number]
    return current_card


#button function
def word_change():
    french=data_setting()["French"]
    canva.itemconfig(title,text="French",fill="black")
    canva.itemconfig(word,text=french,fill="black")
    canva.itemconfig(image, image=card_img_front)
    canva.after(3000, animation)

def is_known():
    data.remove(current_card)
    new_data=pandas.DataFrame(data)
    new_data.to_csv("/home/jenin/Desktop"
                    "/Fash_card/data/to_"
                    "learn_words.csv",index=False)


    word_change()


#ui--------------------------------------------------------------
window= tk.Tk()
window.title("Flash Card")
window.config(pady=50,padx=50,bg=BACKGROUND_COLOR)
#images-----------------------------------------------------------
card_img_front= tk.PhotoImage(file="/home/jenin/Desktop/Fash_card"
                                   "/images/card_front.png",)
card_img_back= tk.PhotoImage(file="/home/jenin/Desktop/Fash_card"
                                     "/images/card_back.png" )
#canvas----------------------------------------------------------

canva= tk.Canvas(window,width=800, height=526, highlightthickness=0)
image=canva.create_image(400,263,image= card_img_front)
title =canva.create_text(400,150,text="", font=("Ariel", 40, "italic"))
word = canva.create_text(400,263, text="", font=("Ariel",40, "bold"))
canva.grid(row=0,column=0,columnspan=2)

word_change()
canva.after(5000,animation)


#buttons---------------------------------------------------------------
img_wrong= tk.PhotoImage(file="/home/jenin/Desktop/Fash_card/images/wrong.png")
button_wrong= tk.Button(image=img_wrong, highlightthickness=0,command=word_change)
button_wrong.grid(row=1, column=0)

img_right= tk.PhotoImage(file="/home/jenin/Desktop/Fash_card/images/right.png")
button_right= tk.Button(image=img_right, highlightthickness=0,command=is_known)
button_right.grid(row=1, column=1)



window.mainloop()
