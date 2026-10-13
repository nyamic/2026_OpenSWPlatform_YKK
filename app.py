from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run(debug=True)