from docx import Document
from docx.shared import Inches
import pandas as pd

document = Document()
df = pd.read_excel ("D:\OneDrive\Escritorio\Prueba Informe\datos.xlsx")


document.add_page_break()
document.save('maqueta.docx')