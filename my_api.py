from crypt import methods
from urllib import request
from flask import Flask,jsonify,request
import math 


app = Flask(__name__)


def validate(x):

    num = str(x)

    if num[::-1].find('.') == 4:
        return True
    else:
        return False


def calc_D(X,Y,Z):
    D =  (((Y-((Z/2)*Y/(((Y*Y/X)+X)/2))) * (Y-((Z/2)*Y/(((Y*Y/X)+X)/2)))) /(X-((Z/2)-((Z/2)*math.cos((math.radians(
            math.degrees(math.asin(math.radians(math.degrees(Y/(((Y*Y/X)+X)/2)))))))))))) +(X-((Z/2)-((Z/2)*math.cos((math.radians(
            math.degrees(math.asin(math.radians(math.degrees(Y/(((Y*Y/X)+X)/2)))))))))))
    return D
    

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/model/',methods=['GET'])
def model():
    data = request.args.to_dict()
    model = data['model']
    X = data['X']
    Y,Z = model.split('x')
    X = float(X)
    Y = float(Y)
    Z = float(Z)
    if(validate(X)):
        return jsonify({"D": calc_D(X,Y,Z)})
    else:
        return jsonify({"error": "400 BAD request"})

            

if __name__ == '__main__':
    app.run(debug=True)