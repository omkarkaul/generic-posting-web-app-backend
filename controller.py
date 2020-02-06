from flask import Flask, request, make_response, jsonify
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
def get_comments_for_post():
    args = dict(request.args)
    print(args)
    if 'post' in args:
        post = args['post']
        
        comments = db.get_comments_for_post(post)
        
        response = make_response(jsonify(comments), 200)
        response.headers['Content-Type'] = 'application/json'

        return response
    else:
        return make_response(("Missing 'post' param!", 400))

@app.route("/api/posts", methods = ['POST'])
def add_new_post():
    if request.is_json:
        body = request.get_json()

        post = body.get('post')

        if post is None:
            return make_response(('Bad request!', 400))

        result = db.add_new_post(post)
        
        if result == 1:
            return make_response((f"Successfully posted {post.upper()} to the database!", 200))
        elif result == 2:
            return make_response((f"{post.upper()} is a duplicate entry!", 409))

    return make_response(('Bad request!', 400))

@app.route("/api/comments", methods = ['POST'])
def add_new_comment():
    args = dict(request.args)

    if request.is_json and 'post' in args:
        body = request.get_json()
        
        comment = body.get('comment')
        post = args.get('post')
    
        if comment is None:
            return make_response(('Bad request!', 400))

        result = db.add_new_comment(post, comment)

        if result == 1:
            return make_response((f"Successfully added comment for post {post}!", 200))
        elif result == 2:
            return make_response((f"Post '{post}' doesn't exist!", 400))
    
    return make_response(("Bad data!", 400))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)