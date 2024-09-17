
import os

from PIL import Image
from reportlab.pdfgen import canvas

# Get the current directory where the script is executed
current_directory = os.getcwd()


# Function to create a PDF for each image in the current directory
def create_pdfs_for_images(directory):
    # List all files in the current directory
    files = os.listdir(directory)

    # Check each file in the current directory
    for file in files:
        # Check if it is a supported image file
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Full path to the image
            image_path = os.path.join(directory, file)

            # Name of the output PDF file based on the image name
            pdf_name = os.path.splitext(file)[0] + '.pdf'
            pdf_path = os.path.join(directory, pdf_name)

            # Open the image using Pillow to get its dimensions
            img = Image.open(image_path)
            width, height = img.size

            # Create a PDF for each image with the image's size
            c = canvas.Canvas(pdf_path, pagesize=(width, height))
            try:
                # Insert the image into the PDF without resizing
                c.drawInlineImage(image_path, 0, 0, width=width, height=height)

                # Save the PDF file
                c.save()
                print(f'Successfully generated PDF: {pdf_path}')

            except Exception as e:
                print(f"Error processing image {image_path}: {e}")                                   


# Call the function to create PDFs for all images in the current directory
create_pdfs_for_images(current_directory)
