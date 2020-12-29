from flask import Flask, url_for, request, redirect, abort, jsonify, session
from trainingrecordsDAO import trainingDAO

app = Flask(__name__, 
            static_url_path='', 
            static_folder='staticpages')
            
app.secret_key = 'SecretDataRep'


#index
@app.route('/')
def index():
    #return "hello"
    count=0
    count+=1

    if not 'counter' in session:
        session['counter'] =0
        print("new session")

    sessionCount=session['counter']
    sessionCount+=1
    session['counter']=sessionCount

    

    pageContent="<h1>counts</h1>" +\
        "session Count ="+str(sessionCount) +\
        "<br/>this Count ="+str(count)
    
    return pageContent
    
@app.route('/clear')
def clear():
    #session.clear()
    session.pop('counter',None)   

    return "done"
    
#curl http://127.0.0.1:5000


#get all
@app.route('/training')
def getAll():
    return jsonify(trainingDAO.getAll())
#curl http://127.0.0.1:5000/training


#find by id
@app.route('/training/<int:userid>')
def findById(userid):
    return jsonify(trainingDAO.findById(userid))
#curl http://127.0.0.1:5000/training/1001

#create
@app.route('/training',methods=['POST'])
def create():
    if not request.json:
        abort(400)

    records = {
           "userid": request.json['userid'],
           "name": request.json['name'],
           "trainingrecord": request.json['trainingrecord'],
           "yearcompleted": request.json['yearcompleted'],
           "expiryyear": request.json['expiryyear']
    }
    return jsonify(trainingDAO.create(records)), 201
    return "served by Create "
# curl -X POST -d "{\"userid\":1002, \"name\":\"Joe Bloggs\", \"trainingrecord\":\"Safe Pass\", \"yearcompleted\":2019, \"expiryyear\":2023}" -H Content-Type:application/json http://127.0.0.1:5000/training

# update
@app.route('/training/<int:userid>',methods=['PUT'])
def update(userid):
    foundtraining=trainingDAO.findById(userid)
    print(foundtraining)
    if foundtraining == {}:
        return jsonify({}), 404
        
    currentRecord = foundtraining
    if 'name' in request.json:
        currentRecord['name'] = request.json['name']
    if 'trainingrecord' in request.json:
        currentRecord['trainingrecord'] = request.json['trainingrecord']
    if 'yearcompleted' in request.json:
        currentRecord['yearcompleted'] = request.json['yearcompleted']
    if 'expiryyear' in request.json:
        currentRecord['expiryyear'] = request.json['expiryyear']  
    trainingDAO.update(currentRecord)
    
    return jsonify(currentRecord)
# curl -X PUT -d "{\"name\":\"Joe Blond\", \"Year Completed\":2018}" -H content-type:application/json http://127.0.0.1:5000/training/1001
# delete
@app.route('/training/<int:userid>',methods=['DELETE'])
def delete(userid):
    trainingDAO.delete(userid)
    return jsonify({"done": True})
# curl -X DELETE http://127.0.0.1:5000/training/1001
if __name__ == "__main__":
    app.run(debug=True)