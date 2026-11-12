import pymupdf

path="c://Users//91995//Downloads//Introduction to Python.pdf"

document=pymupdf.open(path)

page=document.load_page(0)
text=page.get_text()
print(text)