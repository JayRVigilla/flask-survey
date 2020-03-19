from flask import Flask, render_template, request, jsonify, redirect
from flask_debuggertoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "password"

debug = DebugToolbarExtension(app)
