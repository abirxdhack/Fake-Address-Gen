from flask import Flask, jsonify, request, render_template
import json
import random
import os
import pycountry
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/', methods=['GET'])
def status():
    return render_template('status.html')

@app.route('/api/address', methods=['GET'])
def get_address():
    country_input = request.args.get('country', request.args.get('code', '')).strip().lower()
    if not country_input:
        return jsonify({
            "error": "Country code or name parameter is required",
            "api_owner": "@ISmartCoder",
            "api_updates": "t.me/TheSmartDev"
        }), 400

    country_code = None
    if country_input in ["uk", "united kingdom"]:
        country_code = "gb"
    elif country_input in ["uae", "united arab emirates"]:
        country_code = "ae"
    else:
        if len(country_input) == 2:
            country_code = country_input.upper()
            country = pycountry.countries.get(alpha_2=country_code)
            if not country:
                return jsonify({
                    "error": "Invalid country code provided",
                    "api_owner": "@ISmartCoder",
                    "api_updates": "t.me/TheSmartDev"
                }), 404
        else:
            try:
                country = pycountry.countries.search_fuzzy(country_input)[0]
                country_code = country.alpha_2
            except LookupError:
                return jsonify({
                    "error": "Invalid country name or code provided",
                    "api_owner": "@ISmartCoder",
                    "api_updates": "t.me/TheSmartDev"
                }), 404

    file_country_code = 'uk' if country_code == 'GB' else country_code.lower()
    display_country_code = 'GB' if country_code == 'UK' else country_code

    file_path = os.path.join('data', f"{file_country_code}.json")
    app.logger.info(f"Attempting to load file: {file_path}")

    try:
        with open(file_path, 'r') as file:
            addresses = json.load(file)

        if not isinstance(addresses, list):
            addresses = [addresses]

        if not addresses:
            return jsonify({
                "error": "Sorry No Address Available For This Country",
                "api_owner": "@ISmartCoder",
                "api_updates": "t.me/TheSmartDev"
            }), 404

        random_address = random.choice(addresses)
        random_address["api_owner"] = "@ISmartCoder"
        random_address["api_updates"] = "t.me/TheSmartDev"

        country = pycountry.countries.get(alpha_2=display_country_code)
        country_flag = country.flag if country and hasattr(country, 'flag') else "Unknown"
        random_address["country_flag"] = country_flag

        return jsonify(random_address)

    except FileNotFoundError:
        app.logger.error(f"File not found: {file_path}")
        return jsonify({
            "error": "Sorry Bro Invalid Country Code Provided",
            "api_owner": "@ISmartCoder",
            "api_updates": "t.me/TheSmartDev"
        }), 404
    except Exception as e:
        app.logger.error(f"Error: {str(e)}")
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
            app.logger.error("Data directory not found")
            return jsonify({
                "error": "Data directory not found",
                "api_owner": "@ISmartCoder",
                "api_updates": "t.me/TheSmartDev"
            }), 404

        for filename in os.listdir(data_dir):
            if filename.endswith('.json'):
                country_code = filename.split('.')[0].upper()
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
        app.logger.error(f"Error: {str(e)}")
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
