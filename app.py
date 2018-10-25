from flask import *
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")


@app.route('/shop')
def shop_page():
	candys = ["chocolate" , "lolipops" , "snacks"]
	return render_template("shop.html",candys = candys)

if __name__ == '__main__':
	app.run(debug = True)


