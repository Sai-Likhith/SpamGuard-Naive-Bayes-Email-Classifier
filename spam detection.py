import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

data = pd.read_csv('spam.csv', encoding='latin-1')
data = data[['v1', 'v2']]
data = data.rename(columns={"v1":"label", "v2":"text"})

data['label'] = data['label'].map({'ham': 0, 'spam': 1})

count_vector = CountVectorizer(stop_words='english')
training_data = count_vector.fit_transform(data['text'])

naive_bayes = MultinomialNB()
naive_bayes.fit(training_data, data['label'])

X_train, X_test, y_train, y_test = train_test_split(data['text'], data['label'], random_state=1)

count_vector = CountVectorizer(stop_words='english')
training_data = count_vector.fit_transform(X_train)
testing_data = count_vector.transform(X_test)

naive_bayes = MultinomialNB()
naive_bayes.fit(training_data, y_train)

predictions = naive_bayes.predict(testing_data)

print("Accuracy: {}% \n".format(naive_bayes.score(testing_data, y_test)*100))

email = input("Enter the E-mail body: \n")
testing_data = count_vector.transform([email])

if naive_bayes.predict(testing_data) == 0:
    print("\nThe email is NOT SPAM.")
else:
    print("\nThe email is SPAM")