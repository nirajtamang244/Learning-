"""Modifying the API to return a custom error message if negative numbers are provided.
Adding a try-except block to catch general exceptions and return a "Something went wrong" message"""

from flask import Flask, jsonify,request

app= Flask(__name__)

@app.route("/",methods=["GET"])
def home():
    return jsonify("Welcome to the home Page!")

@app.route("/divide", methods= ["GET"])
def divide():
    try:
        a= request.args.get("a",type=float)
        b=request.args.get("b",type= float)

        if a is None or b is None:
            raise ValueError("Please enter a correct value")
        if a<0  or b<0:
            raise ValueError("Do not enter a negative number")
        
        total= a/b
        return jsonify({"result":total})
    
    except ZeroDivisionError:
        return jsonify({"error":"cannot divide by zero"})
    
    except ValueError as e:
        return jsonify({"Error":str(e)})
    
    except Exception:
        return jsonify({"error":"something went wrong"}) 


if __name__=="__main__" :
    app.run(debug=True, port= 8000) 