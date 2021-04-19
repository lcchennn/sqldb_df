# import packages
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import lcchendb
import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

# parse github repo for csv file names
url = "https://github.com/lcchennn/sqldb_df/"
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc, "html.parser")
a_tags = soup.find_all('a')
urls = ['https://github.com/lcchennn/sqldb_df/'+re.sub('/blob', '', link.get('href'))
        for link in a_tags  if '.csv' in link.get('href')]
file_names = [url.split('.csv')[0].split('/')[url.count('/')] for url in urls]
files = ', '.join(file_names)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def hello(files=files):
    return render_template('index.html', files=files)

@app.route('/tables', methods=['post'])
def todf():
    csv_name = request.form.get('input_csv')
    path = r'https://raw.githubusercontent.com/lcchennn/sqldb_df/main/' + csv_name + '.csv'
    df = lcchendb.readtodf(path)
    tname = csv_name
    tshape = df.shape
    table = df.head(2).to_html()
    return render_template('tables.html', name=tname, table=table, tshape=tshape)

@app.route('/percentiles', methods=['post'])
def pct():
    csv_name = request.form.get('input_csv')
    input_pct = int(request.form.get('input_pct'))
    path = r'https://raw.githubusercontent.com/lcchennn/sqldb_df/main/' + csv_name + '.csv'
    df = lcchendb.readtodf(path)
    npct = lcchendb.npercnetile(df, input_pct)
    p_df = pd.DataFrame.from_dict(npct)
    result = p_df.to_html()
    return render_template('pct.html', name=csv_name, table=result, input_pct=input_pct)

@app.route('/enternew')
def new_student():
   return render_template('sqlitedb.html')

if __name__ == "__main__":
    app.run(debug=True)




