
# House Price Predictor 🏠

A web-based application to predict residential house prices using **Linear Regression** and **Polynomial Regression** models. Users can input key features like area, number of bedrooms, age, and location to estimate the house price.

---

## Features

- Predict house prices based on multiple factors:
  - Area (in sq. ft)
  - Number of Bedrooms
  - Age of the Property
  - Location (City Center, Suburb, Village)
- Compares Linear and Polynomial Regression models.
- Interactive and attractive **web interface** built with Flask.
- Responsive design with modern UI and background visuals.

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/AbijithSebastian/HousePricePredictor.git
cd HousePricePrediction
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Flask app:

```bash
cd webapp
python app.py
```

5. Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## Project Structure

```
HousePricePrediction/
├─ backend/
│  ├─ model.pkl
│  ├─ preprocessor.pkl
│  └─ poly.pkl
├─ webapp/
│  ├─ templates/
│  │  └─ index.html
│  ├─ static/
│  │  ├─ style.css
│  │  └─ house_icon.png
│  └─ app.py
├─ .gitignore
├─ README.md
└─ requirements.txt
```

---

## Technologies Used

- Python 3
- Flask
- Pandas
- Scikit-learn
- HTML, CSS (Glassmorphism + Modern UI)
- Git & GitHub

---

## How It Works

1. Users input house details via the web form.
2. The backend preprocesses inputs using the saved `preprocessor.pkl`.
3. Data is transformed with polynomial features (if Polynomial Regression is selected).
4. Predictions are made using the saved `model.pkl`.
5. The estimated price is displayed on the same page.

---

## Notes

- Ensure your virtual environment is activated before running the app.
- Dependencies are listed in `requirements.txt`.
- The dropdown location text is black for readability on a dark-themed UI.
