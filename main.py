from flask import Flask, render_template

app = Flask(__name__) #passing in name helps Flsak determine root path

#each page is connected to a python function (routing)

# @ means decorator - modify python function, used to route/map url to return value in Flask
@app.route('/')
def index():
    return render_template("report.html")

@app.route('/profile/<playername>')
def profile(playername):
    return render_template("profile.html", playername=playername)

@app.route('/about')
def about():
    return render_template("about.html")

#request.method is the method that is used for that route

if __name__ == "__main__":
    app.run(debug=True)