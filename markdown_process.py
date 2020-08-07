import markdown
import pdfkit
import sys


class Markdown():
    def __init__(self, md, css='', outfile='output'):
        with open('template.html', 'r', encoding='utf-8') as input:
            self.html = input.read()
            input.close()
        with open(md, 'r', encoding='utf-8') as input:
            raw_md = input.read()
            self.title = raw_md.splitlines()[0].strip('#').strip()
            self.body = markdown.markdown(raw_md)
            input.close()
        with open(css, 'r', encoding='utf-8') as input:
            self.css = input.read()
            input.close()
        self.insert_element(self.title, '</title>')
        self.insert_element(self.css, '</style>')
        self.insert_element(self.body, '</body>')
        self.pdf_options = {
            'quiet': '',
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
        }

    def insert_element(self, element, index):
        i = self.html.find(index)
        self.html = f'{self.html[:i]}{element}{self.html[i:]}'

    def toPDF(self, outfile):
        pdfkit.from_string(
            self.html, outfile, options=self.pdf_options)

    def toHTML(self, outfile):
        with open(outfile, 'w', encoding='utf-8') as output:
            output.write(self.html)


for arg in sys.argv:
    if '.md' in arg:
        input_md = arg
    if '.css' in arg:
        input_css = arg
    if '.html' in arg:
        html = arg
    if '.pdf' in arg:
        pdf = arg


resume = Markdown(input_md, input_css)

if html:
    resume.toHTML(html)

if pdf:
    resume.toPDF(pdf)
