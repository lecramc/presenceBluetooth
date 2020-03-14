import pymysql
from bluepy.btle import Scanner, DefaultDelegate
import FenMain
#import os
#import time
con = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='bluetooth')

def commit(monCurseur, maVar):
    try:
        monCurseur.execute(maVar)
        con.commit()
    finally:
        con.close()


class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

scanner = Scanner().withDelegate(ScanDelegate())
device = []
devices = scanner.scan(10.0)
cursor = con.cursor()
for dev in devices:
    for (adtype, desc, value) in dev.getScanData():
        print("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
        print("  %s =  %s " % (desc, value))
        tupleDevice = (value, dev.addr)
        device.append(tupleDevice)
        sql = "INSERT INTO Appel(DateHeure) VALUES (CURRENT_TIMESTAMP)"
        commit(cursor,sql)
        FenMain.FenMain(device)
#print(name)
#time.sleep(10.0)


