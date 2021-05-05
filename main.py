from document_generator import Document
from personal_data_model import PersonalData
import os
import sys

OUTPUT_DATA_PATH = "./output_data"
INPUT_CSV = "./input_data.csv"

if __name__ == '__main__':

    if not os.path.exists(OUTPUT_DATA_PATH):
        os.mkdir(OUTPUT_DATA_PATH)

    personal_data_list = []
    fileInputName = INPUT_CSV

    if len(sys.argv) > 1:
        fileInputName = sys.argv[1]

    with open(fileInputName, 'rb') as pd_file:
        while True:
            line = pd_file.readline()
            if not line:
                break
            
            clean = lambda s: s.decode('UTF-8').rstrip(",\n\r ").lstrip(",\n\r ")

            if clean(line) == "":
                continue
            pd = PersonalData()
            rows = []

            num_str = clean(line)
            nrows = int(num_str)
            
            for i in range(nrows):
                row = clean(pd_file.readline())
                rows.append(row.split(","))

            id_number = clean(pd_file.readline())
            area = "independientes" #clean(pd_file.readline())
            name = clean(pd_file.readline())
            
            pd.setArea(area)
            pd.setIdNumber(id_number)
            pd.setName(name)
            pd.setNumberRows(nrows)
            pd.setRows(rows)

            personal_data_list.append(pd)
    for pd in personal_data_list:
        pdf = Document()
        pdf.generatePDF(f"{OUTPUT_DATA_PATH}/{pd.getName()}.pdf", pd)