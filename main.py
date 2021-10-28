from tkinter import *
import requests


def get_quote():
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, bg="#C7BEA2")

canvas = Canvas(width=300, height=414, bg="#C7BEA2", borderwidth=0, highlightthickness=0)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="", width=250, font=("Arial", 27, "bold"), fill="white")
canvas.grid(row=0, column=0)
get_quote()
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote, bg="#C7BEA2", borderwidth=0)
kanye_button.grid(row=1, column=0)


window.mainloop()
