from pdfminer.high_level import extract_text

class RegularPDFText():
    def _init_():
        pass
    def textconvert(self, filename):
        return extract_text(filename, caching=True, codec='utf-8', laparams=None)
