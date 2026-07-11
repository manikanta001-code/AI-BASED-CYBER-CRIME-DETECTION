from modules.image_detector.metadata import analyze_metadata

path = input("Image path: ").strip().strip('"')

result = analyze_metadata(path)

print("\n========== METADATA REPORT ==========\n")

for key, value in result.items():
    print(f"{key}: {value}")