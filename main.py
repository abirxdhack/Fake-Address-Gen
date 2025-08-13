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
    country_input = request.args.get('country', request.args.get('code', '')).strip().upper()
    if not country_input:
        return jsonify({
            "error": "Country code or name parameter is required",
            "api_owner": "@ISmartCoder",
            "api_updates": "t.me/TheSmartDev"
        }), 400

    country_mappings = {
        "UK": ("GB", "United Kingdom"),
        "UAE": ("AE", "United Arab Emirates"),
        "AE": ("AE", "United Arab Emirates"),
        "UNITED KINGDOM": ("GB", "United Kingdom"),
        "UNITED ARAB EMIRATES": ("AE", "United Arab Emirates")
    }

    if country_input in country_mappings:
        country_code, country_name = country_mappings[country_input]
    else:
        if len(country_input) == 2:
            country_code, country_name = country_input, country_input
            country = pycountry.countries.get(alpha_2=country_input)
            if country:
                country_name = country.name
        else:
            try:
                country = pycountry.countries.search_fuzzy(country_input)[0]
                country_code, country_name = country.alpha_2, country.name
            except LookupError:
                country_code, country_name = country_input, country_input

    file_country_code = 'uk' if country_code == 'GB' else country_code.lower()
    file_path = os.path.join('data', f"{file_country_code}.json")
    app.logger.info(f"Attempting to load file: {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
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
        try:
            flag_emoji = chr(0x1F1E6 + ord(country_code[0]) - ord('A')) + chr(0x1F1E6 + ord(country_code[1]) - ord('A'))
        except:
            flag_emoji = "🏚"
        random_address["country"] = country_name
        random_address["country_flag"] = random_address.get("country_flag", flag_emoji)
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

        country_mappings = {
            "UK": "United Kingdom",
            "UAE": "United Arab Emirates",
            "AE": "United Arab Emirates"
        }

        for filename in os.listdir(data_dir):
            if filename.endswith('.json'):
                country_code = filename.split('.')[0].upper()
                display_country_code = 'GB' if country_code == 'UK' else country_code
                country_name = country_mappings.get(display_country_code, display_country_code)
                country = pycountry.countries.get(alpha_2=display_country_code)
                if country:
                    country_name = country.name
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
