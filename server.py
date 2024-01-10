from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
	return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

def write_to_file(data):
	with open('./database.txt','a') as database:
		info = f"Email: {data['email']}, Subject: {data['subject']}\nMessage:{data['message']}\n"
		database.write(info)


def write_to_csv(data):
	with open('./database.csv','a',newline='') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']

		csv_writer = csv.writer(database,delimiter =',')
		csv_writer.writerow([email,subject,message])
		

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return render_template('thankyou.html',name = data['email'])
		except:
			return 'did not save to database'
	else:
		return 'fail to submit'
    

import csv

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])