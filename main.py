from flask import Flask, render_template

app = Flask(__name__)

LISTINGS  =  [
	{
		'id': 1,
		'title': 'title one',
    'post_date': 'Aug 14 2023',
		'due_date': 'Sep 1 2023',
    'description': 'some details about the task here, add as much as you need to',
		'price': '50',
    'contact_email': 'abc@123.com',
    'contact_phone': '123-456-7890',
    'contact_name': 'John Doe',
    'tags': ''
	},
	{
		'id': 2,
		'title': 'title two',
    'post_date': 'Aug 16 2023',
		'due_date': 'Sep 1 2023',
    'description': 'some details about the task here, add as much as you need to',
		'price': '50',
    'contact_email': 'abc@123.com',
    'contact_phone': '123-456-7890',
    'contact_name': 'John Doe',
    'tags': ''
	}
]

@app.route("/")
def listings_main():
    return render_template('home.html', listings=LISTINGS, company_name='itlistings')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)