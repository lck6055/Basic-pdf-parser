# Basic PDF Parser 📝

A Python-based PDF parser that extracts **questions, options, tables, and images** from structured text-based PDFs such as multiple-choice question papers.

---

## Features ✨

- **Question & Option Extraction:** Extracts numbered questions (e.g., Q1., 1.) and associated lettered multiple-choice options (e.g., a., b., c., d.).
- **Table Extraction:** Extracts tables from the PDF pages using `pdfplumber`.
- **Image Extraction:** Extracts images from the PDF pages.
- **Structured Output:** Saves the final extracted data as a structured **JSON** file (`result.json`).
- **File Management:** Stores all extracted images in a dedicated folder (`Pics extraction`).

---

## Installation ⚙️

1. **Clone the repository:**

    ```bash
    git clone [https://github.com/lck6055/Basic-pdf-parser.git](https://github.com/lck6055/Basic-pdf-parser.git)
    cd Basic-pdf-parser
    ```

2. **Install the required Python libraries:**

    ```bash
    pip install -r requirements.txt
    ```

---

## Usage 🖥️

1. **Prepare the PDF:** Place your target PDF file in the project directory and, if necessary, update the `PDF_PATH` variable inside the `parsing.py` script.
2. **Run the parser:**

    ```bash
    python parsing.py
    ```

### Output:

- **JSON Data:** A file named `result.json` containing the extracted questions and options.
- **Images:** Extracted images saved within the folder `Pics extraction`.

---

## Running Mode & Limitations ⚠️

**❗ IMPORTANT: This is currently a prototype and is still under development. The existing limitations are acknowledged.**

| Aspect | Details |
| :--- | :--- |
| **Best Used With** | **Text-based PDFs**. It **will not** work on scanned PDFs without Optical Character Recognition (OCR). |
| **Question Format** | Assumes clearly numbered questions (e.g., `Q1.`, `1.`, etc.). |
| **Option Format** | Assumes lettered options (e.g., `a.`, `b.,` `c.`, `d.`). |
| **Image Caveat** | Image extraction is page-based and may include **all images** on the page, not strictly tied to the exact question block. |
| **Table Caveat** | Tables are extracted using `pdfplumber` and may not be perfect for highly complex or irregular table layouts. |
| **Failure Condition** | PDFs without clear numbering or those consisting solely of scanned images may result in incomplete or empty JSON data. |

---

## References 📚

This project utilizes the following key libraries and documentation:

- [PyMuPDF Documentation](https://pymupdf.readthedocs.io/)
- [pdfplumber Documentation](https://github.com/jsvine/pdfplumber)
- [Python official docs for `re` and `json` modules](https://docs.python.org/3/)
- **Documentation Assistance:** An AI language model was used to help structure and write the content of this README file.
