import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.metrics import confusion_matrix

#read and clean

d=pd.read_csv("/content/psyc.csv")
data=pd.DataFrame(d)

#convert string values to numeric values
data['gender'] = data['gender'].replace({'Female': 1,'Male':0})
data['Personality'] = data['Personality'].map({'dependable': 0,
                                           'extraverted': 1,
                                           'lively': 2,
                                           'responsible': 3,
                                           'serious': 4})

#training and fitting model

X = data.iloc[:,0:7:1]
y = data.iloc[:,7:8:1]
y=y.astype('int')


# splitting X and y into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=45)
# training the model on training set
gnb = GaussianNB()
gnb.fit(X_train.values, y_train.values.ravel())


#making predictions on the testing set
y_pred = gnb.predict(X_test.values)


#accuracy of model
print("Gaussian Naive Bayes model accuracy (in %): ", metrics.accuracy_score(y_test, y_pred)*100)
#  confusion matrix
print()
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)

#predicting
#Questions
print()

while(1):
 age1=input("Enter your age: ")
 if(age1.isdigit()==0):
   print("Enter integer value!")
 elif(int(age1)>=0 and int(age1)<=100):
  break
 else:
  print("Enter valid input!")

while(1):
 gender1=input("Enter your gender (0-Male/1-Female): ")
 if( gender1.isdigit() and (int(gender1)==0 or int(gender1)==1)):
  break
 else:
  print("Enter valid input!")

print("\nOn scale 1-9 rate (1-lowest & 9-highest): \n")
while(1):
 a=input("1. Your openness / willingness to adjust according to different situations: ")
 if(a.isdigit() and int(a)>=1 and int(a)<=9):
  break
 else:
  print("Enter valid input!\n")

while(1):
 b=input("2. Your neuroticism / negative emotions: ")
 if(b.isdigit() and int(b)>=1 and int(b)<=9):
  break
 else:
  print("Enter valid input!\n")

while(1):
 c=input("3. Your conscientiousness / being responsible, careful or diligent: ")
 if(c.isdigit() and int(c)>=1 and int(c)<=9):
  break
 else:
  print("Enter valid input!\n")

while(1):
 d=input("4. Your agreeableness / ability to accept things: ")
 if(d.isdigit() and int(d)>=1 and int(d)<=9):
  break
 else:
  print("Enter valid input!\n")

while(1):
 e=input("5. Your extraversion / ability to socialize: ")
 if(e.isdigit() and int(e)>=1 and int(e)<=9):
  break
 else:
  print("Enter valid input!\n")


# Making predictions on new data
new_data = pd.DataFrame([{'gender':gender1, 'age': age1 ,'openness': a, 'neuroticism': b, 'conscientiousness': c, 'agreeableness': d, 'extraversion': e}])
predictions = gnb.predict(new_data.values)

# printing the predicted personality
personality_map = {0: 'dependable', 1: 'extraverted', 2: 'lively', 3: 'responsible', 4: 'serious'}
z=predictions.squeeze(0)
print("\nPredicted Personality:", personality_map[int(z)])


#book recommendations

bookgenres = {
    0: ["Self-help", "Leadership", "Personal development","Business ", "Time management","Psychology"],
    1: ["Thrillers", "Adventure", "Romance (with strong social elements)","Action and Adventure", "Mystery and Suspense", "Historical"],
    2: ["Biographies", "Memoirs", "Travel literature","Pop culture and Entertainment", "Humor and Satire", "Food and cooking"],
    3: ["Self-help", "Leadership", "Personal development","Business ", "Time management","Psychology"],
    4: ["Historical fiction", "Literary classics", "Philosophy","Political and social books", "Fiction", "Poetry"]
}

print("Being a person of ",personality_map[int(z)]," personality type, you would enjoy reading the following book genres:\n" )

genres=bookgenres[int(z)]
for i in genres:
  print("  ->",i)

print("\nHappy Reading !!")
