from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key' # Needed for sessions to store secret_number

@app.route('/')
def index():
    # Initialize the game or reset it
    session['secret_number'] = random.randint(1, 100)
    session['attempts'] = 0
    return render_template('index.html', message="I'm thinking of a number between 1 and 100.")

@app.route('/guess', methods=['POST'])
def guess():
    user_guess = int(request.form['guess'])
    secret_number = session.get('secret_number')
    attempts = session.get('attempts', 0)
    attempts += 1
    session['attempts'] = attempts

    message = ""
    if user_guess < secret_number:
        message = "Too low!"
    elif user_guess > secret_number:
        message = "Too high!"
    else:
        message = f"Congratulations! You guessed the number {secret_number} in {attempts} attempts."
        #  button

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True) 
