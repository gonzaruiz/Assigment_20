
# coding: utf-8

# In[ ]:


#Machine Learning 1 - Assigment_20


# In[ ]:


#1. What are the three stages to build the hypotheses or model in machine learning?


# In[ ]:


#Three stages to build the hypotheses or model :¶
#a) Model building
#b) Model testing
#c) Applying the model


# In[ ]:


#2. What is the standard approach to supervised learning?


# In[ ]:


# The standard approach to supervised learning is to split the set of example into the training set 
#and the test set to evalute our model selection and then apply the model which is more accurate & 
#efficient and overcome the issues such as underfitting & overfitting.


# In[ ]:


# 3. What is Training set and Test set?


# In[ ]:


#Training Set :
#It is part of dataset which are used to learn the behaviour of the data using the model selected.

#Test Set :
#Test set is used to test the accuracy of the hypotheses generated using the training set.


# In[ ]:


#4. What is the general principle of an ensemble method and what is bagging and boosting in ensemble method?


# In[ ]:


#General principle of an ensemble method :¶
#Ensemble model combines multiple "individual" (diverse) models together and delivers superior prediction power.

#Bagging :
#It is an ensemble method in which first, we create random samples of the training data set (sub sets of training 
#data set). Then, we build a classifier for each sample. Finally, results of these multiple classifiers are combined using average or majority voting. Bagging helps to reduce the variance error.

#Boosting :
#It provides sequential learning of the predictors. The first predictor is learned on the whole data set, while the following are learnt on the training set based on the performance of the previous 
#one. It starts by classifying original data set and giving equal weights to each observation. If classes are predicted incorrectly using the first learner, then it gives higher weight to the missed 
#classified observation. Being an iterative process, it continues to add classifier learner until a limit is reached in the number of models or accuracy. Boosting in general decreases the bias error 
#and builds strong predictive models. However, they may sometimes over fit on the training data.


# In[ ]:


#5. How can you avoid overfitting ?


# In[ ]:


#Steps for reducing overfitting:
#1. Add more data
#2. Use data augmentation
#3. Use architectures that generalize well
#4. Add regularization (mostly dropout, L1/L2 regularization are also possible)
#5. Reduce architecture complexity.
#Brief description on the above mentioned steps are as below :
#The first step is of course to collect more data. However, in most cases we will not
#be able to. Let’s assume we have collected all the data. The next step is data augmentation: 
#something that is always recommended to use. Data augmentation includes things like randomly 
#rotating the image, zooming in, adding a color filter etc. Data augmentation only happens to 
#the training set and not on the validation/test set. It can be useful to check if we are using 
#too much data augmentation. For example, if we zoom in so much that features of a cat are not 
#visible anymore, than the model is not going to get better from training on these images.

#The third step is to use an architecture that generalizes well. However, much more important is 
#the fourth step: adding regularization. The three most popular options are: dropout, L1 
#regularization and L2 regularization. Dropout deletes a random sample of the activations 
#(makes them zero) in training. In the Vgg model this is only applied in the fully connected 
#layers at the end of the model. However, it can also be applied to the convolutional layers. 
#We need to be aware that dropout causes information to get lost.

