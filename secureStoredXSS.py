from flask import Flask, request, redirect
from markupsafe import escape, Markup

app = Flask(__name__)

comments = []

@app.route('/', methods =['GET', 'POST'])
def home():

    if request.method == 'POST':
        newComment = request.form['comment']
        comments.append(escape(newComment))
        return redirect('/')

    commentSection = Markup("<br>".join(comments))  


    return f"""<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Comment Section</title>
                </head>
                <body>
                    <h1>Leave a Comment Below</h1>
                    <form action="/" method="POST">
                        <label>Comment: </label>
                        <input type="text" name="comment" placeholder="Enter your comment"> <br>
                        <input type="submit" value="Post">
                    </form>

                    <h2> Comment Section </h2>
                    {commentSection}

                </body>
                </html>"""

if __name__ == '__main__':
    app.run(debug=True)