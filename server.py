from flask import Flask, request, Response, render_template, jsonify
import requests
import time
import random
import json



app = Flask(__name__, static_url_path='/static')




@app.route("/gpt2", methods=["POST"])
def gpt2():

    url='https://train-fgixn9wtlmw9ywgxc1mt-gpt2-train-teachable-ainize.endpoint.ainize.ai/predictions/gpt-2-ko-small-finetune'

    #https://train-fgixn9wtlmw9ywgxc1mt-gpt2-train-teachable-ainize.endpoint.ainize.ai/predictions/gpt-2-ko-small-finetune

    #https://train-fynx0a29peulf0eemtel-gpt2-train-teachable-ainize.endpoint.ainize.ai/predictions/gpt-2-ko-small-finetune

    context = request.form['context']
    length = request.form['length']

    if length == "short":
        length = random.randrange(50,100)
    else:
        length = 200

    data=json.dumps({
            'text': context,
            'num_samples': 5,
            'length': length
        })

    response = requests.post(url, headers={'Content-Type': 'application/json'}, data=data)

    if response.status_code == 200:
        res = response.json() 
        
        #콘솔에 결과 출력확인
        print(res)

        #json파일을 파이썬 딕셔너리로 변경후 출력
        return json.dumps(res)

    else:
        print("Failed requests")


@app.route("/")
def main():
    return render_template("home.html")

@app.route("/pricing.html", methods=["GET"])
def pricing():
    return render_template("pricing.html")

@app.route("/home.html", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/index.html", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/form.html", methods=["GET"])
def form():
    return render_template("form.html")

@app.route("/signin.html", methods=["GET"])
def signin():
    return render_template("signin.html")

@app.route("/signup.html", methods=["GET"])
def signup():
    return render_template("signup.html")

# Health Check
@app.route("/healthz", methods=["GET"])
def healthCheck():
    return "", 200


#if __name__ == "__main__":
#    from waitress import serve
#    serve(app, host='0.0.0.0', port=80)   

app.run(port = 5001)