from flask import Flask, render_template, request, redirect

from google.appengine.ext import ndb

app = Flask(__name__)


class PotentialClient(ndb.Model):
	email = ndb.StringProperty()


@app.route('/notify', methods=['POST'])
def notify():
	email = request.form['name']
	print email
	# potential_client = PotentialClient(email)
	# potential_client.put()


	return redirect('/')



@app.route("/")
def home():
	return render_template("thebabyhub.html")

if __name__ == '__main__':
	app.run(debug=True)		