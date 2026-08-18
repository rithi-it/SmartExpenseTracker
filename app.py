from flask import Flask, render_template, request

app = Flask(__name__)

expenses = []
budget = 0


@app.route("/")
def home():
    total = sum(x[1] for x in expenses)
    remaining = budget - total

    return render_template(
        "index.html",
        expenses=expenses,
        budget=budget,
        total=total,
        remaining=remaining
    )


@app.route("/budget", methods=["POST"])
def set_budget():
    global budget

    budget = float(request.form["budget"])

    return home()


@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    amount = float(request.form["amount"])

    expenses.append([name, amount])

    return home()


@app.route("/delete/<int:i>")
def delete(i):
    expenses.pop(i)

    return home()


if __name__ == "__main__":
    app.run()