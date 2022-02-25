from pikepdf import Pdf
new_pdf = Pdf.new()
with Pdf.open('in/t2200-21e.pdf') as pdf:
    pdf.save('output-nofill.pdf')