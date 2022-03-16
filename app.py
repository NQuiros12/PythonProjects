from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        df = pd.read_csv(request.files.get('file'))
        return render_template('upload.html', shape = df.shape)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run('0.0.0.0',5000,debug=True)
