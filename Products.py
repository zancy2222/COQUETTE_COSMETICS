import tkinter as tk
from tkinter import messagebox, Toplevel, Canvas, Scrollbar, ttk
from PIL import Image, ImageTk

import datetime

products = {
    "Lipstick": [
        {"name": "Liquid Matte Ultra-Comfort Transfer-Proof Lipstick", "price": 1550, "brand": "HUDA BEAUTY",
         "desc": "Finish: Matte, Formulation: Liquid, Stick Benefits: Long-wearing",
         "link": "https://www.sephora.ph/products/huda-beauty-liquid-matte-ultra-comfort-transfer-proof-lipstick/v/muse",
         "image": "HUDA BEAUTY.jpg"},
        {"name": "Satinallure™ Lipstick", "price": 1880, "brand": "PAT MCGRATH LABS",
         "desc": "Finish: Satin, Formulation: Cream, Benefits: Hydrating",
         "link": "https://www.sephora.ph/products/pat-mcgrath-labs-satinallure-lipstick/v/venusian-peach",
         "image": "PAT MCGRATH LABS.jpg"},
        {"name": "Silk Suede Lipstick", "price": 1600, "brand": "NATASHA MOOR",
         "desc": "Finish: Matte, Formulation: Liquid, Stick Benefits: Long-wearing",
         "link": "https://www.sephora.ph/products/natasha-moor-silk-suede-lipstick/v/euphoria",
         "image": "NATASHA MOOR.jpg"}
    ],
    "Lip Balm": [
        {"name": "Lux Ultra-Hydrating Lip Balm", "price": 1120, "brand": "FENTY SKIN",
         "desc": "Function: Moisturise, Treatment, Finish: Natural, Formulation: Balm, Benefits: Hydrating",
         "link": "https://www.sephora.ph/products/fenty-skin-lux-ultra-hydrating-lip-balm/v/cherry",
         "image": "FENTY SKIN.jpg"},
        {"name": "Glowing Lip Balm", "price": 2143, "brand": "SULWHASOO",
         "desc": "Finish: Satin, Formulation: Cream, Benefits: Hydrating",
         "link": "https://www.sephora.ph/products/sulwhasoo-glowing-lip-balm/v/no-dot-000-clear",
         "image": "SULWHASOO.jpg"},
        {"name": "Paradise Blooming Balm", "price": 2250, "brand": "DEAR DAHLIA",
         "desc": "Formulation: Balm, Stick, Benefits: Hydrating",
         "link": "https://www.sephora.ph/products/dear-dahlia-paradise-blooming-balm/v/3-8g",
         "image": "DEAR DAHLIA.jpg"}
    ],
    "Lip Gloss": [
        {"name": "Stay Vulnerable Glossy Lip Balm", "price": 1450, "brand": "RARE BEAUTY",
         "desc": "Formulation: Liquid, Benefits: Hydrating, Long-wearing",
         "link": "https://www.sephora.ph/products/rare-beauty-stay-vulnerable-glossy-lip-balm/v/nearly-apricot",
         "image": "RARE BEAUTY.jpg"},
        {"name": "Gloss Bomb Universal Lip Luminizer", "price": 1690, "brand": "FENTY BEAUTY",
         "desc": "Formulation: Liquid, Benefits: Hydrating",
         "link": "https://www.sephora.ph/products/fenty-gloss-bomb-universal-lip-luminizer/v/champ-stamp-fantasy",
         "image": "FENTY BEAUTY.jpg"},
        {"name": "Major Volume Plumping Gloss", "price": 1770, "brand": "PATRICK TA",
         "desc": "Formulation: Liquid, Benefits: Hydrating",
         "link": "https://www.sephora.ph/products/patrick-ta-major-volume-plumping-gloss/v/looks-natural",
         "image": "PATRICK TA.jpg"}
    ],
    "Foundation": [
        {"name": "Pro Filt'r Soft Matte Longwear Foundation", "price": 2950, "brand": "FENTY BEAUTY",
         "desc": "Skin Type: Combination, Dry, Normal, Oily, Finish: Matte, Coverage: Full, Medium, Formulation: Liquid",
         "link": "https://www.sephora.ph/products/fenty-pro-filtr-soft-matte-longwear-foundation/v/100-light-with-neutral-undertones",
         "image": "10FENTY BEAUTY.jpg"},
        {"name": "Best Skin Ever Perfect Natural Finish Longwear Foundation", "price": 1250, "brand": "SEPHORA COLLECTION",
         "desc": "Skin Type: Combination, Dry, Normal, Oily, Finish: Natural, Radiant, Coverage: Medium, Sheer, Formulation: Liquid",
         "link": "https://www.sephora.ph/products/sephora-collection-best-skin-ever-perfect-natural-finish-longwear-foundation/v/03-p",
         "image": "11 SEPHORA COLLECTION.jpg"},
        {"name": "Liquid Touch Weightless Foundation", "price": 2200, "brand": "RARE BEAUTY",
         "desc": "Skin Type: Combination, Dry, Normal, Oily, Coverage: Medium, Formulation: Liquid",
         "link": "https://www.sephora.ph/products/rare-beauty-liquid-touch-weightless-foundation/v/130n",
         "image": "12 RARE BEAUTY.jpg"}
    ],
    "Concealer": [
        {"name": "Liquid Touch Brightening Concealer", "price": 1550, "brand": "RARE BEAUTY",
         "desc": "Skin Type: Combination, Dry, Normal, Oily, Finish: Radiant, Coverage: Full, Medium, Formulation: Liquid",
         "link": "https://www.sephora.ph/products/rare-beauty-liquid-touch-brightening-concealer/v/110n",
         "image": "13 RARE BEAUTY.jpg"},
        {"name": "Shape Tape Contour Concealer", "price": 2050, "brand": "TARTE",
         "desc": "Skin Type: Combination, Dry, Normal, Oily, Sensitive, Finish: Matte, Radiant, Satin, Coverage: Full, Formulation: Cream",
         "link": "https://www.sephora.ph/products/tarte-shape-tape-contour-concealer/v/8b-porcelain-beige",
         "image": "14 TARTE.jpg"},
        {"name": "Fauxfilter Luminous Matte Liquid Concealer", "price": 2100, "brand": "HUDA BEAUTY",
         "desc": "Skin Type: Combination, Dry, Normal, Oily, Finish: Matte, Coverage: Full, Medium, Formulation: Cream",
         "link": "https://www.sephora.ph/products/huda-beauty-fauxfilter-luminous-matte-liquid-concealer/v/cotton-candy-2-dot-3-beige",
         "image": "15 HUDA BEAUTY.jpg"}
    ],
    "Powder": [
        {"name": "Prisme Libre Loose Powder", "price": 3560, "brand": "GIVENCHY",
         "desc": "Function: Finishing, Skin Type: Combination, Dry, Normal, Oily, Finish: Matte, Formulation: Loose Powder",
         "link": "https://www.sephora.ph/products/givenchy-prisme-libre/v/1-mousseline-pastel",
         "image": "16 GIVENCHY.jpg"},
        {"name": "Veil Translucent Setting Powder", "price": 3100, "brand": "HOURGLASS",
         "desc": "Function: Setting, Skin Type: Normal, Finish: Natural, Formulation: Loose Powder",
         "link": "https://www.sephora.ph/products/hourglass-veil-translucent-setting-powder/v/translucent",
         "image": "17 HOURGLASS.jpg"},
        {"name": "HD Skin Setting Powder", "price": 2600, "brand": "MAKE UP FOR EVER",
         "desc": "Function: Setting, Skin Type: Combination, Dry, Normal, Oily, Finish: Matte, Formulation: Pressed Powder",
         "link": "https://www.sephora.ph/products/make-up-for-ever-hd-skin-setting-powder/v/0-dot-1",
         "image": "18 MAKE UP FOR EVER.jpg"}
    ],
    "Eyeshadow": [
        {"name": "Discovery Eyeshadow Palette - Give Yourself Grace", "price": 2000, "brand": "RARE BEAUTY",
         "desc": "Function: Colour, Finish: Matte, Shimmer, Formulation: Pressed Powder",
         "link": "https://www.sephora.ph/products/rare-beauty-discovery-eyeshadow-palette-give-yourself-grace/v/default",
         "image": "19 RARE BEAUTY.jpg"},
        {"name": "Snap Shadows Eyeshadow Palette", "price": 2060, "brand": "FENTY BEAUTY",
         "desc": "Function: Colour, Finish: Matte, Shimmer, Formulation: Pressed Powder",
         "link": "https://www.sephora.ph/products/fenty-beauty-snap-shadows-eyhadow-palette/v/true-neutrals",
         "image": "20 FENTY BEAUTY.jpg"},
        {"name": "Tartelette™ Fresh Picked Amazonian Clay Palette", "price": 1550, "brand": "TARTE",
         "desc": "Function: Colour, Finish: Matte, Natural, Shimmer, Formulation: Pressed Powder",
         "link": "https://www.sephora.ph/products/tarte-tartelette-fresh-picked-amazonian-clay-palette/v/default",
         "image": "21 TARTE.jpg"}
    ],
    "Mascara": [
        {"name": "Unlocked Instant Extensions Mascara", "price": 2000, "brand": "HOURGLASS",
         "desc": "Function: Lengthen, Volumize",
         "link": "https://www.sephora.ph/products/hourglass-unlocked-instant-extensions-mascara/v/ultra-black",
         "image": "22 HOURGLASS.jpg"},
        {"name": "They're Real! Mascara", "price": 1760, "brand": "BENEFIT COSMETICS",
         "desc": "Function: Lengthen, Volumize",
         "link": "https://www.sephora.ph/products/benefit-cosmetics-theyre-real-mascara/v/jet-black",
         "image": "23 BENEFIT COSMETICS.jpg"},
        {"name": "Legendary Lengths Mascara", "price": 1150, "brand": "SLEEK MAKEUP",
         "desc": "Function: Lengthen",
         "link": "https://www.sephora.ph/products/sleek-makeup-legendary-lengths-mascara/v/jet-black",
         "image": "24 SLEEK MAKEUP.jpg"}
    ],
    "Blush": [
        {"name": "Air Matte Blush", "price": 1800, "brand": "NARS",
         "desc": "Finish: Matte, Coverage: Light, Medium, Formulation: Cream",
         "link": "https://www.sephora.ph/products/nars-air-matte-blush/v/darling",
         "image": "25 NARS.jpg"},
        {"name": "Rare Beauty Soft Pinch Liquid Blush", "price": 1450, "brand": "RARE BEAUTY",
         "desc": "Finish: Matte, Radiant, Formulation: Liquid",
         "link": "https://www.sephora.ph/products/rare-beauty-soft-pinch-liquid-blush/v/bliss",
         "image": "26 RARE BEAUTY.jpg"},
        {"name": "Cheek To Chic Blush", "price": 2600, "brand": "CHARLOTTE TILBURY",
         "desc": "Finish: Matte, Radiant, Formulation: Pressed Powder",
         "link": "https://www.sephora.ph/products/charlotte-tilbury-cheek-to-chic-blush/v/love-glow",
         "image": "27 CHARLOTTE TILBURY.jpg"}
    ]
}


