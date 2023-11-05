from fpdf import FPDF
from PIL import Image

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font('helvetica', '', 50)
def center(text, height):
    title = text.strip()

    # Calculate the width of the page and the width of the title
    page_width = pdf.w
    title_width = pdf.get_string_width(title)

    # Calculate the x-coordinate for centering the title
    x_centered = (page_width - title_width) / 2

    # Move to the x-coordinate for centering the title
    pdf.set_x(x_centered)

    # Draw the centered title
    #pdf.cell(title_width, 10, title, new_x="LMARGIN", new_y="NEXT", "C")
    pdf.cell(title_width, height, title, new_x="LMARGIN", new_y="NEXT", align='C')

center('CS50 Shirtificate', 60)
imgw = 190
pdf.image("shirtificate.png", (pdf.w - imgw)/2, 70, imgw)

pdf.set_font('helvetica', 'B', 24)
pdf.set_text_color(250, 250, 250)

center(input('Shirt sentence: '), 140)

pdf.output("shirtificate.pdf")