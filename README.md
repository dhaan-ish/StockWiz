# StockWiz

## Overview

StockWiz is a web-based application designed to predict the closing stock prices using machine learning models. It provides predictions based on historical data including high, open, low, and volume information.

## Technologies Used

- Frontend:
  - HTML
  - CSS
  - JavaScript

- Backend:
  - Python

## Getting Started

To run StockWiz on your local machine, follow these steps:

1. Clone the repository:

`git clone https://github.com/dhaan-ish/StockWiz.git`

2. Navigate to the project folder:

`cd StockWiz`

3. Activate the virtual environment:

```myenv\Scripts\activate```

4. Run the Python application:

`python app.py`

5. Access the app in your web browser at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## How it Works.

StockWiz uses machine learning models hosted on Hugging Face to predict the closing stock prices. The GradioClient library is used to integrate these models into the web application, allowing users to make predictions easily.

## Usage

1. Access the StockWiz web app at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

2. Enter the relevant data (high, open, low, volume) for a stock you want to predict.

3. Click the "Predict" button to get the predicted closing price.

4. Review the prediction and use it as needed for your investment decisions.

## Contributing

If you'd like to contribute to StockWiz, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The machine learning models used in this project are hosted on [Hugging Face](https://huggingface.co/).
- GradioClient library: [Gradio](https://www.gradio.app/)

Feel free to contact us for any questions or issues.