# Initialize shopping cart
cart = []

# GUI setup
root = tk.Tk()
root.title("Coquette Cosmetics")
root.geometry("600x500")
root.config(bg="#FFC0CB")

# Title label
title_label = tk.Label(root, text="🎀 Welcome to COQUETTE COSMETICS 🎀", font=("Helvetica", 16, "bold"), bg="#FFC0CB")
title_label.pack(pady=10)

# Frame for categories and products
frame = tk.Frame(root, bg="#FFE4E1", bd=5)
frame.pack(pady=10, fill="both", expand=True)

# Product display area
product_display = tk.Text(frame, width=50, height=10, wrap="word", font=("Helvetica", 12))
product_display.pack(pady=10)


# Functions
def show_categories():
    product_display.delete("1.0", tk.END)
    product_display.insert(tk.END, "Select a category:\n\n")
    for category in products:
        product_display.insert(tk.END, f"{category}\n")
    product_display.insert(tk.END, "\nClick 'View Products' to explore.")


def view_products():
    category = selected_category.get()
    if category in products:
        product_display.delete("1.0", tk.END)
        product_display.insert(tk.END, f"{category} Products:\n\n")
        items = products[category]  # Access the list directly
        for idx, item in enumerate(items, 1):
            product_display.insert(tk.END, f"{idx}. {item['name']} - PHP {item['price']}\n")
            product_display.insert(tk.END, f"   Brand: {item['brand']}\n")
            product_display.insert(tk.END, f"   Description: {item['desc']}\n")
            product_display.insert(tk.END, f"   Link: {item['link']}\n\n")
    else:
        messagebox.showinfo("Info", "Please select a category.")


