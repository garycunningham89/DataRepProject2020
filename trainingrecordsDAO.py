import mysql.connector
from mysql.connector import cursor
import dbconfigtemplate as cfg
    #def __init__(self):
     #   self.db = mysql.connector.connect(
      #      host = 'localhost',
       #     user = 'root',
        #    password= '',
         #   database = 'datarepproject'
          #  )
        #print('connection made')
class TrainingDAO:
    db = ""
    def connectToDB(self):
        self.db = mysql.connector.connect(
            host =      cfg.mysql['host'],
            user =      cfg.mysql['username'],
            password=   cfg.mysql['password'],
           database =  cfg.mysql['database']
        )
    def __init__(self):
        self.connectToDB()
    #print('connection made')

    def getCursor(self):
       if not self.db.is_connected():
          self.connectToDB()
       return self.db.cursor()

    def create(self, record):
        cursor = self.db.cursor()
        sql = "Insert into training (userid, name, trainingrecord, yearcompleted, expiryyear) values (%s,%s,%s,%s,%s)"
        values = [
            record['userid'],
            record['name'],
            record['trainingrecord'],
            record['yearcompleted'],
            record['expiryyear']
            ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid
        
    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from training'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
        
        return returnArray

    def findById(self, userid):
        cursor = self.db.cursor()
        sql = 'select * from training where userid = %s'
        values = [ userid ]
        values = [ userid ]
        cursor.execute(sql,values)
        result = cursor.fetchone()
        return self.convertToDict(result)
    
    def update(self, record):
        cursor = self.db.cursor()
        sql = "update training set name = %s, trainingrecord = %s, yearcompleted = %s, expiryyear = %s where userid = %s" 
        values = [
            record['userid'],
            record['name'],
            record['trainingrecord'],
            record['yearcompleted'],
            record['expiryyear']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return record
        
    def delete(self, userid):
        cursor = self.db.cursor()
        sql = 'delete from training where userid = %s'
        values = [userid]
        cursor.execute(sql,values)
        return {}
        
    def convertToDict(self, result):
        colnames = ['userid','name','trainingrecord','yearcompleted','expiryyear']
        record = {}
        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                record[colName] = value
            return record
trainingDAO = TrainingDAO()