import logging
from pathlib import Path

from pdfminer.converter import TextConverter
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter

from io import StringIO

def parse(input_path):


    rsrcmgr = PDFResourceManager()
    sio = StringIO()
    device = TextConverter(rsrcmgr, sio)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    for file_path in Path(input_path).iterdir():
        file = open(file_path, "rb")
        parser = PDFParser(file)
        document = PDFDocument(parser)
        if not document.is_extractable:
            raise PDFTextExtractionNotAllowed
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
        parser.close()
        print(sio.getvalue())

    device.close()
    sio.close()

