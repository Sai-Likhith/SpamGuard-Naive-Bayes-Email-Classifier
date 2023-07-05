# SpamGuard-Naive-Bayes-Email-Classifier
SpamGuard is an efficient email classification system powered by Naive Bayes algorithm. It quickly analyzes the content of an email, evaluating its likelihood of being spam. With a simple input of the email body, SpamGuard accurately determines whether the email is spam or not, providing users with a reliable and effective tool for spam detection.

The approach for the SpamGuard system is as follows:

**1. Data Preparation:** Load the dataset containing labeled emails (spam and non-spam) using pandas. Extract the relevant columns for label and text content. Rename the columns accordingly.

**2. Data Preprocessing:** Map the labels to numeric values (0 for non-spam, 1 for spam). Perform text preprocessing, such as removing stop words and tokenizing, using the CountVectorizer from sklearn.

**3. Training the Classifier:** Split the dataset into training and testing sets using train_test_split. Fit the training data to the Multinomial Naive Bayes classifier, which is suitable for text classification tasks.

**4. Prediction:** Take user input as the email body to be classified. Transform the input using the trained CountVectorizer. Predict the label (spam or non-spam) using the Naive Bayes classifier.

**5. Output:** Display the prediction result to the user, indicating whether the email is spam or not. Additionally, provide the accuracy of the classifier on the testing data.

This approach combines data preprocessing, training, and prediction steps to accurately classify emails as spam or non-spam based on their content.

![image](https://github.com/Sai-Likhith/SpamGuard-Naive-Bayes-Email-Classifier/assets/102646751/870f571f-a043-4a5a-be83-2858371b7228)
