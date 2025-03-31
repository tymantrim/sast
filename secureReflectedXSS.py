from flask import Flask, request
from markupsafe import escape
app = Flask(__name__)


@app.route('/', methods =['GET'])
def search():
    query = escape(request.args.get('q'))

    return f"""
            <html>
            <head><title>Search Engine</title></head>
            <body>
                <h1>Search Results</h1>
                <p>Results for: {query}</p>
                <form action="/" method="get">
                    <input type="text" name="q">
                    <input type="submit" value="Search">
                </form>
            </body>
            </html>
            """

if __name__ == '__main__':
    app.run(debug=True)