from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('search.html')

@app.route('/results', methods=['POST'])
def get_results():

    # Validate the query string
    # length? special characters?
    natural_language_query = request.form.get('natural_language_query')

    # Run query

    # Format results
    # get doc title, passage(s), page numbers?
    # format into appropriate dictionary

    # Render template ... with fields: title + passage for documents, original search query should be in search box (different colour or something)
    print(request.form.get('natural_language_query'))
    return render_template('results.html')

if __name__=='__main__':
    app.run(debug=True)