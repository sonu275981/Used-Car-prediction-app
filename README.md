
# Used-Car-prediction-app

Cars are more than just a utility for many. We all have different tastes when it comes to owning a car or at least when thinking of owning one. Some fit in our budget and some lauxury brands are heavy on our pockets. But that should not stop us from owning it, atleast used ones. The goal of this project to predict the costs of used cars to enable the buyers to make informed purchase using the data collected from various sources and distributed across various locations in India.

## Dataset Descrption

Dataset used here is from a hackathon hosted by MachineHack. Go to the hackathon homepage to know more about the dataset. The dataset set contains features like Location, Manufacture details, car features such as Fuel type, Engine, and usage parameters. Below is the app in Working condition.

- Size of Dataset: 17,966 records

- Features:

- Name: The brand and model of the car.
- Year: The year or edition of the model.
- Kilometers_Driven: The total kilometres driven in the car by the previous owner(s) in KM.
- Fuel_Type: The type of fuel used by the car. Transmission: The type of transmission used by the car.
- Mileage: The standard mileage offered by the car company in kmpl or km/kg
- Engine: The displacement volume of the engine in cc.
- Power: The maximum power of the engine in bhp.
- Price: The price of the used car in US Dollor.

## key technical aspects

After data exploration and visualization various data prepossing steps are selected after of data. Following are noticeable ones among them.

- `New_Price` feature dropped due to significant missing values.
- Continuos variables including target feature are Log transformed to make their distribution symetrical.
- `Kilometers_Driven` and `Mileage` are multiplied together to form new feature as this interaction show high correlation with target feature `price`.
- `Brand`,`Model`, and `Location` are encoded using Target encoding as they have lot of categories.
- `Fuel_Type`, `transmission` are `one-hot encoded`.
- `Year` columns are deducted by current year to introduce aging effect (current year - edition year).

## Best Model selection

The data is trained on Linear Regression, KNN, SVM, Decision Tree,Random Forest, GBDT and XGBoost with hyper-parmeter tuning. GBDT turns out be best model with lowest loss of 0.033.




