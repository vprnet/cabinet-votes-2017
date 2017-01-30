from main import app
from flask import render_template, request
from query import get_votes
from config import FREEZER_BASE_URL

votes = get_votes()

@app.route('/')
def index():
    page_title = 'Cabinet Votes 2017'
    page_url = FREEZER_BASE_URL.rstrip('/') + request.path

    return render_template('content.html',
        page_title=page_title,
        page_url=page_url,
        votes=votes)
