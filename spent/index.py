from flask import Flask, redirect, url_for, request, render_template, make_response
import sqlite3
import csv
from datetime import datetime
from io import StringIO
app = Flask(__name__)

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      thing = request.form['thing']
      spent = request.form['spent']
      if thing and spent:
         conn = sqlite3.connect('spent.db')
         c = conn.cursor()
         c.execute("INSERT INTO SPENT (DATE, MONTH, THING, AMOUNT) VALUES (date('now'), strftime('%m', 'now'), ?, ?)", (thing, spent))
         conn.commit()
         conn.close()
         return render_template('index.html')
      return render_template('index.html')
   else:
      return render_template('index.html')
   
@app.route('/get_data', methods=['POST', 'GET'])
def get_data():
   if request.method == 'GET':
      conn = sqlite3.connect('spent.db')
      c = conn.cursor()
      c.execute('SELECT * FROM SPENT')
      data = c.fetchall()
      conn.close()
      buffer = StringIO()
      writer = csv.writer(buffer, delimiter='\t')

    # Write the headers and data to the buffer
      writer.writerow(['ID', 'DATE', 'MONTH', 'THING', 'AMOUNT'])
      for row in data:
         writer.writerow(row)
         

    # Return the TSV data
      return buffer.getvalue()
   
@app.route('/show_data', methods=['POST'])
def show_data():
   month = request.form['month']
   conn = sqlite3.connect('spent.db')
   c = conn.cursor()
   c.execute("SELECT * FROM SPENT WHERE MONTH = ?", (month,))
   rows = c.fetchall()
   conn.close()
   buffer = StringIO()
   writer = csv.writer(buffer, delimiter='\t')

    # Write the headers and data to the buffer
   writer.writerow(['ID', 'DATE', 'MONTH', 'THING', 'AMOUNT'])
   for row in rows:
      row = list(row)
      row[1] = datetime.strptime(row[1], '%Y-%m-%d').strftime('%m/%d/%Y')
      writer.writerow(row)
    # Return the TSV data

   buffer.seek(0) 
   response = make_response(buffer.getvalue())
   response.headers['Content-Disposition'] = 'attachment; filename=data.csv'
   response.headers['Content-Type'] = 'text/csv'

   return response
   # return buffer.getvalue()


if __name__ == '__main__':
   app.run(debug = True)