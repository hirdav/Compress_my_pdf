

import fitz  # PyMuPDF for PDF handling
import os
import textwrap
from PIL import Image
import io

def extract_text_and_ascii_from_pdf(pdf_path, output_path, line_width=80):
    # Initialize an empty string for the extracted text
    text = ""
    
    # Open the PDF and read each page's text
    with fitz.open(pdf_path) as doc:
        for page_num, page in enumerate(doc):
            # Get raw text from the page
            page_text = page.get_text("text")
            images = page.get_images(full=True)

            # Split page text into paragraphs for better formatting
            paragraphs = page_text.split('\n\n')
            for paragraph in paragraphs:
                # Wrap each paragraph to a specified line width for better readability
                wrapped_text = textwrap.fill(paragraph, width=line_width)
                text += wrapped_text + "\n\n"  # Add spacing between paragraphs
            
            # If there are images, convert them to ASCII art and add to the text
            for img_index, img in enumerate(images):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image = Image.open(io.BytesIO(image_bytes))
                ascii_art = convert_image_to_ascii(image, line_width)
                text += f"Image {page_num+1}-{img_index+1}:\n{ascii_art}\n\n"
    
    # Save the extracted and formatted text to a file
    with open(output_path, "w", encoding="utf-8") as text_file:
        text_file.write(text)
    
    print(f"Text and ASCII art extracted and formatted to {output_path}")

def convert_image_to_ascii(image, line_width):
    # Convert the image to grayscale and resize it based on line width
    grayscale_image = image.convert("L")
    aspect_ratio = grayscale_image.width / grayscale_image.height
    new_width = line_width
    new_height = int(new_width / aspect_ratio / 2)
    resized_image = grayscale_image.resize((new_width, new_height))
    
    # ASCII characters by intensity
    ascii_chars = "@%#*+=-:. "
    ascii_art = ""
    for y in range(new_height):
        for x in range(new_width):
            pixel_value = resized_image.getpixel((x, y))
            ascii_art += ascii_chars[pixel_value // 32]
        ascii_art += "\n"
    return ascii_art

if __name__ == "__main__":
    # Set paths to the input PDF and output text file
    pdf_path = os.path.join(os.path.dirname(__file__), "..", "data", "sample4.pdf")
    output_path = os.path.join(os.path.dirname(__file__), "..", "data", "text_data_with_ascii.txt")
    
    # Extract and format text from the PDF
    extract_text_and_ascii_from_pdf(pdf_path, output_path)



