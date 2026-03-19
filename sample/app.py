from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/add', methods=['GET', 'POST'])
def add_feedback():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')

        return "Feedback submitted"

    return render_template('add_feedback.html')
if __name__=='__main__':
    app.run(debug=True)