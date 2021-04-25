from flask import Flask, request, render_template
from youtube import search
from description_search import create_whoosh_index, query_on_whoosh
import json

import os

print("The variable __name__: ")
print(__name__)

# __name__ is a special variable in python
# it can either be "__main__" or the name of the script
app = Flask(__name__)

# the request handler

# listens to 
# example: google.com/
# example: google.com/search
@app.route("/")
def index(): # method name doesn't matter to Flask
    heading = "Youtube Description Search"
    
    return render_template("index.html", user=heading)

@app.route("/query", methods=['GET', 'POST'])
def query():
    arg = request.args.get('q')
    if not arg or not arg.strip():
        return render_template("query.html")

    index_name = "whoosh_index_" + arg
	
    if request.method == 'GET':

        filename = "youtube_search_" + arg + ".json"
        if os.path.exists(filename):
            # Pull data from an existing JSON file
            f = open(filename)
            results = json.load(f)
        else:
            results = search(arg, 1, False)
            create_whoosh_index(results, index_name)

        return render_template("query.html", query_term=arg, data=results)


    if request.method == 'POST':
        # the result sent by the search box on the query page
        search_term = request.form['description_search']

        print(search_term)
        results = query_on_whoosh(index_name, search_term)
        return render_template("query.html", query_term=arg, search_term=search_term, data=results, description_search=True)

@app.route("/music_query", methods=['GET'])
def music_query():
    arg = request.args.get('q')
    if not arg or not arg.strip():
        render_template("music_query.html")

    index_name = "whoosh_index_"+ arg +".json"

    if request.method == 'GET':
        
        filename = "youtube_music_search_"+ arg +".json"
        if os.path.exists(filename):
            f = open(filename)
            results = json.load(f)
        else:
            results = search(arg, 1, True)
            create_whoosh_index(results, index_name)

        return render_template("music_query.html", query_term=arg, data=results)
         

