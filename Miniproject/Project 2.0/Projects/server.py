from amazon import main
import csv
from flask import Flask,redirect, request,render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("MiniFrontEnd.html")

@app.route("/products",methods=["POST"])
def submit():
    product = request.form["product"]
    print(product)
    main(product)
    return redirect("/csv")


@app.route('/csv')
def csv_table():
    data = []
    with open('data.csv', 'r',encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return render_template('table.html', data=data)

if __name__ == "__main__":
    app.run()