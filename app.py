from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get('expression', '')
    try:
        # Safe eval (minimal context)
        result = eval(expression, {"__builtins__": {}}, {})
    except ZeroDivisionError:
        result = 'Error: Division by zero'
    except:
        result = 'Invalid expression'
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)

