import datetime
import PyPDF2


class PdfHelper:

    MAX_LINES_PER_PAGE = 20

    def __init__(self, path):
        self.path = path
        self.MAX_LINES_PER_PAGE = 20

    def write_pdf(self, lines):
        # Get current date and time
        now = datetime.datetime.now()

        # Open the PDF file for appending
        pdf_file = open(self.path, 'ab')

        # Check if the PDF file is empty
        file_size = pdf_file.tell()
        is_empty = (file_size == 0)

        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfFileWriter()

        # Check if a new page is needed
        if not is_empty and len(pdf_writer.pages) > 0:
            last_page = pdf_writer.pages[-1]
            if last_page.getContentsStream() and last_page.getContentsStream().getData():
                if len(last_page.getContentsStream().getData()) > self.MAX_LINES_PER_PAGE:
                    # Create a new page
                    page = pdf_writer.addBlankPage(width=612, height=792)  # Letter size page (8.5 x 11 inches)
            else:
                # Create a new page
                page = pdf_writer.addBlankPage(width=612, height=792)  # Letter size page (8.5 x 11 inches)
        else:
            # Create a new page
            page = pdf_writer.addBlankPage(width=612, height=792)  # Letter size page (8.5 x 11 inches)

        # Add the log entry to the page
        for line in lines:
            page.mergePage(PyPDF2.pdf.PageObject.createFromString(line))

        # Write the page to the PDF file
        pdf_writer.addPage(page)
        pdf_writer.write(pdf_file)

        # Close the PDF file
        pdf_file.close()