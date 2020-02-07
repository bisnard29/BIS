from reportlab.lib.units import cm
from invoice.conf import settings

business_details = (
    u'Your Name',
    u'# A street',
    u'##### Town',
    u'Country',
    u'',
    u'Email: you@example.com',
    u'Site: www.example.com',
    u'Tel: 0## ### ### ###'
)

note = (
    u'PAYMENT TERMS: 30 DAYS FROM INVOICE DATE.',
    u'Please make all cheques payable to Your Name.',
)


def draw_header(canvas):
    """ Draws the invoice header """
    canvas.setStrokeColorRGB(0.13, 0.55, 0.87)
    canvas.setFillColorRGB(0.2, 0.2, 0.2)
    canvas.setFont('Helvetica', 16)
    canvas.drawString(18 * cm, -1 * cm, 'Invoice')
    canvas.drawInlineImage(settings.INV_LOGO, 1 * cm, -1 * cm, 92, 16)
    canvas.setLineWidth(4)
    canvas.line(0, -1.25 * cm, 21.7 * cm, -1.25 * cm)


def draw_address(canvas):
    """ Draws the business address """
    canvas.setFont('Helvetica', 9)
    textobject = canvas.beginText(13 * cm, -2.5 * cm)
    for line in business_details:
        textobject.textLine(line)
    canvas.drawText(textobject)


def draw_footer(canvas):
    """ Draws the invoice footer """
    textobject = canvas.beginText(1 * cm, -27 * cm)
    for line in note:
        textobject.textLine(line)
    canvas.drawText(textobject)