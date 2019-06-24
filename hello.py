from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def boxes():
    return render_template("index.html")


@app.route("/<times>")
def moreboxes(times):
    return render_template("morecheckers.html", num_times=int(times))
  


if __name__=="__main__":
    app.run(debug=True)