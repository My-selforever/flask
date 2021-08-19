from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    {
        'id': 1,
        'name': 'Raju',
        'done': 'false',
        'contact':'9987644456'
    },
    {
        'id': 2,
        'name': 'Rahul',
        'done': 'false',
        'contact':'9876543222'
    }
]




@app.route("/get-data")
def getTask():
    return jsonify({'data': data})


@app.route("/update-data",methods=["POST"])
def updatedata():
    if not request.json:
        return jsonify({'Status': 'error', 'description': 'enterData'})
    dat = {
        'id':data[-1]['id']+1,
        'name': request.json['name'],
        'done': request.json['done'],
        'contact':request.json['contact'],
    }
    data.append(dat)
    return jsonify ({'status':'successful','Description':'Data Updated'})

if(__name__ == "__main__"):
    app.run(debug=True)
