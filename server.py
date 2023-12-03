from flask import Flask,jsonify,request
from json import load,loads

app = Flask(__name__)

def openSrc():
    with open("public/data/data.json","r",encoding="utf-8") as src:
        data = load(src)
        return data
def found(array,name):
    for company in array:
        if company["companyName"] == name:
            return company

@app.route("/members")
def members():
    return {"members":["member1","member2","member3","member4"]}

@app.route("/api/getCompany")
def getCompany():
    with open("public/data/data.json","r",encoding="utf-8") as src:
        data = load(src)
        response = jsonify([item["companyName"] for item in data["company"]])
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

@app.route("/api/getProduct")
def getProduct():
    selected_data = request.args.get('company')
    print(selected_data)
    if (selected_data == "undefined"):
        return jsonify("false")
    return jsonify(found(openSrc()["company"],selected_data))

if __name__ == "__main__":
    app.run(debug=True)