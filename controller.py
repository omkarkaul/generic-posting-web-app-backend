from flask import Flask, request, make_response, Response, jsonify
from database import Database

app = Flask(__name__)
db = Database()


@app.route("/api/posts", methods = ['GET'])
def get_all_posts():
    posts = db.get_all_posts()

    response = make_response(jsonify(posts), 200)
    response.headers['Content-Type'] = 'application/json'

    return response

@app.route("/api/comments", methods = ['GET'])
def get_comments_for_post(post):
    args = dict(request.args)

    if 'post' in args:
        post = args['post']
        print(post)
        
        comments = db.get_comments_for_post(post)

        response = make_response(jsonify(comments), 200)
        response.headers['Content-Type'] = 'application/json'

        return response
    else:
        return make_response(("Missing 'post' param!", 400))

# @app.route("/api/posts", methods = ['POST'])
# def add_post():
#     args = dict(request.args)

#     if 'name' in args:
#         name = args['name']
        
#         return app.make_response((f"Successfully added {name} into the DB!"), 200)
#     else:
#         return app.make_response(("Missing 'name' param!", 400))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)