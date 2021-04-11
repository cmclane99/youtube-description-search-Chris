from flask import Flask, request, render_template
from youtube import search
from description_search import create_whoosh_index, query_on_whoosh

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
    username = request.args.get('user')
    if not username or not username.strip():
        username = "World"

    return render_template("index.html", user=username)

@app.route("/query", methods=['GET', 'POST'])
def query():
    arg = request.args.get('q')
    if not arg or not arg.strip():
        return render_template("query.html")

    index_name = "whoosh_index_" + arg
	
    if request.method == 'GET':
        results = search(arg, 1)
        create_whoosh_index(results, index_name)
        return render_template("query.html", query_term=arg, data=results)

    if request.method == 'POST':
        # the result sent by the search box on the query page
        search_term = request.form['description_search']
        print(search_term)
        results = query_on_whoosh(index_name, search_term)
        return render_template("query.html", query_term=arg, data=results)
