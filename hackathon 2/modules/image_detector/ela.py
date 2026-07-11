from PIL import Image, ImageChops, ImageEnhance
import os


def analyze_ela(image_path, quality=90):

    temp_file = "temp_ela.jpg"

    original = Image.open(image_path).convert("RGB")

    original.save(temp_file, "JPEG", quality=quality)

    compressed = Image.open(temp_file)

    diff = ImageChops.difference(original, compressed)

    extrema = diff.getextrema()

    max_diff = max(channel[1] for channel in extrema)

    if max_diff == 0:
        max_diff = 1

    scale = 255.0 / max_diff

    ela_image = ImageEnhance.Brightness(diff).enhance(scale)

    output = "ela_output.jpg"

    ela_image.save(output)

    pixels = list(ela_image.getdata())

    total = 0

    for pixel in pixels:
        total += sum(pixel) / 3

    average = total / len(pixels)

    os.remove(temp_file)

    if average < 20:
        prediction = "LIKELY ORIGINAL"
        risk = 5

    elif average < 40:
        prediction = "POSSIBLY EDITED"
        risk = 40

    else:
        prediction = "HIGH POSSIBILITY OF EDITING"
        risk = 75

    return {
        "prediction": prediction,
        "ela_score": round(average, 2),
        "risk_score": risk,
        "ela_image": output
    }