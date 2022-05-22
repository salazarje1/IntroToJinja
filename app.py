from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import stories


app = Flask(__name__)
app.config["SECRET_KEY"] = "chickensarecool"


debug = DebugToolbarExtension(app)


@app.route("/madlibs_form")
def madlibs_form():
    return render_template("form.html")

@app.route("/story")
def madlibs():
    place = request.args["place"]
    noun = request.args["noun"] 
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural_noun"]
    story = stories.story.generate({"place":place, "noun":noun, "verb":verb, "adjective":adjective, "plural_noun":plural_noun})
    return render_template("madlibs.html", story=story)