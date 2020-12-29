from trainingrecordsDAO import trainingDAO

record1 = {
    'userid': 1002,
    'name': 'John Does',
    'trainingrecord': 'Safe Pass',
    'yearcompleted': 2012,
    'expiryyear': 2015
}

record2 = {
    'userid': 1001,
    'name': 'Jane Doe',
    'trainingrecord': 'Safe Pass',
    'yearcompleted': 2022,
    'expiryyear': 2025
}
#trvalue = trainingDAO.create(record)
returnValue = trainingDAO.findById(record2['userid'])
print(returnValue)
returnValue = trainingDAO.update(record2)
print(returnValue)
returnValue = trainingDAO.findById(record2['userid'])
print(returnValue)
returnValue = trainingDAO.delete(record2['userid'])
print(returnValue)