import pymupdf

path1="C://Users//91995//Downloads//Introduction to Python.pdf"
path2="C://Users//91995//Downloads//dummy.pdf"

pdf_paths=[path1,path2]

for path in pdf_paths:
    doc=pymupdf.open(path)
    for page_num in range(doc.page_count):
        page=doc.load_page(page_num)
        text=page.get_text()
        print(text)