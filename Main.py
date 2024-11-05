import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import subprocess
import sys


class CoquetteCosmeticsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Coquette Cosmetics")
        self.root.geometry("600x500")
        self.root.configure(bg="#FFF0F5")  # Light pink background color

        # Load and resize the logo image
        self.load_logo()

        # Create UI elements
        self.create_ui_elements()

    def load_logo(self):
        """Load and resize the logo image."""
        try:
            image = Image.open("LOGO1.png")
            resized_image = image.resize((200, 200), Image.LANCZOS)  # Adjusted size for a smaller, refined look
            self.logo_image = ImageTk.PhotoImage(resized_image)
        except Exception as e:
            messagebox.showerror("Image Error", "Logo image not found. Make sure 'LOGO1.png' is in the directory.")
            sys.exit()

    def create_ui_elements(self):
        """Create and place the UI elements."""
        logo_label = tk.Label(self.root, image=self.logo_image, bg="#FFF0F5")
        logo_label.pack(pady=(20, 10))

        welcome_text = tk.Label(
            self.root,
            text="🎀 Welcome to COQUETTE COSMETICS 🎀\nUnveil your inner coquette!",
            font=("Garamond", 20, "bold"),
            fg="#D44872",  # Dark pink color for a luxurious feel
            bg="#FFF0F5",
            wraplength=500,
            justify="center"
        )
        welcome_text.pack(pady=(10, 40))

        # Create a style for the "Proceed" button
        self.create_proceed_button()

    def create_proceed_button(self):
        """Create and style the Proceed button."""
        style = ttk.Style()
        style.configure("TButton",
                        font=("Garamond", 14, "bold"),
                        foreground="#D44872",
                        background="#D44872",
                        padding=10)
        style.map("TButton",
                  background=[("active", "#C04066")])  # Darker pink on hover

        proceed_button = ttk.Button(
            self.root,
            text="Proceed",
            command=self.proceed,
            style="TButton"
        )
        proceed_button.pack(pady=20)

    def proceed(self):
        """Function to handle the Proceed button click."""
        try:
            self.root.destroy()  # Close the current window
            subprocess.run([sys.executable, "Products.py"])  # Open Products.py
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open Products.py: {e}")


# Create the main window and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CoquetteCosmeticsApp(root)
    root.mainloop()