def add_to_cart():
    item_id = item_entry.get()
    category = selected_category.get()
    if category in products:
        try:
            item_id = int(item_id) - 1  # Adjust for zero-based indexing
            item = products[category][item_id]  # Access the item directly in the list
            cart.append(item)
            messagebox.showinfo("Added to Cart", f"{item['name']} added to cart!")
        except (IndexError, ValueError):
            messagebox.showerror("Error", "Invalid item number.")
    else:
        messagebox.showerror("Error", "Please select a valid category.")



def view_cart():
    product_display.delete("1.0", tk.END)
    product_display.insert(tk.END, "🛒 Your Cart:\n\n")
    if cart:
        total = 0
        for idx, item in enumerate(cart, 1):
            product_display.insert(tk.END, f"{idx}. {item['name']} - PHP {item['price']}\n")
            total += item['price']
        product_display.insert(tk.END, f"\nTotal: PHP {total}")
    else:
        product_display.insert(tk.END, "Your cart is empty.")


def remove_from_cart():
    item_id = item_entry.get()
    try:
        item_id = int(item_id) - 1  # Convert to zero-based index
        removed_item = cart.pop(item_id)  # Remove item from cart
        messagebox.showinfo("Removed", f"{removed_item['name']} removed from cart.")
    except (IndexError, ValueError):
        messagebox.showerror("Error", "Invalid item number.")



