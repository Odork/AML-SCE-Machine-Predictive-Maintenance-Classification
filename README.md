Machine Predictive Maintenance Classification
This application is designed to predict machine failure for predictive maintenance using machine learning. It utilizes a synthetic dataset with 10,000 data points and 14 features.



Dataset Description
The dataset consists of the following features:

UID: Unique identifier ranging from 1 to 10000.
productID: Product quality variant with letters L, M, or H, and a variant-specific serial number.
air temperature [K]: Generated using a random walk process, later normalized to a standard deviation of 2 K around 300 K.
process temperature [K]: Generated using a random walk process, normalized to a standard deviation of 1 K, added to the air temperature plus 10 K.
rotational speed [rpm]: Calculated from power of 2860 W, overlaid with normally distributed noise.
torque [Nm]: Torque values are normally distributed around 40 Nm with an Ïƒ = 10 Nm and no negative values.
tool wear [min]: The quality variants H/M/L add 5/3/2 minutes of tool wear to the used tool in the process.
machine failure: A label that indicates whether the machine has failed in this particular data point for any of the following failure modes.
Important Note: There are two targets in the dataset. Do not use one of them as a feature, as it will lead to data leakage.


Dependencies
Python 3.x
Streamlit
Pandas
Scikit-learn



Model Details
The predictive model used in this application is a Random Forest Classifier, a powerful ensemble learning method that can handle both numerical and categorical features.
The model is trained on the synthetic dataset and can predict whether the machine will experience failure based on the input parameters.



