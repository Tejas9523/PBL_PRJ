from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        """Function Declaration"""
    return render_template('index.html')

if __name__== "__main__":
    app.run(debug=True)

