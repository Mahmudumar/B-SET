import PyPDF2

# Open the PDF file in binary mode
with open('b-stat.pdf', 'rb') as file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(file)

    # Initialize an empty string to store the extracted text
    text = ''

    # Iterate through each page of the PDF
    for page_num in range(len(pdf_reader.pages)):
        # Get the page object
        page = pdf_reader.pages[page_num]

        # Extract text from the page
        page_text = page.extract_text()

        # Append the extracted text to the string
        text += page_text

# Print the extracted text
print(text)
