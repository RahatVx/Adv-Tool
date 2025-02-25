from flask import Flask, render_template
from config.settings import Config

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/stats')
def stats():
    return {
        "status": "active",
        "storage_used": "1.2GB",
        "active_processes": 3
    }