def checkout():
    if not cart:
        messagebox.showerror("Error", "Your cart is empty.")
        return

    try:
        amount_paid = float(amount_entry.get())
        total_cost = sum(item['price'] for item in cart)
        if amount_paid < total_cost:
            messagebox.showerror("Error", "Insufficient amount.")
            return
        change = amount_paid - total_cost
        generate_receipt(total_cost, amount_paid, change)
        messagebox.showinfo("Checkout", f"Payment successful!\nChange: PHP {change}")
        cart.clear()
    except ValueError:
        messagebox.showerror("Error", "Invalid amount entered.")


def generate_receipt(total, paid, change):
    with open("receipt.txt", "w") as file:
        file.write("------ Receipt ------\n")
        file.write(f"Date: {datetime.datetime.now()}\n\n")
        for item in cart:
            file.write(f"{item['name']} - PHP {item['price']}\n")
        file.write(f"\nTotal: PHP {total}\n")
        file.write(f"Amount Paid: PHP {paid}\n")
        file.write(f"Change: PHP {change}\n")
        file.write("----------------------\n")


selected_category = tk.StringVar(value="Lipstick")  # Default category


def preview_product_images():
    preview_window = Toplevel(root)
    preview_window.title("Product Image Preview")
    preview_window.geometry("800x600")

    canvas = Canvas(preview_window, width=780, height=580)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = Scrollbar(preview_window, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Get the selected category
    category = selected_category.get()

    row = 0
    for product in products.get(category, []):  # Load images based on selected category
        image_path = product["image"]
        try:
            img = Image.open(image_path)
            img = img.resize((150, 150), Image.LANCZOS)
            img_tk = ImageTk.PhotoImage(img)

            img_label = tk.Label(frame, image=img_tk, text=product["name"], compound="top")
            img_label.image = img_tk  # Keep a reference to avoid garbage collection
            img_label.grid(row=row, column=0, padx=10, pady=10)
            row += 1

        except Exception as e:
            print(f"Could not open {image_path}: {e}")

    # Configure scrolling region
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))



# Button to preview product images
preview_button = tk.Button(root, text="Preview Product Images", font=("Helvetica", 12), command=preview_product_images)
preview_button.pack(pady=10)

# Dropdown for selecting categories
selected_category = tk.StringVar(root)
selected_category.set("Select a Category")
category_menu = tk.OptionMenu(root, selected_category, *products.keys())
category_menu.pack(pady=5)

# Entry for item selection
item_entry = tk.Entry(root, font=("Helvetica", 12))
item_entry.pack(pady=5)
item_entry.insert(0, "Enter item number")

# Entry for payment amount
amount_entry = tk.Entry(root, font=("Helvetica", 12))
amount_entry.pack(pady=5)
amount_entry.insert(0, "Enter amount to pay")

# Buttons
btn_frame = tk.Frame(root, bg="#FFC0CB")
btn_frame.pack(pady=10)

view_btn = tk.Button(btn_frame, text="View Products", font=("Helvetica", 12), command=view_products)
view_btn.grid(row=0, column=0, padx=10)

add_btn = tk.Button(btn_frame, text="Add to Cart", font=("Helvetica", 12), command=add_to_cart)
add_btn.grid(row=0, column=1, padx=10)

cart_btn = tk.Button(btn_frame, text="View Cart", font=("Helvetica", 12), command=view_cart)
cart_btn.grid(row=0, column=2, padx=10)

remove_btn = tk.Button(btn_frame, text="Remove from Cart", font=("Helvetica", 12), command=remove_from_cart)
remove_btn.grid(row=0, column=3, padx=10)

checkout_btn = tk.Button(root, text="Checkout", font=("Helvetica", 12), command=checkout)
checkout_btn.pack(pady=10)

# Show categories at startup
show_categories()

root.mainloop()
