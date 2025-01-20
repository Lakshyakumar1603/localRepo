import pdfplumber,PyPDF2,re

# Open the PDF file
with pdfplumber.open('p1.pdf') as pdf:

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader("p1.pdf")


     # Get the number of pages in the PDF
    num_pages = len(pdf_reader.pages)

    # Get the first page
    page = pdf.pages[0]


    # Extract text from the page
    text = page.extract_text()
    footer_pattern = re.search("^Transaction Statement for 7014805639$", text)
    if footer_pattern:
            text = text.replace(footer_pattern, '')
            
    print(text)
    # print(type(new_text))
    # print(text[0:500])
