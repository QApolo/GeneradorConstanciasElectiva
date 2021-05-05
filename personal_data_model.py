class PersonalData:    
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