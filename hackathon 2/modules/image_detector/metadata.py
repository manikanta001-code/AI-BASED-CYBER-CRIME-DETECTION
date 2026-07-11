from PIL import Image
from PIL.ExifTags import TAGS


def analyze_metadata(image_path):

    report = {
        "camera": "Unknown",
        "software": "Not Available",
        "datetime": "Unknown",
        "gps": "Not Available",
        "risk_score": 0,
        "reasons": []
    }

    try:

        img = Image.open(image_path)
        exif = img.getexif()

        if not exif:

            report["risk_score"] += 20
            report["reasons"].append("No EXIF metadata found.")

            return report

        for tag_id, value in exif.items():

            tag = TAGS.get(tag_id, tag_id)

            if tag == "Model":
                report["camera"] = str(value)

            elif tag == "Software":
                report["software"] = str(value)

            elif tag == "DateTime":
                report["datetime"] = str(value)

            elif tag == "GPSInfo":
                report["gps"] = "Available"

        software = report["software"].lower()

        suspicious = [
            "photoshop",
            "gimp",
            "canva",
            "pixlr",
            "adobe",
            "lightroom"
        ]

        for editor in suspicious:

            if editor in software:

                report["risk_score"] += 40

                report["reasons"].append(
                    f"Edited using {report['software']}"
                )

        if report["camera"] == "Unknown":

            report["risk_score"] += 20

            report["reasons"].append(
                "Camera model missing."
            )

    except Exception as e:

        report["risk_score"] = 30

        report["reasons"].append(str(e))

    return report