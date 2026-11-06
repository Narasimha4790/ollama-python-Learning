import pymupdf

pdf_path="C://Users//91995//Downloads//dummy.pdf"

try:
    doc = pymupdf.open(pdf_path)

except pymupdf.FileNotFoundError:
    print("PDF file not found. Check the file path.")

else:
    print("No.of Pages",doc.page_count)

    extracted_text=[]

    for page in range(doc.page_count):
        current_page=doc.load_page(page)
        text=current_page.get_text()
        extracted_text.append(text)

    doc.close()

    combined_text=" ".join(extracted_text)

    print(combined_text)
