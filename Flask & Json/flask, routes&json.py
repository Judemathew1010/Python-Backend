from flask import Flask, jsonify #creating flask class

app = Flask(__name__) #creating instance of flask class

@app.route('/api/AiBusinessCard', methods = ['GET'])
def get_article():
    businesscard = [
                    {'id':1,'name':'name','job title':'job_title','name':'name',},
                    {'id':2,'address':'address','company':'company','email':'email',},
                    {'id':3,'website':'website',}
                    ]
    return jsonify(businesscard)

if __name__ == "__main__":
    app.debug = True 
    app.run(host='0.0.0.0', port =5000)
   
