from flask import Flask, render_template, request
app = Flask(__name__)


calculation_history = []

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        num1 = float(request.form.get("num1"))
        num2 = float(request.form.get("num2"))
        operation = request.form.get("operation")

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                result = "Cannot divide by zero"
            else:
                result = num1 / num2
        else:
            result = "Invalid Operation"

        
        calculation = {
            "num1": num1,
            "num2": num2,
            "operation": operation,
            "result": result
        }

        calculation_history.append(calculation)

        
        if len(calculation_history) > 5:
            calculation_history.pop(0)

        return render_template(
            "result.html",
            num1=num1,
            num2=num2,
            operation=operation,
            result=result
        )

    except Exception:
        return "Invalid Input"


@app.route("/greet/<username>")
def greet(username):
    return render_template("greet.html", username=username)


@app.route("/history")
def history():
    return render_template("history.html", history=calculation_history)



@app.errorhandler(405)
def method_not_allowed(e):
    return "<h2>Method Not Allowed</h2>", 405


if __name__ == "__main__":
    app.run(debug=True)