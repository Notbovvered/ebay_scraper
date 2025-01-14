from flask import Flask, render_template
import csv

app = Flask(__name__)

# Route to display the CSV data
@app.route("/")
def display_csv():
    data = []
    with open("iphone 14.csv", newline="") as csvfile:
        csvreader = csv.reader(csvfile)
        headers = next(csvreader)  # Get headers
        for row in csvreader:
            data.append(row)
    return render_template("index.html", headers=headers, data=data)

if __name__ == "__main__":
    app.run(debug=True)