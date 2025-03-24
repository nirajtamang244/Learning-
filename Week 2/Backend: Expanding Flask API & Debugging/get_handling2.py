from flask import Flask,jsonify,request


app= Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', default="Guest")
    return jsonify({"message": f"Hello, {name}!"})


@app.route('/add', methods=['POST'])
def add():
    try:
        data = request.get_json()
        a = data.get("a")
        b = data.get("b")

        if a is None or b is None:
            raise ValueError("Missing 'a' or 'b' in request body")

        return jsonify({"result": a + b})
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__=="__main__":
    app.run()