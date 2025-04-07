from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

feedback_data = []

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if not name or not email or not message:
            flash('Please fill out all fields!', 'error')
            return redirect(url_for('feedback'))

        feedback_data.append({
            'name': name,
            'email': email,
            'message': message
        })

        flash('Thank you for your feedback!', 'success')
        return redirect(url_for('feedback_list'))

    return render_template('feedback.html')


@app.route('/feedback/list')
def feedback_list():
    return render_template('feedback_list.html', feedback=feedback_data)

if __name__ == '__main__':
    app.run()