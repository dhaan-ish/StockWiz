# StockWiz

## Overview

StockWiz is a web-based application designed to provide stock price predictions based on historical data, including high, open, low, and volume information. It utilizes machine learning models hosted on Hugging Face to make accurate predictions for stock market enthusiasts.

## Technologies Used

- **Frontend:**
  - HTML
  - CSS
  - JavaScript

- **Backend:**
  - Python
  - Flask
  - GradioClient

## Getting Started

```bash
git clone https://github.com/dhaan-ish/StockWiz.git
cd StockWiz
python -m venv venv  # Optional but recommended
# Activate the virtual environment based on your OS
pip install -r requirements.txt
python app.py
```

Access the app in your web browser at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## How it Works

StockWiz leverages machine learning models hosted on Hugging Face to predict closing stock prices. The GradioClient library is used to seamlessly integrate these models into the web application, providing users with an easy-to-use interface for making predictions.

## Usage

1. Access the StockWiz web app at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

2. Enter the relevant data, including high, open, low, and volume, for the stock you want to predict.

3. Click the "Predict" button to obtain the predicted closing price.

4. Review the prediction and use it for your investment decisions.

## Contributing

If you'd like to contribute to StockWiz, please fork the repository and submit a pull request. We welcome contributions that enhance the application's functionality or fix issues.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The machine learning models used in this project are hosted on [Hugging Face](https://huggingface.co/).
- GradioClient library: [Gradio](https://www.gradio.app/)

Feel free to contact us for any questions or issues.

