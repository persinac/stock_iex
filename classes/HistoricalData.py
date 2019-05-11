class HistoricalData:
    def __init__(self, id, symbolid, opendate, opener, closer,
                         high, low, volume, uopener, ucloser, uhigh, ulow,
                        uvolume, change, changepercent, label, createdon):
        self.id = id
        self.symbolid = symbolid
        self.opendate = opendate
        self.opener = opener
        self.closer = closer
        self.high = high
        self.low = low
        self.volume = volume
        self.uopener = uopener
        self.ucloser = ucloser
        self.uhigh = uhigh
        self.ulow = ulow
        self.uvolume = uvolume
        self.change = change
        self.changepercent = changepercent
        self.label = label
        self.createdon = createdon

    def __enter__(self):
        return self

    def createcommadelimitedvalueforinsert(self):
        retVal = ""
        retVal += "'" + self.symbolid + "'"
        retVal += ", '" + self.opendate + "'"
        retVal += ",'" + self.opener + "'"
        retVal += ",'" + self.closer + "'"
        retVal += ",'" + self.high + "'"
        retVal += ",'" + self.low + "'"
        retVal += ",'" + self.volume + "'"
        retVal += ",'" + self.uopener + "'"
        retVal += ",'" + self.ucloser + "'"
        retVal += ",'" + self.uhigh + "'"
        retVal += ",'" + self.ulow + "'"
        retVal += ",'" + self.uvolume + "'"
        retVal += ",'" + self.change + "'"
        retVal += ",'" + self.changepercent + "'"
        retVal += "," + str(self.label) + ""
        retVal += ",'" + self.createdon + "'"
        return retVal