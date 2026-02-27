from flask import Flask, render_template, request, flash, url_for, redirect,session
import mysql.connector
import os
from datetime import datetime


app = Flask(__name__)
app.secret_key =os.getenv("SECRET_KEY")

def get_db_connector():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("DB_PASS"),
        database="expense_tracker",
        autocommit=True
    )

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        amount = request.form.get("amount")

        if not name or not amount:
            flash("Enter all details")
            return redirect(url_for("home"))

        db = get_db_connector()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO expenses(name, amount,date) VALUES(%s, %s,%s)",
            (name, amount,datetime.now())
        )
        cursor.execute(
            "select name,amount from expenses where DATE(date)=CURDATE()"
        )
        users=cursor.fetchall()

        os.makedirs("main", exist_ok=True)
        today = datetime.now().strftime("%Y-%m-%d")
        file_path = f"main/{today}.csv"

        with open(file_path, "w") as f:
            f.write("Item,Amount\n")
            for user in users:
                f.write(f"{user[0]},{user[1]}\n")

        flash("Saved successfully")
        return redirect(url_for("home"))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True,use_reloader=False)
