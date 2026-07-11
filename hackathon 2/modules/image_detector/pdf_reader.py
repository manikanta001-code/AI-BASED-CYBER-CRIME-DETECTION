import fitz  # PyMuPDF
from PIL import Image
import io


def extract_images_from_pdf(pdf_path):
    """
    Extract all images from a PDF.
    Returns a list of PIL Image objects.
    """

    images = []

    pdf = fitz.open(pdf_path)

    for page in pdf:

        image_list = page.get_images(full=True)

        for img in image_list:

            xref = img[0]

            base_image = pdf.extract_image(xref)

            image_bytes = base_image["image"]

            image = Image.open(io.BytesIO(image_bytes))

            images.append(image)

    pdf.close()

    return images