import fitz  # PyMuPDF
import pdfplumber
import re
import json
import os

PDF_PATH = "solar.pdf"           # path to your PDF
OUTPUT_JSON = "result.json"      # JSON output
IMAGE_DIR = "Pics extraction"   # directory to save images

# Create image directory if not exists
os.makedirs(IMAGE_DIR, exist_ok=True)


def extract_options(text):
    """
    Extract options from text using regex:
    Looks for a., b., c., d. patterns
    """
    options = {}
    matches = re.findall(r"([a-dA-D])\.\s*(.*?)\s*(?=[a-dA-D]\.|$)", text, re.DOTALL)
    for letter, option_text in matches:
        options[letter.lower()] = option_text.strip()
    return options if options else None

def extract_questions_from_text(text):
    """
    Split text into questions by numbering (Q1, 1., etc.)
    """
    pattern = r"(?:Q\d+|\d+)\.?\s*(.*?)\n(?=(?:Q\d+|\d+)\.?|$)"
    questions = re.findall(pattern, text, re.DOTALL)
    return [q.strip() for q in questions]

# ---------- MAIN PARSER ----------
def parse_pdf(pdf_path):
    data = []
    doc = fitz.open(pdf_path)

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(doc):
            pdf_page = pdf.pages[page_num]

            page_text = page.get_text("text")

            questions_text = extract_questions_from_text(page_text)

            # images extraction
            page_images = []
            for img_index, img in enumerate(page.get_images(full=True)):
                xref = img[0]
                pix = fitz.Pixmap(doc, xref)

                # Convert to RGB if needed
                if pix.n > 4 or pix.n == 4:
                    pix = fitz.Pixmap(fitz.csRGB, pix)

                img_filename = f"{IMAGE_DIR}/page{page_num+1}_img{img_index}.png"
                pix.save(img_filename)
                pix = None
                page_images.append(img_filename)

            # table creation
            tables = pdf_page.extract_tables()
            tables = tables if tables else None

            # combine question one after other
            if questions_text:
                for idx, q_text in enumerate(questions_text, start=1):
                    question_data = {
                        "page": page_num + 1,
                        "question_no": idx,
                        "text": q_text,
                        "options": extract_options(q_text),
                        "table": tables,
                        "images": page_images if page_images else None
                    }
                    data.append(question_data)
            else:
                
                data.append({
                    "page": page_num + 1,
                    "note": "No clear questions extracted. PDF may not follow Q1./1. pattern."
                })

    return data

# json file creation
def save_json(data, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# main fun()
if __name__ == "__main__":
    parsed_data = parse_pdf(PDF_PATH)
    save_json(parsed_data, OUTPUT_JSON)
    print(f"✅ Parsing complete! JSON saved to {OUTPUT_JSON}")
    print(f"📂 Images saved in folder: {IMAGE_DIR}")