from tkinter import *
import sys
from cards import shoe_reset, draw_card

BACKGROUND_COLOR = "#00a300"

root = Tk()
root.config(bg=BACKGROUND_COLOR)
root.geometry("900x500")
root.title("Blackjack")

container_frame = Frame(root, bg=BACKGROUND_COLOR)
container_frame.pack(pady=20)

# Frames for the cards
dealer_frame = LabelFrame(container_frame, text="Dealer", bd=0)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

player_frame = LabelFrame(container_frame, text="Player", bd=0)
player_frame.grid(row=0, column=1, ipadx=20)

# Put the cards in the frames
dealer_label = Label(dealer_frame, text="")
dealer_label.pack(pady=20)

player_label = Label(player_frame, text="")
player_label.pack(pady=20)

# Buttons
shuffle_button = Button(root, text="Shuffle Deck", font=("Helvetica", 12), command=shoe_reset)
shuffle_button.pack(pady=20)

card_button = Button(root, text="Get Cards", font=("Helvetica", 12))
card_button.pack(pady=20)

def main():
  root.mainloop()

main()