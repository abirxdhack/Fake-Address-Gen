

# Fake Address Generator API

A simple and efficient Flask-based API for generating random fake addresses for various countries. This project is designed to provide developers with a tool to generate realistic address data for testing and development purposes.

## 🌐 API Overview

The Fake Address Generator API allows you to generate random fake addresses for supported countries by providing a country code. The API is currently hosted at [https://smartfake.vercel.app/](https://smartfake.vercel.app/) and is ready for use!

## 🚀 Features

- Generate random fake addresses for multiple countries.
- Easy-to-use RESTful API with a single endpoint.
- Supports a wide range of country codes (e.g., US, UK, BD, etc.).
- Includes a sleek, responsive front-end interface built with Tailwind CSS.
- Open-source and welcoming contributions!

## 📡 API Endpoint

**GET** `/api/address?code={country_code}`

- **Description**: Generates a random fake address for the specified country.
- **Query Parameter**:
  - `code`: The country code (e.g., `US`, `UK`, `BD`). Case-insensitive. Required.
- **Example Request**:
  ```bash
  curl -X GET "https://smartfake.vercel.app/api/address?code=US"
  ```
- **Example Success Response**:
  ```json
  {
    "country": "United States",
    "city": "New York",
    "street": "123 Main St",
    "zip": "10001",
    "state": "NY",
    "api_owner": "@ISmartCoder",
    "api_updates": "t.me/TheSmartDev"
  }
  ```
- **Example Error Response**:
  ```json
  {
    "error": "Country code not found",
    "api_owner": "@ISmartCoder",
    "api_updates": "t.me/TheSmartDev"
  }
  ```

## 🛠️ Installation

To run the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/abirxdhack/Fake-Address-Gen.git
   cd Fake-Address-Gen
   ```

2. **Install dependencies**:
   ```bash
   pip install flask
   ```

3. **Prepare the data**:
   - Ensure the `data/` folder contains JSON files for each country (e.g., `bd.json`, `us.json`).
   - Each JSON file should contain an array of address objects.

4. **Run the application**:
   ```bash
   python main.py
   ```

5. **Access the API**:
   - The API will be available at `http://localhost:5000/`.
   - Visit `http://localhost:5000/` to see the front-end interface.

## 📂 Data Structure

The API relies on JSON files stored in the `data/` folder. Each file is named after a country code (e.g., `bd.json`) and contains an array of address objects. Example structure for `us.json`:

```json
[
  {
    "country": "United States",
    "city": "New York",
    "street": "123 Main St",
    "zip": "10001",
    "state": "NY"
  },
  {
    "country": "United States",
    "city": "Los Angeles",
    "street": "456 Elm St",
    "zip": "90001",
    "state": "CA"
  }
]
```

## 🌍 Supported Countries

The API currently supports the following countries (add more by contributing!):

- **US** - United States
- **UK** - United Kingdom
- **BD** - Bangladesh
- **CA** - Canada
- **IN** - India
- ...and many more! Check the front-end interface or the `data/` folder for the full list.

## 🤝 Contributing

We welcome contributions to make this project even better! Here's how you can help:

- **Add more addresses**: Contribute new JSON files to the `data/` folder for additional countries or expand existing ones. Follow the naming convention (e.g., `country_code.json`).
- **Improve the code**: Submit pull requests with enhancements to the API or front-end.
- **Report issues**: Open an issue on the [GitHub repository](https://github.com/abirxdhack/Fake-Address-Gen) if you find bugs or have feature requests.

To contribute:

1. Fork the repository: [https://github.com/abirxdhack/Fake-Address-Gen](https://github.com/abirxdhack/Fake-Address-Gen)
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Make your changes and commit:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to your fork and submit a pull request.

**Forks are welcome!** Help us expand the database and improve the API.

## 📢 Updates & Support

- **Updates Channel**: Stay updated with the latest news and improvements at [t.me/TheSmartDev](https://t.me/TheSmartDev).
- **Contact**: Reach out to the project owner, [@ISmartCoder](https://t.me/ISmartCoder), for custom APIs, bots, or support.

## 🙏 Acknowledgments

A huge thanks to **Mahir Labib** for providing the initial database! Your contribution is greatly appreciated.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Want custom APIs or bots?**  
We offer solutions in Python, PHP, and Node.js. DM [@ISmartCoder](https://t.me/ISmartCoder) to buy or discuss custom development!

