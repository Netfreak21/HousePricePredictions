# Housing-Price-Predictions

### Problem Statement
Help Alzar, the record keeper for finding lost details of 3.5k houses with the help of Machine Learning.

### Installation
* Clone repository and run **feature_extraction.py** to create all_data.csv dataset. (Change the paths of all files accessed in *feature_extraction.py* to local paths on your machine first)
  * Dataset is given in form of text files so preprocessing is required to convert them into `csv file`
  * `feature_extraction.py` extracts data from text files and make `all_data.csv`.

### Requirements
* This problem statement uses **xgboost Regressor** so it must be installed through either of these ways.
  * **Using pip-** `pip install xgboost`
  * **Using conda-** `conda install -c py-xgboost`
* Python2.7 is preferred for this project.

### Usage
* Run `feature_extraction.py`to create dataset from raw text files to processed csv files.
* Run `feature_analysis.py`on Jupyter notebook to visualize dataset using functions of pandas dataframe.
* Run `feature_analysis.py` on Jupyter notebook to visualize relations between features and target value with the help of **histogram, scatter plots** and  **Heat Map**.

![Heat Map](https://github.com/pintugawar/House-Prices-Predictions/blob/master/Screenshot%20from%202018-07-09%2018-05-18.png)

* Run `regression.py` on Jupyter notebook for trying new features and feature selection and filling **NaN** values through **interpolation**.
  * After this data is ready to fit for different models.
* Running `regression.py`
  * This gives detail `r2_score analysis` after tuning hyperparameters of different types of regressions.
  * This will run `cross validation` across the training set on **LinearRegression**, **LassoRegression**, **Ridge Regression** and **xgboost Regression** and prints `r2_score`.


### Results
* With the help of `xgboost regressor` we are able to achieve r2_score of **0.99512**.
* `Solution.csv` is also given in repository to match results of test dataset.
* xgboost with tuned parameters gives final `r2_score` of **0.99553** on test dataset.
### Note : For avoiding errors update the file's path accessed in feature_extraction.py, feature_analysis.py and regression.py
