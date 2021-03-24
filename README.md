# IntelImageClassification

In this project 4 models were created which is able to classify between 6 classes present in the Intel Image Classification Dataset

The models used were InceptionV3, ResNet50, VGG19, Xception.

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
| InceptionV3      | 98.94      | 92.33   |
| VGG19   | 17.93        | 17.50      |
| Xception   | 98.41        | 92.27      |
| ResNet50   | 97.86        | 92.63      |
			

The accuracy and loss visualizations are as follows:

Training Accuracy

![image](https://user-images.githubusercontent.com/56645508/112268510-18471d80-8c9d-11eb-982e-7d955cc9ac75.png)

Validation Accuracy

![image](https://user-images.githubusercontent.com/56645508/112268625-44629e80-8c9d-11eb-8a24-480d7345ddd5.png)


Training Loss

![image](https://user-images.githubusercontent.com/56645508/112268640-49bfe900-8c9d-11eb-9069-22f4afd44dd3.png)


Validation Loss

![image](https://user-images.githubusercontent.com/56645508/112268655-4fb5ca00-8c9d-11eb-82bc-44a3e2f20dad.png)



After 20 Epochs ResNet50 had the highest validation accuracy, hence it was deployed using flask.

The Screenshot of the final model is as follows:

![image](https://user-images.githubusercontent.com/56645508/112270207-5cd3b880-8c9f-11eb-9d38-b131b2f846eb.png)


![image](https://user-images.githubusercontent.com/56645508/112270184-534a5080-8c9f-11eb-8e8a-0351d6fc8b6b.png)

			
		


