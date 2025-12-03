from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

calorie_entries = []
DAILY_GOAL = 2000  


@app.route("/")
def index():
    total_calories = sum(item["calories"] for item in calorie_entries)
    remaining = DAILY_GOAL - total_calories
    return render_template(
        "index.html",
        total_calories=total_calories,
        goal=DAILY_GOAL,
        remaining=remaining
    )


@app.route("/add", methods=["GET", "POST"])
def add_food():
    if request.method == "POST":
        name = request.form.get("name")
        calories_str = request.form.get("calories", "0")

        try:
            calories = int(calories_str)
        except ValueError:
            calories = 0

        calorie_entries.append({"name": name, "calories": calories})
        return redirect(url_for("summary"))

    return render_template("page1.html")  


@app.route("/summary")
def summary():
    total_calories = sum(item["calories"] for item in calorie_entries)
    return render_template("page2.html", entries=calorie_entries, total_calories=total_calories)


if __name__ == "__main__":
    app.run(debug=True)
