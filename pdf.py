from pikepdf import Pdf, PdfImage


old_pdf = Pdf.open("c:\\Users\\Samiullah\\Favorites\\Downloads\\Pakistan_CR2017B.pdf")

page_1 = old_pdf.pages[13]


if page_1.images:
    print("Available image keys:", list(page_1.images.keys()))  

image_key = "/Image108"  
if image_key in page_1.images:
        raw_image = page_1.images[image_key]  
        pdf_image = PdfImage(raw_image)  
        pdf_image.extract_to(fileprefix="test1")
        print("Extracted image saved as: test1.png")
else:
        print("Image {image_key} not found.")

