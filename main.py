from document_generator import Document, PersonalData ,INPUT_DATA_PATH, OUTPUT_DATA_PATH
import os
import sys

INPUT_CSV = "./input_data.csv"
if __name__ == '__main__':

    files = os.listdir(INPUT_DATA_PATH)
    personal_data_list = []

    fileInputName = INPUT_CSV

    if len(sys.argv) > 1:
        fileInputName = sys.argv[1]

    with open(fileInputName, 'rb') as pd_file:
        while True:
            line = pd_file.readline()
            if not line:
                break

            if line.decode('UTF-8').rstrip("\n\r ") == ",,,":
                continue
            pd = PersonalData()
            rows = []

            clean = lambda s: s.decode('UTF-8').rstrip(",\n\r ").lstrip(",\n\r ")

            num_str = clean(line)
            nrows = int(num_str)
            
            for i in range(nrows):
                row = clean(pd_file.readline())
                rows.append(row.split(","))

            area = clean(pd_file.readline())
            name = clean(pd_file.readline())
            date = clean(pd_file.readline())
            
            pd.setArea(area)
            pd.setName(name)
            pd.setDate(date)
            pd.setNumberRows(nrows)
            pd.setRows(rows)

            personal_data_list.append(pd)
    for pd in personal_data_list:
        pdf = Document()
        pdf.generatePDF(f"{OUTPUT_DATA_PATH}/{pd.getName()}.pdf", pd)
    

    ### With txt file converting DEPRECATED
    """for f in files:
        filename = ".".join(f.split('.')[0:-1])
        
        input_name = f"{INPUT_DATA_PATH}/{f}"
        output_name = f"{OUTPUT_DATA_PATH}/{filename}.pdf"
        pdf = Document()
        pdf.generatePDF(input_name, output_name, personal_data)
    """
    