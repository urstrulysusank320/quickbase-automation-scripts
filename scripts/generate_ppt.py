from pptx import Presentation
import requests

# Example: create a simple PPT
ppt = Presentation()
slide = ppt.slides.add_slide(ppt.slide_layouts[0])
slide.shapes.title.text = "Quickbase Report"
slide.placeholders[1].text = "Generated via GitHub + app.perfect"

# Save locally (or to web server)
file_path = "quickbase_report.pptx"
ppt.save(file_path)

# Optional: upload to a storage (S3, GDrive, etc.) and get download URL
print("PPT generated successfully:", file_path)
