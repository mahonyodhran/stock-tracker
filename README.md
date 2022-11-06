# Stock Tracker

## Description
Application to calculate the users current portfolio value and profit/loss on personal stock portfolio.

## Run Locally

Clone the project

```bash
  git clone https://github.com/mahonyodhran/stock-tracker.git
```

Create a virtual environment in the root directory

```bash
  python -m venv venv
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run app

```bash
  python app/app.py
```

---

` Note: The app gets it data from the load_json_data() method within 'methods.py'. The method gets the data from a file called 'shares.json' so I have included a sample JSON file called 'example_shares.json' so feel free to rename this to 'shares.json' and the app will run. You can then enter in your own data following the template where the ticker ('AMZN', 'META') is the keyS.`

---


## Roadmap

#### Release 1 - Basic Functionality

- Create basic application layout

- Get overall portfolio value

- Get value per ticker

- Get profit/loss per ticker

- Get overll profit/loss

#### Release 2 - Basic UI

- TBC