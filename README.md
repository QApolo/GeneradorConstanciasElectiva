# Generador Constancias Electiva ESCOM
Script Python 3 that generates pdf files for IPN ESCOM

## Requirements
* Python 3+
* fpdf

### fpdf Install
You can install fpdf through pip package installer

* See [Link](https://pypi.org/project/fpdf/), [Link 2](https://pyfpdf.readthedocs.io/en/latest/)  for more details 

you may need to provide super user privileges e.g 
```bash
sudo pip3 install fpdf
```

## Usage
<!---
This script takes input from files inside folder **input_data** by default, this does not exist in the repo, you can either create it yourself or execute the main.py once.

```bash
python3 main.py
```

Inside this new folder you should put txt files following the structure shown in the next example:

```
3
Club de algoritmia, Nombre Profesor, 100, 2
Club de algoritmia, Nombre Profesor, 100, 2
Club de algoritmia, Nombre Profesor, 100, 2
Area a la que pertenece
Nombre completo con apellidos
a los dieciocho dias del mes de marzo del dos mil veintiuno
```

>where in this case 3 indicates the number of rows that the table within the document will have, and the next 3 lines describe the table content separated by comma

after these 3 lines you must specify the area
and lastly a detailed date in spanish

-->
This script takes a CSV file as input
```bash
python3 main.py file.csv
```
```

The csv file must have a structure like the following
4,,,
Edgardo Adrián Franco Martínez,64,16-2
Edgardo Adrián Franco Martínez,64,17-1
Edgardo Adrián Franco Martínez,64,17-2
Edgardo Adrián Franco Martínez,64,18-1
Independientes,,,
2014630138,,,
Hugo Michel Barbosa Lopez,,,
A los diecinueve días del mes,,,
,,,
2,,,
Edgardo Adrián Franco Martínez,64,16-2
Edgardo Adrián Franco Martínez,64,16-2
Independientes,,,
2016630138,,,
Isaac Sanchez Aguilar,,,
A los diecinueve días del mes,,,
