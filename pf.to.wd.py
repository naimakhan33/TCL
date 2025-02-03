from pdf2docx import Converter  

old_pdf = r"C:\Users\Samiullah\Favorites\Downloads\Resume.pdf"
new_doc = r"new_docx"

obj = Converter(old_pdf)
obj.convert(new_doc) 
obj.close()
  

