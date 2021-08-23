# House Rocket Analysis
In this project, we will analyze the dataset to generate insights, answer three main questions, create and answer our own hypotheses, and create a Web App that can be seen in the browser.

#### WARNING: It is recommended to see the main insights and final reports in the Web App before viewing the Notebooks

### The dataset was taken from Kaggle, at [link](https://www.kaggle.com/harlfoxem/housesalesprediction), with the following description:

"This dataset contains home sales prices for King County, which includes Seattle. It includes homes sold between May 2014 and May 2015.
It's a great dataset for evaluating simple regression models. "

## Business problem

The "CEO" of the imaginary company House Rocket works with the purchase and resale of real estate in Seattle, USA. He hired me to analyze a dataset with multiple homes available for purchase and then answer three main questions,

* 1 - Which houses should the CEO of House Rocket buy and at what price?

* 2 - As the house is owned by the company, what would the sale price be?

* 3 - When is the best time to sell them?

* 4 - Should House Rocket do a renovation to increase the sale price? What would be the suggestions for changes? What is the price increase given for each retrofit option?

In addition, I created and answered 3 hypotheses, in addition to creating a Web App that can be run and opened in the browser to have access to the main Insights and two maps of the houses.

# Web Application
### The Web App created by the Stramlit framework, which can be seen in the browser, contains the main Insights, tables with all houses available for purchase and houses recommended for purchase, in addition to the possible earnings from reselling the houses, whether the house is renovated or not.


#### To use the Web App, just follow these steps:

1. Edit the following snippet of the "app.py" file inside the APP folder. Inside it put the path to the project's root folder.

```python
project_path = "Put here the path to the project's root folder, the folder 'house_rocket_analysis'"
```

2. From the command line, run the following command:
```bash
streamlit run APP/appy.py
```

#### Now just go to the link provided in your browser.
---
---
# Notebook: 1.0-Data_Exploratory

### In this section, we'll explore the House Rocket dataset. We will follow these steps:

1. Identify missing or duplicate values ​​and treat them if necessary
2. Calculate descriptive statistics
3. Identify if there are outliers in the dataset and resolve them if necessary
4. Explore the correlation of house prices with other variables
#
# Notebook: 2.0-Main_Questions

### In this section, we'll answer the three main questions.
* In addition to generating the final table with the recommendation of the house to buy, the ideal resale price whether the house is renovated or not, in addition to the possible resale profit.

#
# Notebook: 3.0-Hypotheses

### In this section, we will create and answer our own hypotheses based on our knowledge of the dataset.
