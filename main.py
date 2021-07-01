from flask import Flask, request, render_template, make_response

app = Flask(__name__)


@app.route('/')
def index():
    response = make_response(render_template('index.html'))
    response.headers['Refresh'] = '86400; url=http://127.0.0.1:5000/o1SfuSXpptIk1p8U0qISobkrYwXSILflr6ZxTsmF?p=banana'
    return response


@app.route('/o1SfuSXpptIk1p8U0qISobkrYwXSILflr6ZxTsmF')
def flag():
    p = request.args.get('p', type=str)
    if p == 'banana':
        return 'flag{l00k_at_Th3_he4d3rs!}'
    else:
        return 'Ah ah ah, you didn\'t say the magic word'


if __name__ == '__main__':
    app.run()
