import os
import fitz
from PIL import Image

IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".tiff",
    ".tif",
    ".webp"
}


def load_file(file_path):
    """
    Loads an image or PDF.

    Returns:
        List[PIL.Image]
    """

    extension = os.path.splitext(file_path)[1].lower()

    # ---------- IMAGE ----------
    if extension in IMAGE_EXTENSIONS:

        image = Image.open(file_path)

        return [image]

    # ---------- PDF ----------
    elif extension == ".pdf":

        pdf = fitz.open(file_path)

        pages = []

        for page in pdf:

            pix = page.get_pixmap(dpi=300)

            img = Image.frombytes(
                "RGB",
                [pix.width, pix.height],
                pix.samples
            )

            pages.append(img)

        pdf.close()

        return pages

    else:

        raise ValueError(
            f"Unsupported file type: {extension}"
        )