from document_generator import Document, INPUT_DATA_PATH, OUTPUT_DATA_PATH
import os
if __name__ == '__main__':

    files = os.listdir(INPUT_DATA_PATH)
   
    for f in files:
        filename = ".".join(f.split('.')[0:-1])
        
        input_name = f"{INPUT_DATA_PATH}/{f}"
        output_name = f"{OUTPUT_DATA_PATH}/{filename}.pdf"
        pdf = Document()
        pdf.generatePDF(input_name, output_name)

    