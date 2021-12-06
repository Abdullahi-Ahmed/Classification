# Classification
I know there's alot of blogs and acticles about what classification problem is in machine learning.  
this read me won't compite with those acticle to drive the best way you could understand classification but contribute to those acticle to give you options.  
Am not a writer and I don't expect to write the best piece but I promise i will try my best for your option collections.
Classification problem is when you are trying to predict a class or label in a given dataset.  
A good example of Classification problem is this repo. the provided data has columns and there's an important column labelled "outcome" thats the column we're trying to predict

### Real Life Problem
is many cases the client you're working for or the project you're working on expect you to label the columns and identify the problem statement on your own. I know many Love advice will say follow your heart and don't let you head get in the way, well this is the opposite. But don't worry when a client expect you to define the problem statement you've already above the data science ladder and it will be a piece of cake.  
For those who are finding hard to grasp don't worry I will walk you though this repo.

## This Repo
#### Objectives
1. Download the data  
2. Understand the problem statement
3. Data preprocessing
4. Modeling
5. Performance metrics  
   
##### Downloading the data
click Healthcare - Diabetes.zip file then click download button on the far right, incase for some reason you can't download click view raw.  
  
##### Understanding the problem statement
To make it easy for you it's classification problem.  
How did i know it? it's very simply, whenever you're working on a data that has a class or label and you're acquired to use that class to predict then that's a classification problem. popular examples are spam detection, fraud detection, customer churn prediction and many more.  
There two types of Classification problem;
                                          1. Binary classification - it's when you have only two class to predict i.e predicting if someone is Short or Tall 
                                          2. Multi- class - it's when you have more than two class to predict i.e predicting  if someone is Short, Medium or Tall.
###### Look Out For.
In some cases people confuse classification problem with clustering problem, Clustering problem may look similar to classification problem but if the data in hand doesn't label the value you want to predict then it's not classification use case. Clustering algorithm is sometimes used as feature engineering for classification use cases. a good blog to look into https://towardsdatascience.com/cluster-then-predict-for-classification-tasks-142fdfdc87d6

##### Data preprocessing
Data Preprocessing is a Data Mining technique that involves transforming raw data into an understandable format According to Techopedia.  
In this repo I will only focus on Missing data and how to solve it but in real cases data is always dirt and will take almost 40% cleaning the data.  
First things first, Check if we have missing values?
![image](/Classification/images/Screenshot 2021-12-06 204029.jpg?raw=true "Optional Title")





as you can see we don't have missing values but that we do have Zeros in Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI columns and we know that Glucose level can never be zero or Blood pressure be zero thus the data is corrupted.  
Let's replace zero values to the average value of that column (i.e we replace zeros in Glucose column with it's average which is 120.89453125 and do the same) I won't advice this in case the zero values are alot.  
You can also drop the raws that have zero values instead.





It's Always important to Check if our dataset is balanced.










##### Model
In most cases you don't know which Algorithm can produce the best result and you constantly compare Algorithm while monitoring underfitting & overfitting. This field have advanced that in big project we use AutoML technology to help us identify the optimal Algorithm to use. We also use hyper-parameter tunning to further improve our score after identifying an Algorithm. Check out my https://github.com/Abdullahi-Ahmed/Random_Search README.  
We are randomly taking four different Algorithm and use the best score Algorithm:








##### Performance Metrics 
It's Very important to use the most appropriate performance metrics.  
What is  Performance metrics? it's a measure or result to judge if Algorithm is worth production. there are Alot of Performance Metrics in classification use case i.e
1. Confusion Metrics
2. FPR 
3. Recall 
4. Percision
5. Accurancy
6. F.beta
7. Cohen kappa  


I will end this read me with a story and question  
Imagine you have 10 people's heights which 9 of the them are tall and only one is short. If you use accurancy you will get 90% score  
Is this the best Metric to judge your Algorithm result?  
maybe you didn't get where am heading...  
in our case which metrics is important to focus,  
Predicting a healthy person to have diabetes or  
Predicting a diabetic person to be healthy

#### Will help you answer this in my next repo.


