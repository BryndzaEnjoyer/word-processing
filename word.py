from pydoc import doc
from docx import Document
from pathlib import Path
def find_document(filename):
    file_path = Path(__file__).parent / filename
    doc = Document(file_path)
    return doc
#1a
def count_paragraphs(filename):
    doc = find_document('essay_FINAL_general.docx')
    return len(doc.paragraphs)

#1b
doc = find_document('essay_FINAL_general.docx')
print("Number of paragraphs in the document:", count_paragraphs('essay_FINAL_general.docx'))
font = doc.styles['Normal'].font

#1c
def extract_file(filename):
    # file_path = Path(__file__).parent / filename
    doc = find_document('essay_FINAL_general.docx')

    header_lines = []
    title = ""
    body_paragraphs = []

    i = 0
    while i < len(doc.paragraphs) and doc.paragraphs[i].text.strip() != "":
        header_lines.append(doc.paragraphs[i].text.strip())
        i += 1

    while i < len(doc.paragraphs) and doc.paragraphs[i].text.strip() == "":
        i += 1

    while i < len(doc.paragraphs) and doc.paragraphs[i].text.strip() != "":
        title = doc.paragraphs[i].text
        i += 1

    for p in doc.paragraphs[i:]:
        t = p.text.strip()
        if t != "":
            body_paragraphs.append(t)

    return "\n".join(header_lines), title, "\n\n".join(body_paragraphs)

print(f'Header: {extract_file('essay_FINAL_general.docx')[0]}, Title: {extract_file('essay_FINAL_general.docx')[1]}, Body: {extract_file('essay_FINAL_general.docx')[2][:100]}...')
