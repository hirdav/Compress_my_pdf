import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import fitz  # PyMuPDF for PDF handling
import textwrap
import gzip, bz2, zlib
import matplotlib.pyplot as plt
from PIL import Image
import io
import threading

extracted_text_path = None
compressed_files = {}

def update_status(message):
    """Update status label in GUI."""
    status_label.config(text=message)
    root.update_idletasks()

def select_pdf():
    """Open file dialog to select a PDF file."""
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    pdf_entry.delete(0, tk.END)
    pdf_entry.insert(0, file_path)

def extract_text_and_ascii(pdf_path, output_folder):
    """Extract text and convert images to ASCII."""
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]  
    output_txt_path = os.path.join(output_folder, f"{pdf_name}.txt")
    text = ""

    with fitz.open(pdf_path) as doc:
        for page_num, page in enumerate(doc):
            update_status(f"Extracting text: Page {page_num+1}/{len(doc)}")
            page_text = page.get_text("text")
            images = page.get_images(full=True)

            paragraphs = page_text.split('\n\n')
            for paragraph in paragraphs:
                wrapped_text = textwrap.fill(paragraph, width=80)
                text += wrapped_text + "\n\n"

            for img_index, img in enumerate(images):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image = Image.open(io.BytesIO(image_bytes))
                ascii_art = convert_image_to_ascii(image, 80)
                text += f"\nImage {page_num+1}-{img_index+1}:\n\n{ascii_art}\n\n"

    with open(output_txt_path, "w", encoding="utf-8") as text_file:
        text_file.write(text)

    return output_txt_path

def convert_image_to_ascii(image, line_width):
    """Convert image to ASCII."""
    grayscale_image = image.convert("L")
    aspect_ratio = grayscale_image.width / grayscale_image.height
    new_width = min(line_width, grayscale_image.width)
    new_height = int(new_width / aspect_ratio / 2)
    resized_image = grayscale_image.resize((new_width, new_height))
    
    ascii_chars = "█▓▒░. "
    ascii_art = ""
    for y in range(new_height):
        line = "".join(ascii_chars[resized_image.getpixel((x, y)) // 51] for x in range(new_width))
        ascii_art += line.center(line_width) + "\n"
    return ascii_art

def compress_text():
    """Compress extracted text with progress updates."""
    global compressed_files, extracted_text_path
    if not extracted_text_path:
        messagebox.showerror("Error", "Please extract text first!")
        return

    update_status("Compressing text...")
    with open(extracted_text_path, "r", encoding="utf-8") as file:
        text_data = file.read()
    
    compressed_files = {}
    compressors = {
        "gzip": gzip.compress(text_data.encode("utf-8")),
        "bz2": bz2.compress(text_data.encode("utf-8")),
        "zlib": zlib.compress(text_data.encode("utf-8"))
    }

    for i, (method, compressed_data) in enumerate(compressors.items(), 1):
        update_status(f"Compressing ({method.upper()})... [{i}/3]")
        compressed_path = f"{extracted_text_path}_{method}.txt"
        with open(compressed_path, "wb") as file:
            file.write(compressed_data)
        compressed_files[method] = (compressed_path, len(compressed_data) / len(text_data.encode("utf-8")))

    update_status("Compression completed!")

def analyze_results():
    """Plot compression results with progress updates."""
    global compressed_files
    if not compressed_files:
        messagebox.showerror("Error", "Please compress the text first!")
        return

    update_status("Generating compression analysis...")
    methods = list(compressed_files.keys())
    ratios = [compressed_files[m][1] for m in methods]

    plt.figure(figsize=(6, 4))
    plt.barh(methods, ratios, color=['skyblue', 'salmon', 'lightgreen'])
    plt.xlabel("Compression Ratio")
    plt.title("Compression Ratio by Method")
    plt.figtext(0.5, -0.1, "Lower compression ratio means better compression efficiency.", wrap=True, ha='center', fontsize=10)
    plt.show()
    update_status("Analysis displayed!")

def process_pdf():
    """Threaded function to extract text so GUI remains responsive."""
    def run():
        global extracted_text_path
        pdf_path = pdf_entry.get()
        output_folder = filedialog.askdirectory()

        if not pdf_path or not output_folder:
            messagebox.showerror("Error", "Please select both a PDF file and an output folder.")
            return

        update_status("Extracting text from PDF...")
        extracted_text_path = extract_text_and_ascii(pdf_path, output_folder)
        update_status("Text extraction completed!")

    threading.Thread(target=run).start()

def process_compression():
    """Threaded function to run compression in background."""
    threading.Thread(target=compress_text).start()

def process_analysis():
    """Threaded function to show analysis in background."""
    threading.Thread(target=analyze_results).start()

# GUI Setup
root = tk.Tk()
root.title("PDF to ASCII & Compression")
root.geometry("500x300")

# Select PDF File
tk.Label(root, text="Select PDF File:").pack(pady=5)
pdf_entry = tk.Entry(root, width=50)
pdf_entry.pack()
tk.Button(root, text="Browse", command=select_pdf).pack(pady=5)

# Run Extraction Button
tk.Button(root, text="Extract Text", command=process_pdf, bg="blue", fg="white").pack(pady=5)

# Run Compression Button
tk.Button(root, text="Compress Text", command=process_compression, bg="green", fg="white").pack(pady=5)

# Show Analysis Button
tk.Button(root, text="Show Analysis", command=process_analysis, bg="orange", fg="white").pack(pady=5)

# Status Label
status_label = tk.Label(root, text="Idle", fg="black")
status_label.pack(pady=10)

root.mainloop()
