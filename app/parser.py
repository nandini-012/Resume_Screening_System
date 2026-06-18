import pdfplumber
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(r"C:\Users\hplap\Downloads\NANDINI_Resume_Job_Latest.pdf") as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

resume_text = extract_text_from_pdf(r"C:\Users\hplap\Downloads\NANDINI_Resume_Job_Latest.pdf")
print(resume_text)