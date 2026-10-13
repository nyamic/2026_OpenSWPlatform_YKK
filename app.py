from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/list')
def view_list():
    return render_template('list.html')

@app.route('/review')
def view_review():
    return render_template('review.html')

@app.route('/register-items')
def register_items():
    return render_template('reg_items.html')

@app.route('/register-reviews')
def register_reviews():
    return render_template('reg_reviews.html')

@app.route("/submit_item")
def reg_item_submit():
    name=request.args.get("name")
    status=request.args.get("status")
    return "Input name:" + name + " input status:" + status

@app.route("/submit_item_post", methods=["POST"])
def reg_item_submit_post():
        image_file=request.files["picture"]
        image_file.save("static/images/{}".format(image_file.filename))
        data=request.form
        return render_template("result.html", data=data,
                               img_path="static/images/{}".format(image_file.filename))

if __name__ == '__main__':
    app.run(debug=True)