from flask import Flask, jsonify, request, render_template
import json
import random
import os
import pycountry

app = Flask(__name__)

@app.route('/', methods=['GET'])
def status():
    return render_template('status.html')

@app.route('/api/address', methods=['GET'])
def get_address():
    country_code = request.args.get('code', '').upper()
    if not country_code:
        return jsonify({
            "error": "Country code parameter is required",
            "api_owner": "@ISmartCoder",
            "api_updates": "t.me/TheSmartDev"
        }), 400
    
    # Handle UK/GB equivalence
    file_country_code = 'uk' if country_code == 'UK' else country_code.lower()
    display_country_code = 'GB' if country_code == 'UK' else country_code
    
    file_path = os.path.join('data', f"{file_country_code}.json")
    try:
        with open(file_path, 'r') as file:
            addresses = json.load(file)
        
        if not addresses:
            return jsonify({
                "error": "Sorry No Address Available For This Country",
                "api_owner": "@ISmartCoder",
                "api_updates": "t.me/TheSmartDev"
            }), 404
        
        random_address = random.choice(addresses)
        random_address["api_owner"] = "@ISmartCoder"
        random_address["api_updates"] = "t.me/TheSmartDev"
        
        # Get country flag using pycountry
        country = pycountry.countries.get(alpha_2=display_country_code)
        country_flag = country.flag if country and hasattr(country, 'flag') else "Unknown"
        random_address["country_flag"] = country_flag
        
        return jsonify(random_address)
    
    except FileNotFoundError:
        return jsonify({
            "error": "Sorry Bro Invalid Country Code Provided",
            "api_owner": "@ISmartCoder",
            "api_updates": "t.me/TheSmartDev"
        }), 404
    except Exception as e:
        return jsonify({
            "error": str(e),
            "api_owner": "@ISmartCoder",
            "api_updates": "t.me/TheSmartDev"
        }), 500

@app.route('/api/countries', methods=['GET'])
def get_countries():
    try:
        data_dir = 'data'
        countries = []
        
        if not os.path.exists(data_dir):
            return jsonify({
                "error": "Data directory not found",
                "api_owner": "@ISmartCoder",
                "api_updates": "t.me/TheSmartDev"
            }), 404

        for filename in os.listdir(data_dir):
            if filename.endswith('.json'):
                country_code = filename.split('.')[0].upper()
                # Handle UK/GB case for display
                display_country_code = 'GB' if country_code == 'UK' else country_code
                country = pycountry.countries.get(alpha_2=display_country_code)
                country_name = country.name if country else "Unknown"
                
                countries.append({
                    "country_code": display_country_code,
                    "country_name": country_name
                })
        
        if not countries:
            return jsonify({
                "error": "No countries found",
                "api_owner": "@ISmartCoder",
                "api_updates": "t.me/TheSmartDev"
            }), 404

        return jsonify({
            "countries": sorted(countries, key=lambda x: x["country_name"]),
            "total_countries": len(countries),
            "api_owner": "@ISmartCoder",
            "api_updates": "t.me/TheSmartDev"
        })

    except Exception as e:
        return jsonify({
            "error": str(e),
            "api_owner": "@ISmartCoder",
            "api_updates": "t.me/TheSmartDev"
        }), 500

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
        "error": "Sorry This Is Wrong Endpoint",
        "api_owner": "@ISmartCoder",
        "api_updates": "t.me/TheSmartDev"
    }), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
