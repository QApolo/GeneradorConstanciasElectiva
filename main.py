from fpdf import FPDF
import os

AREA = 'AREA'
ALUMNO = 'ALUMNO'
FECHA = 'FECHA'

DOCUMENT_KEY = "SSEIS/050/2021"


LOGO_IPN = "./logoipn.png"
LOGO_ESCOM = "./logoescom.png"

TITLE_ROW_ACTIVITIES = ["Actividad", "Profesor/Responsable", "Horas", "Semestre"]

INPUT_DATA_PATH = "./input_data"
OUTPUT_DATA_PATH = "./output_data"

class Document(FPDF):
     def imagex(self):
        self.set_xy(6.0, 12.0)
        self.image(LOGO_IPN, link = '', type = '', w = 1200 / 30, h = 852 / 30)
        self.set_xy(163.0, 12.0)
        self.image(LOGO_ESCOM,  link = '', type = '', w = 262 / 8, h = 200 / 8)

     def titles(self):
        self.set_xy(0.0, 0.0)
        self.set_font('Arial', 'B', 12)
        self.set_text_color(220, 50, 50)
        self.cell(w = 210.0, h = 40.0, align = 'C', txt = "INSTITUTO POLITÉCNICO NACIONAL", border = 0)
        self.set_xy(0.0,6.0)

        self.set_text_color(10, 110, 231)
        self.multi_cell(w = 210.0, h = 40.0, align = 'C', txt = "ESCUELA SUPERIOR DE CÓMPUTO", border = 0)

        self.set_font('Arial', '', 12)
        self.set_text_color(0, 0, 0)
        self.set_xy(0.0,12.0)
        self.multi_cell(w = 210.0, h = 40.0, align = 'C', txt = "SUBDIRECCIÓN DE SERVICIOS EDUCATIVOS", border = 0)
        self.set_xy(0.0,18.0)
        self.multi_cell(w = 210.0, h = 40.0, align = 'C', txt = "E INTEGRACIÓN SOCIAL", border = 0)

        self.set_xy(0.0,24.0)
        self.multi_cell(w = 210.0, h = 40.0, align = 'C', txt = "DEPARTAMENTO DE SERVICIOS", border = 0)

        self.set_xy(0.0,30.0)
        self.multi_cell(w = 210.0, h = 40.0, align = 'C', txt = "ESTUDIANTILES", border = 0)

        self.set_xy(0.0, 42.0)
        self.set_font('Arial', 'B', 14)
        self.multi_cell(w = 210.0, h = 40.0, align = 'C', txt = "CONSTANCIA", border = 0)
        self.set_font('Arial', 'B', 12)

        self.set_xy(0.0, 52.0)
        self.multi_cell(w = 210.0, h = 40.0, align = 'C', txt = DOCUMENT_KEY, border = 0)
        self.set_font('Arial', '', 12)

     def body(self,name, personal_data_namefile):
        #txt = ""
        with open(name, 'rb') as template_document:
            template_str = template_document.readline().decode('UTF-8')
            footer = template_document.readline().decode('UTF-8')
            
        with open(personal_data_namefile, 'rb') as personal_data_doc:
            self.rows = []
            data_rows = int(personal_data_doc.readline().decode('UTF-8'))

            for i in range(data_rows):
                data_row = personal_data_doc.readline().decode('UTF-8')
                self.rows.append(data_row.split(','))
            
            area = personal_data_doc.readline().decode('UTF-8').strip('\n')
            alumno = personal_data_doc.readline().decode('UTF-8').strip('\n')
            fecha = personal_data_doc.readline().decode('UTF-8').strip('\n')
        
        template_str = template_str.replace(AREA, area)
        template_str = template_str.replace(ALUMNO, alumno)
        footer = footer.replace(FECHA, fecha)

        #self.set_xy(10.0, self.get_y() +  12)    
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, template_str)


        th = self.font_size
        epw = self.w -  2 * self.l_margin
 
        # Set column width to 1/4 of effective page width to distribute content 
        # evenly across table and page
        col_width = epw / 4

        #self.set_xy(10.0, 80.0)  
        self.set_font('Arial', 'B', 10)

        for data in TITLE_ROW_ACTIVITIES:
            self.cell(col_width, 2 * th, str(data), border = 1)
        self.ln(2 * th)
        self.set_font('Arial', '', 10)
            
        for row in self.rows:
            for datum in row:
                # Enter data in colums
                self.cell(col_width, 2.1 * th, str(datum).rstrip('\n'), border = 1)
 
            self.ln(2.1*th)

        self.set_font('Arial', '', 12)
        self.set_xy(10.0, self.get_y() + data_rows)  #self.set_xy(10.0, 80.0 + 2 * 2 * th  * (data_rows + 1))  
        self.multi_cell(0, 10, footer)

        self.set_font('Arial', 'B', 10)
        self.set_xy(0.0, self.get_y())
        self.multi_cell(w = 0.0, h = 10.0, align = 'C', txt = "ATENTAMENTE", border = 0)
        self.multi_cell(w = 0.0, h = 0.0, align = 'C', txt = f"\"LA TÉCNICA AL SERVICIO DE LA PATRIA\"", border = 0)
        self.set_xy(0.0, self.get_y() + 25)

        signer_name = "M. EN C. JOSÉ ASUNCIÓN ENRÍQUEZ ZÁRATE"
        sign_details = f"{signer_name}\nSUBDIRECTOR DE SERVICIOS EDUCATIVOS\nE INTEGRACIÓN SOCIAL"
        self.multi_cell(w = 0.0, h = 5.0, align = 'C', txt = sign_details, border = 0)

     def generatePDF(self, input_name, output_name):
        if not os.path.exists(INPUT_DATA_PATH):
            os.mkdir(INPUT_DATA_PATH)

        if not os.path.exists(OUTPUT_DATA_PATH):
            os.mkdir(OUTPUT_DATA_PATH)
            
        self.add_page()
        self.imagex()
        self.titles()
        self.body("body.txt", input_name)
        print(output_name)
        self.output(output_name, 'F')
        
if __name__ == '__main__':

    files = os.listdir(INPUT_DATA_PATH)
   
    for f in files:
        filename = ".".join(f.split('.')[0:-1])
        
        input_name = f"{INPUT_DATA_PATH}/{f}"
        output_name = f"{OUTPUT_DATA_PATH}/{filename}.pdf"
        pdf = Document()
        pdf.generatePDF(input_name, output_name)

    