from flask import Flask, render_template, request
from WDS import WDSWrapper
import json

app = Flask(__name__)

# Initialise WDS wrapper
with open('wds_credentials.json') as creds:
    wds_credentials = json.load(creds)
    wds = WDSWrapper(wds_credentials)

@app.route('/', methods=['GET'])
@app.route('/search', methods=['GET'])
def index():
    return render_template('search.html')

@app.route('/results', methods=['POST'])
def get_results():

    # Validate the query string
    # length? special characters?
    query = request.form.get('natural_language_query')

    # Run query
    print('Query: ' + request.form.get('natural_language_query'))
    results = wds.query(natural_language_query=query, max_docs=10)

    # Format results
    # get doc title, passage(s), page numbers?
    # format into appropriate dictionary
    # display_results = {}
    # for result in results['results']:
        
        

    # Render template ... with fields: title + passage for documents, original search query should be in search box (different colour or something)
    
    return render_template('results.html', results=results['results'])

if __name__=='__main__':
    app.run(debug=True)