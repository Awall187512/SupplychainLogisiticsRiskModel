Logistics and Supply Chain Risk Scoring#

I have a csv file with a list of data on various types of risk for different countries across Europe. My current csv model will combine these individual country scores to create a total score for a potential journey across Europe. I want to develop a machine learning program which fine tunes the various weightings to learn or fine tune the model to provide an accurate risk score given the variables which have been input. 

This would be classified as a prediction problem as the risk score output is a number. It may be defined as multi- input regression problem. As the model will be trained to predict the output based upon the individual risk scores for each country then this will be classed as a multi-input regression model the relationship of which can be considered parametric. 
My ambition is for the backpropagation aspect of the model to fine tune these hyperparameters to adapt each risk score given a variety of factors and gradually improve that output and accuracy. The current model inputs are as follows:

I currently only have the data on a European country level, however I can provide training, testing and validation datasets as required. 

Input Variables (CSV): 
Location data of point of origin (latitude and longitude)
Location data of destination (latitude and longitude)
Country Name(s)
Mode of transport
Journey Duration 
Country Employment Risk Score
Country Economic Risk Score
Country Weather Risk Score
Country Logistics Risk Score
Country Political Risk Score


Output:
Predicted Overall Risk Score for each country


-----------------------

The flask and output aspect of this code allows me to pull data from two points on a mapbox api and then search the datatable for the appropriate country to create a journey and output a very high level country score. 


