from fpdf import FPDF
import os
from spanish_date import getSpanishStringDate

AREA = 'AREA'
ALUMNO = 'ALUMNO'
FECHA = 'FECHA'
BOLETA = 'BOLETA'

DOCUMENT_KEY = "SSEIS/050/2021"

SIGNER_NAME = "M. EN C. EDGARDO ADRIÁN FRANCO HERNÁNDEZ"

LOGO_IPN = "./src/logoipn.png"
LOGO_ESCOM = "./src/logoescom.png"
TEMPLATE_TEXT = "./src/body.txt"

TITLE_ROW_ACTIVITIES = ["Profesor/Responsable", "Horas", "Semestre"]


INPUT_DATA_PATH = "./input_data"
OUTPUT_DATA_PATH = "./output_data"


class PersonalData:
    def __init__(self):
        pass

    #def __init__(self, filename : str):
        #self.dataFromFile(filename)

    def dataFromFile(self, filename : str):
        with open(filename, 'rb') as personal_data_namefile:
            self.rows = []
            self.data_rows = int(personal_data_namefile.readline().decode('UTF-8'))

            for i in range(self.data_rows):
                data_row = personal_data_namefile.readline().decode('UTF-8')
                self.rows.append(data_row.split(','))
            
            self.area = personal_data_namefile.readline().decode('UTF-8').strip('\n')
            self.id_number = personal_data_namefile.readline().decode('UTF-8').strip('\n')
            self.name = personal_data_namefile.readline().decode('UTF-8').strip('\n')
            self.date = personal_data_namefile.readline().decode('UTF-8').strip('\n')
    
    def setName(self, name: str):
        self.name = name

    def setArea(self, area):
        self.area = area

    def setNumberRows(self, nrows):
        self.data_rows = nrows

    def setRows(self, rows):
        self.rows = rows

    def setIdNumber(self, id_number):
        self.id_number = id_number

    def getName(self) -> str:
        return self.name

    def getArea(self) -> str:
        return self.area
    def getNumberRows(self) -> int:
        return self.data_rows

    def getRows(self) -> list:
        return self.rows

    def getIdNumber(self) -> str:
        return self.id_number



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

     def body(self, name: str, personal_data : PersonalData):
        #txt = ""
        with open(name, 'rb') as template_document:
            template_str = template_document.readline().decode('UTF-8')
            footer = template_document.readline().decode('UTF-8')
            
        #personal_data = PersonalData(personal_data_namefile)

        area = personal_data.getArea()
        alumno = personal_data.getName().upper()
        fecha = getSpanishStringDate()
        boleta = personal_data.getIdNumber()

        data_rows = personal_data.getNumberRows()
        rows = personal_data.getRows()

        template_str = template_str.replace(AREA, area)
        template_str = template_str.replace(ALUMNO, alumno)
        template_str = template_str.replace(BOLETA, boleta)
        footer = footer.replace(FECHA, fecha)

        #self.set_xy(10.0, self.get_y() +  12)    
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, template_str)


        th = self.font_size
        epw = self.w -  2 * self.l_margin
 

        columns_width = [epw /  3, epw / 3, epw / 3]
        final_row = ["Total", "", ""]
        total_hours = 0
        for row in rows:
            total_hours += int(str(row[1]).rstrip('\n'))
        final_row[1] = total_hours
        rows.append(final_row)


        # Set column width to 1/4 of effective page width to distribute content 
        # evenly across table and page
        #col_width = epw / 4
    
        #self.set_xy(10.0, 80.0)  
        self.set_font('Arial', 'B', 10)

        for data, col_width in zip(TITLE_ROW_ACTIVITIES, columns_width):
            self.cell(col_width, 1.1 * th, str(data), align = 'C', border = 1)
        self.ln(1.1 * th)
        self.set_font('Arial', '', 10)
            
        for row in rows:
            for datum, col_width in zip(row, columns_width):
                # Enter data in colums
                self.cell(col_width, 1.1 * th, str(datum).rstrip('\n'), align = 'C', border = 1)
 
            self.ln(1.1*th)

        self.set_font('Arial', '', 12)
        self.set_xy(10.0, self.get_y() + data_rows)  #self.set_xy(10.0, 80.0 + 2 * 2 * th  * (data_rows + 1))  
        self.multi_cell(0, 10, footer)

        self.set_font('Arial', 'B', 10)
        self.set_xy(0.0, self.get_y())
        self.multi_cell(w = 0.0, h = 10.0, align = 'C', txt = "ATENTAMENTE", border = 0)
        self.multi_cell(w = 0.0, h = 0.0, align = 'C', txt = f"\"LA TÉCNICA AL SERVICIO DE LA PATRIA\"", border = 0)
        self.set_xy(0.0, self.get_y() + 25)

        sign_details = f"{SIGNER_NAME}\nREPRESENTANTE DEL CLUB DE ALGORITMIA\n"
        self.multi_cell(w = 0.0, h = 5.0, align = 'C', txt = sign_details, border = 0)

     def generatePDF(self, output_name : str, personal_data : PersonalData):
        if not os.path.exists(INPUT_DATA_PATH):
            os.mkdir(INPUT_DATA_PATH)

        if not os.path.exists(OUTPUT_DATA_PATH):
            os.mkdir(OUTPUT_DATA_PATH)
            
        self.add_page()
        self.imagex()
        self.titles()
        self.body(TEMPLATE_TEXT, personal_data)
        print(output_name)
        self.output(output_name, 'F')
        
    