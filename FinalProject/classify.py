import pandas as pd
import subprocess
from sklearn.model_selection import train_test_split

# Files containing the training data
csv_train_files = ["features-timeslice-1.csv", "features-timeslice-2.csv", "features-timeslice-3.csv", 
             "features-timeslice-4.csv", "features-timeslice-5.csv"]

# number of features in the training data
num_features = 15

def split(data):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=1) # 0.25 x 0.8 = 0.2
    return X_train, y_train, 


def parse_csv():
    return None

def classify(file, model):

    columns = list(range(0,15))
    accuracy_improves = True
    max_accuracy     = -1
    overall_accuracy = -1
    feature_set = []

    while (accuracy_improves):

        for i in columns:
            # Run A2.java to train models in WEKA
            # args: <path to csv> <model type (1=Decision Tree, 2=Random Forest, 3=SVM)> <features indices>
            result = subprocess.check_output(["java", "-cp", ".:util/weka.jar", "A2", file, model] + feature_set + [str(i)], stderr=subprocess.STDOUT)
            #print("java -cp .:util/weka.jar A2 " + file + " " + model + " " + str(feature_set + [i]))
            result = result.decode('utf-8').split(' ')

            # Obtain accuracy of the model for that feature combo
            accuracy = float(result[-1].replace('%', ''))
            #print(feature_set + [str(i)], " ", accuracy)
            
            if (accuracy > max_accuracy):
                best_feature = i
                max_accuracy = accuracy
        

        #print("best_feature = " + str(best_feature) + " with acc=" + str(max_accuracy))

        if (not(str(best_feature) in feature_set)):
            feature_set.append(str(best_feature))
            columns.remove(best_feature)

        if (max_accuracy > overall_accuracy):
            overall_accuracy = max_accuracy

            if (len(columns) < 1):
                accuracy_improves = False
        else:
            accuracy_improves = False

    print(feature_set, " final accuracy=", str(overall_accuracy))

    result = subprocess.check_output(["java", "-cp", ".:util/weka.jar", "A2", file, model] + [str(i) for i in range(0,15)], stderr=subprocess.STDOUT)
    result = result.decode('utf-8').split(' ')

    # Obtain accuracy of the model for that feature combo
    accuracy = float(result[-1].replace('%', ''))
    print([str(i) for i in range(0,15)], " ", accuracy) 

def main():
    # Compile A2.java
    subprocess.run(["javac", "-classpath", "util/weka.jar", "util/MyWekaUtils.java", "A2.java"])

    for file in csv_train_files:
        print("FILE: " + "'" + file + "'")
        # print("Decision Tree")
        # classify(file, "1")
        # print("Random Forest")
        # classify(file, "2")
        # print("SVM")
        # classify(file, "3")
        # print("")
        # print("Naive Bayes")
        # classify(file, "4")
        # print("")
        print("NN")
        classify(file, "5")
        print("")

if __name__=="__main__":
    main()