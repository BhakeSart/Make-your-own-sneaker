from flask import Flask, render_template, request
import requests
import os
import openai

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        color = request.form.get('color')
        brand = request.form.get('brand')
        Type = request.form.get('type')
        insp = request.form.get('insp')
        toe = request.form.get('toe')
        upper = request.form.get('upper')
        heel = request.form.get("heel")
        sole = request.form.get("sole")
        api_route = "https://api.openai.com/v1/images/generations"

        openai.api_key = "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"
        text = (
            f"A high resolution lateral 4K Ultra HD realistic image of {color} coloured {brand} {Type} shoe sneaker similar to {insp} with {upper} coloured upper, {sole} coloured sole, {heel} couloured body, {toe} coloured toebox placed in a monochromatic white background:: hyper detailed, ultrarealistic, high resolution, full side view, product design, product presentation")
        data = openai.Image.create(
            prompt=text,
            n=1,
            size="512x512"
        )
        result = data["data"][0]["url"]

        # data = {
        #     "prompt": text,
        #     "n": 1,
        #     "size": "1024x1024"

        # }
        # response = requests.post(api_route, json=data)

        # api_response = data.json()

        return render_template('sample.html', response=result)

    return render_template('sample.html', response=None)
    # return data
    # return data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
