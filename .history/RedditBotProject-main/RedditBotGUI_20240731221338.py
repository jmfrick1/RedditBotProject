import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from praw_setup import create_reddit_instance
from description_scraper import scrape_descriptions
from image_handler import select_random_image
from imgur_uploader import upload_image_to_imgur
import random

class RedditBotGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Reddit Poster")
        self.geometry("500x700")
        self.configure(bg='lavenderblush')

        self.cute_font = ('Arial', 12)
        self.button_color = '#FFC0CB'
        self.text_bg = 'mintcream'

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Reddit Client ID:", bg='lavenderblush', fg='black', font=self.cute_font).pack()
        self.client_id_entry = tk.Entry(self, width=50, font=self.cute_font)
        self.client_id_entry.pack(pady=5)

        tk.Label(self, text="Reddit Client Secret:", bg='lavenderblush', fg='black', font=self.cute_font).pack()
        self.client_secret_entry = tk.Entry(self, width=50, font=self.cute_font)
        self.client_secret_entry.pack(pady=5)

        tk.Label(self, text="Reddit User Agent:", bg='lavenderblush', fg='black', font=self.cute_font).pack()
        self.user_agent_entry = tk.Entry(self, width=50, font=self.cute_font)
        self.user_agent_entry.pack(pady=5)

        tk.Label(self, text="Reddit Username:", bg='lavenderblush', fg='black', font=self.cute_font).pack()
        self.username_entry = tk.Entry(self, width=50, font=self.cute_font)
        self.username_entry.pack(pady=5)

        tk.Label(self, text="Reddit Password:", bg='lavenderblush', fg='black', font=self.cute_font).pack()
        self.password_entry = tk.Entry(self, width=50, font=self.cute_font, show='*')
        self.password_entry.pack(pady=5)

        tk.Label(self, text="Subreddit Name:", bg='lavenderblush', fg='black', font=self.cute_font).pack()
        self.subreddit_entry = tk.Entry(self, width=50, font=self.cute_font)
        self.subreddit_entry.pack(pady=5)

        tk.Label(self, text="Number of Posts to Scrape:", bg='lavenderblush', fg='black', font=self.cute_font).pack()
        self.num_posts_entry = tk.Entry(self, width=50, font=self.cute_font)
        self.num_posts_entry.pack(pady=5)

        tk.Label(self, text="Time Filter (all, day, week, month, year):", bg='lavenderblush', fg='black', font=self.cute_font).pack()
        self.time_filter_entry = tk.Entry(self, width=50, font=self.cute_font)
        self.time_filter_entry.pack(pady=5)

        tk.Label(self, text="Post Title:", bg='lavenderblush', fg='black', font=self.cute_font).pack()
        self.title_entry = tk.Entry(self, width=50, font=self.cute_font)
        self.title_entry.pack(pady=5)

        tk.Label(self, text="Post Description:", bg='lavenderblush', fg='black', font=self.cute_font).pack()
        self.description_text = scrolledtext.ScrolledText(self, height=6, width=50, bg=self.text_bg, font=self.cute_font)
        self.description_text.pack(pady=5)

        tk.Button(self, text="Load Description", command=self.load_description, bg=self.button_color, font=self.cute_font).pack(pady=5)
        
        self.image_path_var = tk.StringVar(self)
        tk.Button(self, text="Select Image", command=self.select_image, bg=self.button_color, font=self.cute_font).pack(pady=5)
        tk.Label(self, textvariable=self.image_path_var, wraplength=300, bg='lavenderblush', font=self.cute_font).pack(pady=5)

        tk.Button(self, text="Post to Reddit", command=self.post_to_reddit_action, bg=self.button_color, font=self.cute_font).pack(pady=10)

    def load_description(self):
        try:
            client_id = self.client_id_entry.get()
            client_secret = self.client_secret_entry.get()
            user_agent = self.user_agent_entry.get()
            subreddit = self.subreddit_entry.get()
            num_posts = int(self.num_posts_entry.get())
            time_filter = self.time_filter_entry.get()
            descriptions = scrape_descriptions(client_id, client_secret, user_agent, subreddit, num_posts, time_filter)
            chosen_description = random.choice(descriptions).strip()
            self.description_text.delete('1.0', tk.END)
            self.description_text.insert(tk.INSERT, chosen_description)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load description: {e}")

    def select_image(self):
        directory_path = filedialog.askdirectory()
        if directory_path:
            selected_image = select_random_image(directory_path)
            self.image_path_var.set(selected_image)

    def post_to_reddit_action(self):
        try:
            reddit = create_reddit_instance(
                self.client_id_entry.get(),
                self.client_secret_entry.get(),
                self.user_agent_entry.get(),
                self.username_entry.get(),
                self.password_entry.get()
            )
            subreddit_name = self.subreddit_entry.get()
            title = self.title_entry.get()
            body = self.description_text.get('1.0', tk.END).strip()
            image_path = self.image_path_var.get()
            image_url = upload_image_to_imgur(image_path) if image_path else None

            if image_url:
                body += f"\n\n![Image]({image_url})"

            subreddit = reddit.subreddit(subreddit_name)
            subreddit.submit(title, selftext=body)
            messagebox.showinfo("Success", "Post submitted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to post: {e}")

if __name__ == "__main__":
    app = RedditBotGUI()
    app.mainloop()
