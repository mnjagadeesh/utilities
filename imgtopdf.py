# This scrit generate pdf file from given image folder input.
# I usually take picture of old useful book and store in folder.
# Then simply run this script to generate pdf out of it.

# free for anyone to use

# pip install reportlab Pillow

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image
import os


def create_pdf_from_images(image_list, output_pdf):
    # Create a PDF document
    pdf_canvas = canvas.Canvas(output_pdf, pagesize=letter)

    # Loop through each image and add it to the PDF
    for image_path in image_list:
        try:
            # Open the image using Pillow
            image = Image.open(image_path)

            # Get the size of the image and adjust it to fit the page
            width, height = letter
            aspect_ratio = width / float(image.width)
            image_width = width
            image_height = aspect_ratio * float(image.height)

            # Draw the image on the PDF canvas
            pdf_canvas.drawInlineImage(image, 0, 0, width=image_width, height=image_height)

            # Add a new page for the next image
            pdf_canvas.showPage()
        except Exception as e:
            print(f"Error processing {image_path}: {e}")

    # Save the PDF
    pdf_canvas.save()

def list_files(folder_path="C:/Users/Jagadeesh/Downloads/Photos-001/book"):
    flist = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            flist.append(file_path)
    return flist
if __name__ == "__main__":
    # List of image files to include in the PDF
    image_list = list_files()
    
    # Output PDF file
    output_pdf = "output.pdf"

    # Create the PDF from the list of images
    create_pdf_from_images(image_list, output_pdf)

    print(f"PDF created successfully: {output_pdf}")
