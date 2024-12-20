import tkinter as tk
from tkinter import messagebox
import pyshorteners

class UrlShortenerApp:
    def __init__(self, master):
        self.master = master
        master.title("URL Shortener")
        master.configure(bg="black")
        master.geometry("500x200")

        self.about_window = None  # Initialize about window attribute

        self.create_widgets()

    def create_widgets(self):
        # About button
        self.about_button = tk.Button(self.master, text="About", command=self.show_about, bg="gray", fg="white")
        self.about_button.place(x=10, y=10)

        # Create and place the long URL entry field
        self.url_label = tk.Label(self.master, text="Enter the URL to shorten:", bg="black", fg="white")
        self.url_label.pack(pady=10)
        self.url_entry = tk.Entry(self.master, width=50)
        self.url_entry.pack(pady=5)

        # Create and place the shortened URL entry field
        self.shortened_url_label = tk.Label(self.master, text="Shortened URL:", bg="black", fg="white")
        self.shortened_url_label.pack(pady=10)
        self.shortened_url_entry = tk.Entry(self.master, width=50)
        self.shortened_url_entry.pack(pady=5)

        self.shorten_button = tk.Button(self.master, text="Shorten URL", command=self.shorten_url)
        self.shorten_button.pack(pady=20)

    def shorten_url(self):
        long_url = self.url_entry.get()
        if not long_url:
            messagebox.showerror("Error", "Please enter a URL to shorten")
            return

        try:
            type_tiny = pyshorteners.Shortener()
            short_url = type_tiny.tinyurl.short(long_url)
            self.shortened_url_entry.delete(0, tk.END)
            self.shortened_url_entry.insert(0, short_url)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def show_about(self):
        # Check if about window is already open
        if self.about_window is None:
            # Create the about window
            x = self.master.winfo_x()
            y = self.master.winfo_y()

            self.about_window = tk.Toplevel(self.master)
            self.about_window.title("About")
            self.about_window.geometry(f"300x100+{x + 520}+{y}")
            self.about_window.configure(bg="black")

            about_label = tk.Label(self.about_window, text="Created by: Hallucination", bg="black", fg="white", font=("Helvetica", 12))
            about_label.pack(expand=True, pady=20)

            self.about_window.resizable(False, False)
            self.about_window.attributes("-toolwindow", 1)  # Hide minimize and maximize buttons

            self.about_window.protocol("WM_DELETE_WINDOW", self.on_about_window_close)

    def on_about_window_close(self):
        self.about_window.destroy()
        self.about_window = None  # Reset the about_window attribute when closed


# Create the main Tkinter window
root = tk.Tk()
app = UrlShortenerApp(root)

# Run the main loop
root.mainloop()



