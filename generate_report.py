from fpdf import FPDF
import os

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", "B", 16)

pdf.cell(200, 10, "Healthcare Survey Report", ln=True, align="C")
pdf.ln(10)

pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, "This report presents visual analysis of healthcare survey data, including satisfaction levels, service availability, and hygiene conditions in hospitals.")

chart_folder = "charts/"
if os.path.exists(chart_folder):
    for image in sorted(os.listdir(chart_folder)):
        if image.endswith(".png"):
            pdf.add_page()
            pdf.set_font("Arial", "B", 14)
            pdf.cell(200, 10, image.replace("_", " ").replace(".png", "").title(), ln=True, align="C")
            pdf.ln(10)
            pdf.image(os.path.join(chart_folder, image), x=30, w=150)
else:
    pdf.cell(200, 10, "No charts found! Run visualize_healthcare.py first.", ln=True, align="C")

pdf.output("Healthcare_Survey_Report.pdf")
print("PDF report generated: Healthcare_Survey_Report.pdf")
