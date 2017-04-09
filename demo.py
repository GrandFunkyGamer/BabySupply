from flask import Flask, render_template, request, redirect

from google.appengine.ext import ndb

app = Flask(__name__)


@app.route("/")
def home():
	return render_template("thebabyhub.html")


class PotentialClient(ndb.Model):
	email = ndb.StringProperty()


@app.route('/notify', methods=['POST'])
def notify():
	email = request.form.get('email')
	print email
	potential_client = PotentialClient(email=email)
	#or
	#potential_client.email = email
	potential_client.put()


	return redirect('/thankyou')

@app.route('/thankyou', methods=['GET'])
def thankyou():
    return render_template("thebabyhub2.html")








if __name__ == '__main__':
	app.run(debug=True)		