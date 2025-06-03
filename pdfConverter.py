#Vibe coded a pdf scrapper for fun


import fitz  # PyMuPDF
from pdf2image import convert_from_path
import os
import shutil

pdf_path = "AVDASI2_ExpAero.pdf"
output_dir = "pdf_export"
mkdocs_docs = "../docs"  # MkDocs docs folder path

os.makedirs(output_dir, exist_ok=True)

# Convert PDF pages to images first (you need images folder)
images = convert_from_path(pdf_path, poppler_path=r"C:\poppler\poppler-24.08.0\Library\bin")
img_dir = os.path.join(output_dir, "images")
os.makedirs(img_dir, exist_ok=True)

for i, img in enumerate(images):
    img_path = os.path.join(img_dir, f"page_{i+1}.png")
    img.save(img_path, "PNG")

# Open the PDF with PyMuPDF
doc = fitz.open(pdf_path)

# Create one Markdown file for all pages
combined_md_path = os.path.join(output_dir, "combined.md")
with open(combined_md_path, "w", encoding="utf-8") as f:
    for i, page in enumerate(doc):
        text = page.get_text("text")
        f.write(f"# Page {i+1}\n\n")
        f.write(text)
        f.write("\n\n")
        f.write(f"![Page Image](images/page_{i+1}.png)\n\n")

# Copy combined Markdown file to MkDocs docs folder
shutil.copy(combined_md_path, mkdocs_docs)

# Copy images folder to MkDocs docs folder (overwrite if exists)
dest_img_dir = os.path.join(mkdocs_docs, "images")
shutil.copytree(img_dir, dest_img_dir, dirs_exist_ok=True)

print("Conversion done. Combined markdown and images copied to MkDocs docs folder.")
