import tkinter as tk
import qrcode
from PIL import Image, ImageTk
from tkinter import filedialog

# Global variable to store the QR code image
qr_img = None

# Function to generate and display the QR code
def generate_qr_code():
    global qr_img  # Declare qr_img as a global variable
    url = entry.get()  # Get the URL from the entry field
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert the QR code image to a PhotoImage
    qr_img = qr_img.convert('RGB')
    qr_photo = ImageTk.PhotoImage(qr_img)
    
    # Display the QR code in the Tkinter Label
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo

# Function to download the QR code
def download_qr_code():
    if qr_img is not None:
        # Save the QR code image as a file dialog
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")], title="Save QR Code")
        if file_path:
            qr_img.save(file_path)

# Create the main window
window = tk.Tk()
window.title("QR Code Generator")

# Create a label and an entry field for the URL
url_label = tk.Label(window, text="Enter URL:")
url_label.pack(pady=10)
entry = tk.Entry(window)
entry.pack()

# Create a button to generate the QR code
generate_button = tk.Button(window, text="Generate QR Code", command=generate_qr_code)
generate_button.pack(pady=10)

# Create a button to download the QR code
download_button = tk.Button(window, text="Download QR Code", command=download_qr_code)
download_button.pack(pady=10)

# Create a label to display the QR code
qr_label = tk.Label(window)
qr_label.pack()

# Start the Tkinter main loop
window.mainloop()
# Create the main window
window = tk.Tk()
window.title("QR Code Generator")

# Create a label and an entry field for the URL
url_label = tk.Label(window, text="Enter URL:")
url_label.pack(pady=10)
entry = tk.Entry(window)
entry.pack()

# Create a button to generate the QR code
generate_button = tk.Button(window, text="Generate QR Code", command=generate_qr_code)
generate_button.pack(pady=10)

# Create a button to download the QR code
download_button = tk.Button(window, text="Download QR Code", command=download_qr_code)
download_button.pack(pady=10)

# Create a label to display the QR code
qr_label = tk.Label(window)
qr_label.pack()

# Start the Tkinter main loop
window.mainloop()
