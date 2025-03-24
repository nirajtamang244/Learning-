from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/divide', methods=['GET'])
def divide():
    try:
        a = request.args.get('a', type=float)
        b = request.args.get('b', type=float)

        if a is None or b is None:
            raise ValueError("Missing parameters 'a' or 'b'")

        result = a / b
        return jsonify({"result": result})

    except ZeroDivisionError:
        return jsonify({"error": "Cannot divide by zero"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


if __name__== "__main__":
    app.run(debug=True)