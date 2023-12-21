
# Rent_Prediction

DEMO APP LINK https://rent-prediction.streamlit.app/
Rent_Prediction_model using Streamlit Deployment Using Machine Learning Algorithms

# Project Goals
The goal of this project is to analyze the house rental dataset and build a predictive model that can estimate the rent of a house based on its features. The project involves performing exploratory data analysis (EDA) to gain insights, preprocessing the data, selecting a suitable machine learning algorithm, tuning the model hyperparameters, and finally deploying the model using Streamlit.

# Benefits from Project
Market Insights:
Predicting house rent allows individuals, real estate agents, and property managers to gain insights into market trends. Understanding rent fluctuations helps stakeholders make informed decisions about pricing strategies.

Tenant Decision-Making:
Prospective tenants can benefit by having insights into expected rent prices. This information assists them in making informed decisions about where to live and whether a particular property is within their budget.

# About Dataset
This dataset contains information about house rentals in India. The dataset includes various parameters such as the number of bedrooms, rent, size, floor details, area type, area locality, city, furnishing status, preferred tenant type, number of bathrooms, and point of contact. 

 Data Summary:
1) BHK: Number of Bedrooms, Hall, Kitchen.
2) Rent: Rent of the Houses/Apartments/Flats.
3) Size: Size of the Houses/Apartments/Flats in Square Feet.
4) Floor: Houses/Apartments/Flats situated on which floor and total number of floors (Example: Ground out of 2, 3 out of 5, etc.)
5) Area Type: Size of the Houses/Apartments/Flats calculated on either Super Area or Carpet Area or Build Area.
6) Area Locality: Locality of the Houses/Apartments/Flats.
7) City: City where the Houses/Apartments/Flats are located.
8) Furnishing Status: Furnishing Status of the Houses/Apartments/Flats, either it is Furnished or Semi-Furnished or Unfurnished.
9) Tenant Preferred: Type of Tenant Preferred by the Owner or Agent.
10) Bathroom: Number of Bathrooms.
11) Point of Contact: Whom should you contact for more information regarding the Houses/Apartments/Flats.

# Learning for Rent Prediction Model:

1) Exploratory & Statistics Analysis
   
   Perform data exploration to gain insights into the distribution, relationships, and summary statistics of the rental 
   dataset.
   Visualize various features and their impact on rental prices, such as the number of bedrooms, location, furnishing 
   status, and more.
   Identify any outliers, missing values, or data inconsistencies that need to be addressed.
   
2) Feature Engineering & Data Preprocessing:
   
   Create new meaning features to balance or optimize analysis
   Preprocess data and removed outliers to reduce bias or extreme values
   
3) Model Building & Model Tuning
   
   Fitted with several regression model , Found XGboost evaluation metrics most efficient.
   Created Pipeline for Column transformation of Category & Standardization of numeric features.
   Fine Tuned models with RandomsearchCV to get optimum R2 Scores.
   feature Elimination
   
4) Model Deployment with Streamlit:
   
   Build an interactive web application using Streamlit to showcase the trained model's predictions.
   Enable users to input relevant features of a property and obtain an estimated rental price.
   Deploy the web application on a suitable platform to make it accessible to users. 

# Accuracy of Model

After training and tuning the machine learning model on the Home Rental Dataset, the performance of the best model is evaluated using accuracy as the evaluation metric. The model accuracy on the test set is 96%, which shows how well the model predicts the rental price based on the given features.

<img width="560" alt="image" src="https://github.com/Akashjha727/Rent_Prediction/assets/143934503/d00f76c4-9c25-4ccb-af2a-aabcac59fc36">

The above figure shows visualization of XGBoost Model accuracy train & test.

# Deployment with Streamlit

Please click on this link for Demo https://rent-prediction.streamlit.app/
Streamlit Deployment 
<img width="863" alt="image" src="https://github.com/Akashjha727/Rent_Prediction/assets/143934503/d4478a5c-2633-4938-bf2e-ac5087de6de9">
<img width="884" alt="image" src="https://github.com/Akashjha727/Rent_Prediction/assets/143934503/c1d02aad-0fc3-463f-b137-63d60293ba6f">

<img width="873" alt="image" src="https://github.com/Akashjha727/Rent_Prediction/assets/143934503/058a6a8a-224e-401d-b9fe-a154a8aeee87">

<img width="877" alt="image" src="https://github.com/Akashjha727/Rent_Prediction/assets/143934503/de017d94-10da-43cd-863d-aaa42555eb38">


