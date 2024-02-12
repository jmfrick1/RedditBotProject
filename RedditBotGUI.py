import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from praw_setup import create_reddit_instance
import random

class RedditBotGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Reddit Poster")
        self.geometry("500x400")
        self.configure(bg='lavenderblush')  # Set a cute background color for the window

        # Apply styles for labels, buttons, and scrolledtext
        self.cute_font = ('Arial', 12)
        self.button_color = '#FFC0CB'  # A cute pink color for buttons
        self.text_bg = 'mintcream'  # Soft color for text background

        # Title Entry
        self.title_label = tk.Label(self, text="Post Title:", bg='lavenderblush', fg='black', font=self.cute_font)
        self.title_label.pack()
        self.title_entry = tk.Entry(self, width=50, font=self.cute_font)
        self.title_entry.pack(pady=5)

        # Description loading and display
        self.description_label = tk.Label(self, text="Post Description:", bg='lavenderblush', fg='black', font=self.cute_font)
        self.description_label.pack()
        self.description_text = scrolledtext.ScrolledText(self, height=6, width=50, bg=self.text_bg, font=self.cute_font)
        self.description_text.pack(pady=5)
        self.load_description_button = tk.Button(self, text="Load Description", command=self.load_description, bg=self.button_color, font=self.cute_font)
        self.load_description_button.pack(pady=5)

        # Image selection (optional for posting text only)
        self.image_path_var = tk.StringVar(self)
        self.select_image_button = tk.Button(self, text="Select Image", command=self.select_image, bg=self.button_color, font=self.cute_font)
        self.select_image_button.pack(pady=5)
        self.image_label = tk.Label(self, textvariable=self.image_path_var, wraplength=300, bg='lavenderblush', font=self.cute_font)
        self.image_label.pack(pady=5)

        # Posting to Reddit
        self.post_button = tk.Button(self, text="Post to Reddit", command=self.post_to_reddit_action, bg=self.button_color, font=self.cute_font)
        self.post_button.pack(pady=10)

    # Your existing methods (load_description, select_image, post_to_reddit_action) remain unchanged

if __name__ == "__main__":
    app = RedditBotGUI()
    app.mainloop()
