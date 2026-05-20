from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        post_input = request.form.get("post_input", "10")
        split_input = post_input.split(",")
        coorx = split_input[0] if len(split_input) > 0 else "55.6761"
        coory = split_input[1] if len(split_input) > 1 else "11.69581"
    else:
        # Default value for GET request
        coorx = "55.6761"
        coory = "11.69581"
    return render_template('index.html', title='Smadre kasse', coorx=coorx, coory=coory)

@app.route('/about')
def about():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
