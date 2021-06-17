# IntelImageClassification

* Created a tool which is able to classify images between Buildings, Forests, Glaciers, Mountains, Sea and Street.
* Dataset was taken from kaggle. 
* Link for dataset: https://www.kaggle.com/puneet6060/intel-image-classification
* Did a comparative analysis of performance of Inception-V3, ResNet-50, VGG-16, Xception and a Custom CNN on the dataset. 
* Built an API on Flask using the best model and deployed it on a local server 


## Code and Resources Used 
**Python Version:** 3.7  
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle, tensorflow, keras

## Overview
The CNN base with imagenet weights were imported of each model and a stack of Fully Connected Layers were added to it. After that fine tuning was performed on each model.
Each model was trained for 20 epochs.

There were <b>14034</b> images in the training set and <b>3000</b> images in the validation set.

The classes which the model can predict are as follows:
      <br></br>
			1.Buildings
      <br></br>
			2.Forests
			<br></br>
			3.Glacier
      <br></br>
			4.Mountains
			<br></br>
			5.Sea
			<br></br>
			6.Street

The Training and Validation Accuracy of each model after 20 epochs is as follows:

| Model      | Training Accuracy | Validation Accuracy   |
| :---        |    :----:   |          ---: |
| InceptionV3      | 99.32%      | 91.87%   |
| VGG16   | 90.24%        | 88.93%      |
| Xception   | 99.47        | 93.37%      |
| ResNet50   | 99.48        | 92.80%      |
| Custom Model   | 86.9%        | 87.10%      |
			

The accuracy and loss visualizations are as follows:

Training Accuracy

![image](https://user-images.githubusercontent.com/56645508/122374916-63ad5700-cf80-11eb-8e7c-d2ec05b298c6.png)


Validation Accuracy

![image](https://user-images.githubusercontent.com/56645508/122374944-69a33800-cf80-11eb-9baa-aff43b7b06fe.png)


Training Loss

![image](https://user-images.githubusercontent.com/56645508/122374965-6f991900-cf80-11eb-9b07-95515658784e.png)



Validation Loss

![image](https://user-images.githubusercontent.com/56645508/122374990-745dcd00-cf80-11eb-8804-34846f1460f8.png)




After 20 Epochs Xception had the highest validation accuracy, hence it was deployed using flask.

The Screenshot of the final model is as follows:

![image](https://user-images.githubusercontent.com/56645508/112270207-5cd3b880-8c9f-11eb-9d38-b131b2f846eb.png)


![image](https://user-images.githubusercontent.com/56645508/112270184-534a5080-8c9f-11eb-8e8a-0351d6fc8b6b.png)

			
		


