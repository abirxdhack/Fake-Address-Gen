#Copyright @ISmartCoder
#Updates Channel https://t.me/TheSmartDev
from flask import Flask, jsonify, request, render_template
import json
import random
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def status():
    return render_template('status.html')

@app.route('/api/address', methods=['GET'])
def get_address():
    country_code = request.args.get('code', '').upper()
    if not country_code:
        return jsonify({
            "error": "Sorry Bro Invalid Country Code Provided",
            "api_owner": "@ISmartCoder",
            "api_updates": "t.me/TheSmartDev"
        }), 400
    
    file_path = os.path.join('data', f"{country_code.lower()}.json")
    try:
        with open(file_path, 'r') as file:
            addresses = json.load(file)
        
        if not addresses:
            return jsonify({
                "error": "No addresses found for this country code",
                "api_owner": "@ISmartCoder",
                "api_updates": "t.me/TheSmartDev"
            }), 404
        
        random_address = random.choice(addresses)
        random_address["api_owner"] = "@ISmartCoder"
        random_address["api_updates"] = "t.me/TheSmartDev"
        return jsonify(random_address)
    
    except FileNotFoundError:
        return jsonify({
            "error": "Country code not found",
            "api_owner": "@ISmartCoder",
            "api_updates": "t.me/TheSmartDev"
        }), 404
    except Exception as e:
        return jsonify({
            "error": str(e),
            "api_owner": "@ISmartCoder",
            "api_updates": "t.me/TheSmartDev"
        }), 500

@app.errorhandler(404)
def page_not_found(e):
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Error</title>
        <style>
            body {
                background-color: #ffffff;
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                color: #333;
            }
            .error-message {
                text-align: center;
                font-size: 24px;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="error-message">Error: Wrong Endpoint</div>
    </body>
    </html>
    ''', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
