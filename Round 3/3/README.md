Place your Python code into a file named **classify.py**.

[Classification](https://en.wikipedia.org/wiki/Statistical_classification) is one of the main tasks in [machine learning](https://en.wikipedia.org/wiki/Machine_learning).  The problem deals with categorigal data: an underlying assumption is that each data item can be assigned into a certain category. The goal is to be able to deduce, by computational means,  the category of previously unknown data items. The general idea should become clear once you have read the whole question.

We will use real data about medical conditions related to [vertigo](https://en.wikipedia.org/wiki/Vertigo) (a disorder of the balance system). Each data item corresponds to a single patient and consists of several attributes (sometimes called features). The attributes convey information about what kind of symptoms etc. the patients have experienced. The goal is to be able to deduce the patient's condition (= classify, or actually diagnose, the patient) based on the symptoms.

#### The training data

You may download the file **vertigo_train.txt**, which contains training data about vertigo patients. Each row of the file describes both the correct classification and five attribute values for one data item (= patient). The values are separated from each other by white space (tab values). Therefore each row has a total of six values. The first line of the file is shown below.

```
1 4 1 1 5 0
```

The first line describes a data item whose correct class is 1 and whose five attributes (describing symptoms) have values 4, 1, 1, 5 and 0\. It is typical that all data is transformed into numeric form (to better enable e.g. statistical analysis of the values). For example in this case the class 1 really means a condition called [vestibular schwannoma](https://en.wikipedia.org/wiki/Vestibular_schwannoma). Each attribute gives, again in numeric form, information about the level or variation of some symptom.

#### Test data for prediction

The file **vertigo_predict.txt** contains test data about vertigo patients. This data is otherwise similar to the training data but now the first value, the correct classification, is missing. Therefore each row contains only five values. These five attribiute values are given in the same order as they appear in the training set.

In addition the file **vertigo_answers.txt** contains the true classifications for each patient in the test set. Each row contains only one value: the classification of the corresponding test patient. Here "correspondence" means the row index. Row **i** of the answers file corresponds to row **i** of the test file.

#### The task

Now to the actual task of this question.

Test how accurately the following two different methods are able to classify the data items of the test set when the given training set has been available to them.

*   A neural network variant called [perceptron](https://en.wikipedia.org/wiki/Perceptron).
    *   The [scikit-learn library](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html#sklearn.linear_model.Perceptron) offers an easy-to-use implementation of this method. You can first use it with default parameters.
        1.  Instantiate a Perceptron-object, e.g. **p = Perceptron()**.
        2.  Train the method: call **p.fit(data, classes)**.
            *   The **data** parameter should be a list of lists that describes the training data.
                *   Each sublist contains the five attributes (not the classification!) for a single data item.
                    *   The list could hence look something like **[[4, 1, 1, 5, 0], [5, 2, 3, 5, 0], ...]**.
            *   The **classes** parameter should be a list of correct classification categories.
                *   Value at index **i** tells the correct category of the data item **data[i]**.
                *   This list could look something like **[1, 1, ...]**.
            *   Make sure that the values are treated as numbers. When you read information from a file, it can by default be treated as strings.
        3.  Test how well this trained perceptron can classify the test data: call **p.predict(test)**.
            *   The **test** parameter is a list of lists that describes test data items. Its format is similar to the **data** parameter above.
            *   The function returns a list where the value at index **i** tells the predicted class for the data item **test[i]**.
                *   Compare these results to the separately provided correct classification categories and compute the percentage of correct predictions.
    *   After testing with the default parameters, also try if the parameter **n_iter** changes the results (e.g. instantiate the perceptron as **Perceptron(n_iter = 100)**).
*   A very simple "nearest neighbor" search.
    *   Given a data item, assing it to the same category as the training data item that is closest to it (= within least distance). Such a closest item is usually called a "nearest neighbor".
        *   How to measure the distance between two data items?
            *   You may use the so-called "[Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry)".
        *   If more than one training data items are equally close?
            *   You may select the category of any of such equally near neighbors.
    *   Compute the percentage of correct predictions also for this method.

Your program should finally print out information about both tested methods: how many percent of their predictions were correct. The format should be (just replace x and y with the actual percentages):

```
Perceptron: x% correct
Nearest neighbor: y% correct
```