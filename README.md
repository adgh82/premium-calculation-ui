# Premium Predictor UI
## About the app
The application is the frontend for accessing the hosted api that leverages a trained machine learning model to predict the premium price of an individual

## Inputs
The following details are gathered by the UI to successfully call the API and get the price:

1. Age: Minimum value 18, should be an integer
2. Height(in cms): Minimum value 130, should be an integer
3. Weight(in Kgs): Minimum value 50, should be an integer
4. Diabetic: Toggle type, defaulted to No
5. BP Issues: Toggle type, defaulted to No
6. Has Transplants: Toggle type, defaulted to No
7. Has Chronic illness: Toggle type, defaulted to No
8. Has Allergies: Toggle type, defaulted to No
9. Has family cancer history: Toggle type, defaulted to No
10. Has Major surgeries: Select dropdown, defaulted to 0

## Output:
Premium price received from the API

## References
Link to the [FLASK API](https://github.com/adgh82/insurance-premium-predictor-api/blob/main/README.md)

Link to the [Model Training Notebook](https://github.com/adgh82/insurance-cost-predictor-linear-reg/blob/main/insurance_eda.ipynb)

Link to [Medium Article] (https://medium.com/@adgh130582/eda-and-premium-price-prediction-from-insurance-dataset-7c3f30c77e04)
