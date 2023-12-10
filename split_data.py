from sklearn.model_selection import train_test_split

def split_data(data, target, test_size=0.3, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test

# Assuming 'data' is your dataset and 'target' is what you want to predict
data = []
target = []

X_train, X_test, y_train, y_test = split_data(data, target)

print("Training set:", X_train)
print("Test set:", X_test)