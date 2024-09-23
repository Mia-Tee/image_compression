import tkinter as tk
from tkinter import filedialog, messagebox, StringVar, OptionMenu, Frame
from PIL import Image

# Selecting an image file
def select_image():
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if file_path:
        selected_image_path.set(file_path)  # Display selected image path in the frame
    else:
        selected_image_path.set("No file selected")

# Compressing the image
def compress_image():
    file_path = selected_image_path.get()
    
    if not file_path or file_path == "No file selected":
        messagebox.showwarning("Warning", "Please select an image!")
        return
    
    try:
        # Open the image
        img = Image.open(file_path)
        
        # Ask the user where to save the compressed image
        save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("BMP", "*.bmp")])
        
        if not save_path:
            return  # If no save location is selected, return
        
        # Get the selected image quality percentage
        quality = int(quality_var.get())

        # Compress the image by reducing the quality
        img.save(save_path, optimize=True, quality=quality)

        # Show success message
        messagebox.showinfo("Success", f"Image compressed successfully at {quality}% quality!")

    except Exception as e:
        # Show error message if something goes wrong
        messagebox.showerror("Error", f"Failed to compress image: {e}")

# Tkinter window with navy blue theme
root = tk.Tk()
root.title("CompressIt")
root.geometry("500x300")
root.configure(bg='#001f3f')  # Navy blue background

# Variable to hold the selected image path
selected_image_path = StringVar(value="No file selected")

# Variable to hold the selected image quality percentage
quality_var = StringVar(value="60")  # Default quality value

# Header label
header_label = tk.Label(root, text="Compress and Save", font=("Arial", 18, "bold"), bg='#001f3f', fg='white')
header_label.pack(pady=10)

# Button to select image
select_image_button = tk.Button(root, text="Select Image", font=("Arial", 12), bg='white', fg='#001f3f', activebackground='#001f3f', activeforeground='white', command=select_image)
select_image_button.pack(pady=10)

# Frame to display the selected image path
path_frame = Frame(root, bg='white', bd=2, relief="sunken", width=450, height=30)
path_frame.pack(pady=5)
path_label = tk.Label(path_frame, textvariable=selected_image_path, font=("Arial", 10), bg='white', fg='#001f3f', anchor="w", padx=5)
path_label.pack(fill='both')

# Label for image quality
quality_label = tk.Label(root, text="Select Image Quality:", font=("Arial", 12), bg='#001f3f', fg='white')
quality_label.pack(pady=10)

# Dropdown menu for image quality options
quality_options = ["20", "40", "50", "60", "70", "80", "90"]
quality_menu = OptionMenu(root, quality_var, *quality_options)
quality_menu.config(font=("Arial", 12), bg='white', fg='#001f3f', activebackground='#001f3f', activeforeground='white', width=10)
quality_menu.pack(pady=5)

# Button to compress the selected image
compress_button = tk.Button(root, text="Compress Image", font=("Arial", 12), bg='white', fg='#001f3f', activebackground='#001f3f', activeforeground='white', command=compress_image)
compress_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
