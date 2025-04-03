from flask import Flask, request, redirect, url_for, render_template_string
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit upload size to 16MB

# Create the upload folder if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# HTML template with an upload form and image preview
HTML = """
<!doctype html>
<html>
  <head>
    <title>Image Upload and Preview</title>
  </head>
  <body>
    <h1>Upload an Image</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file" accept="image/*">
      <input type="submit" value="Upload">
    </form>
    {% if filename %}
      <h2>Image Preview:</h2>
      <img src="{{ url_for('uploaded_file', filename=filename) }}" style="max-width:300px; border:1px solid #ccc;">
    {% endif %}
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def upload_file():
    filename = None
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template_string(HTML, filename=filename)

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return app.send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)
