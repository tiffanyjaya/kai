import logging
import re

from pathlib import Path

from pdfminer.converter import TextConverter
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfparser import PDFParser

from io import StringIO


def parse(input_path):
    rsrcmgr = PDFResourceManager()
    sio = StringIO()
    device = TextConverter(rsrcmgr, sio, codec="utf-8", laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    for file_path in Path(input_path).glob("*.pdf"):
        try:
            logging.info("Opening pdf file {}".format(file_path))
            file = open(file_path, "rb")
            parser = PDFParser(file)
            document = PDFDocument(parser)
            if not document.is_extractable:
                raise PDFTextExtractionNotAllowed
            for page in PDFPage.create_pages(document):
                interpreter.process_page(page)
            parser.close()

            # evaluate text
            text = sio.getvalue()
            text = re.sub(r'[^\x00-\x7F]+|\x0c',r' ', text)
            print(text)
        except IOError as error:
            logging.error("Cannot open {}".format(file_path))
            logging.error("IOError: {}".format(error))
        except PDFTextExtractionNotAllowed as error:
            logging.error("Cannot extract {}".format(file_path))
            logging.error("PDFTextExtractionNotAllowed: {}".format(error))

    sio.close()
    device.close()

parse(input_path="/Users/tiffapedia/projects/kai")
