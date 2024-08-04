from app import app
from flask import render_template

@app.route('/')



def main():
    return render_template('principal.html')


if __name__ == '__main__':
    app.run (debug=True)