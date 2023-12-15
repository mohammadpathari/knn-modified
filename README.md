# PL-kNN (Performance with different Angle Thresholds)

This repository contains a modified version of the source code of PL-kNN, which is a model proposed to bypass the choice of the k parameter of the standard k-NN classifier. Our modified
code compares the accuracy for <u>different angle thresholds</u> which we've discovered plays a part in how the model performs.

The original PL-kNN model (found [here](https://github.com/SoftwareImpacts/SIMPAC-2022-275)) is based on the Smallest Modified k-Nearest Neighbors (SMKNN) presented by Ayyad et al. in
the following paper:

**Ayyad, S. M., Saleh, A. I., & Labib, L. M. (2019). Gene expression cancer classification using modified K-Nearest Neighbors technique. *Biosystems*, 176, 41-51.**

# Our Results

We conducted this test over different seed level and different split ratios for our training and testing data. In our results' folder we have included the accuracy levels we obtained
for different angle thresholds over Train-Test split ratios of 80:20 & 75:25. The original PL-kNN code used a randomizer to shuffle the data for each iteration. However, we used the
seed function to reproduce our exact results. Here is one example of our analysis:

**For a Train-Test Split of 80:20 {seed value 5}**

![Screenshot](https://raw.githubusercontent.com/Christo77793/PL-kNN-Modified/main/Results/Dataset%20Split%2080-20/Seed%205.png)

The original model used a fixed value of 90 for their angle threshold. However, the above image demonstrates that depending on the angle threshold selected we can obtained lower and
higher accuracy results. In the above image we have compared the original angle threshold with various different angle thresholds to see how the original choice compares with other
angles.

# Usage

The proposed model was aimed to be easy to implement and so to use it just clone the code and run app.py to view our contribution to the Pl-kNN model.

To reproduce our results the specific seed values to be used are:

* Train-Test Split 75:25 Seed 5 & 13
* Train-Test Split 80:20 Seed 5 & 9

# Citations

**Jodas, D.S., Passos, L.A., Papa, J.P. (2022, June 01–03). PL-kNN: A parameterless nearest neighbors classifier. [Paper presentation]. *IWSSIP 2022 - International Conference on
Systems, Signals and Image Processing*, Sofia, Bulgaria. [http://iwssip.bg](http://iwssip.bg)**

# Group members

| Name                     | E-mail                            |
| ----------------------   | ----------------------            |
| Mohammad Pathari         | 200551416@student.georgianc.on.ca | 
