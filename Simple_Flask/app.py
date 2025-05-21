from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.form)
    print(form_data)
    return form_data

if __name__ == "__main__":
    app.run(debug=True)
