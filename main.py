import os
import logging
from flask import Flask, redirect

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.DEBUG,
)

app = Flask(__name__)
REDIRECT_BASE_URL = os.environ.get("TUMBLR_REDIRECT_BASE_URL")
REDIRECT_CODE = int(os.environ.get("TUMBLR_REDIRECT_CODE", 302))

def get_redirect_target(path):
    return "%s%s" % (REDIRECT_BASE_URL, path)

@app.route('/post/<int:post_id>/<post_slug>')
def post_redirect(post_id, post_slug):
    target = get_redirect_target(post_slug)
    app.logger.info("Redirecting Tumblr Blog Post to %s", target)
    return redirect(target, code=REDIRECT_CODE)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    app.logger.info("Catch-all redirect for path %s", path)
    return redirect(get_redirect_target(''), code=REDIRECT_CODE)

if REDIRECT_BASE_URL is None:
    raise RuntimeError("No TUMBLR_REDIRECT_BASE_URL environment variable set")

if __name__ == '__main__':
    app.run()
