from flask import Flask
naya= Flask(__name__)

@naya.route("/")
def ask():
    return "hello yaar"

@naya.route("/user/<name>")
def use(name):
    return f"Hello {name}"

@naya.route("/sq/<int:num>")
def square(num):
    return f" the square is {num**2}"

@naya.route("/multiply/<int:a>/<int:b>")
def muil(a,b):
    return f"{a}x{b}= {a*b}"
    

@naya.route("/divide/<int:a>/<int:b>")
def division(a,b):
    try:
        result= a/b
        return f" when we divide {a} from {b}, we get the value: {result}"
    except ZeroDivisionError:
        return f"Erroe: Division by zero is not allowed"
    
if __name__== "__main__":
    naya.run(port= 3737,debug=True)
