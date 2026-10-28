from fpdf import FPDF


class PDF(FPDF):
    def add_shirt_image(self):
        self.set_font('Helvetica', size=50, style = "B")
        self.cell(w=0, h=70, text="CS50 Shirtificate", border=0, align="C")
        self.image("shirtificate.png", x=15, y=80, w=180)
        

    def add_name(self, name):
        self.set_font('Helvetica', size=30, style = "B")
        self.set_text_color(255, 255, 255)
        self.set_xy(x=0, y=135)
        self.cell(w=0, h=10, text=f"{name} took CS50", border=0, align="C")


def main():
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.add_shirt_image()
    name = input("Name: ")
    pdf.add_name(name)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()