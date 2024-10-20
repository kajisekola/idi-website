from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/<string:page_name>')
def about(page_name):
    return render_template(page_name)
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
# @app.route('/service.html')
# def services():
#     return render_template('service.html')
# @app.route('/testimonial.html')
# def testimonial():
#     return render_template('testimonial.html')
# @app.route('/news.html')
# def news():
#     return render_template('news.html')
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

