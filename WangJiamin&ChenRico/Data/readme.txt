# readme_data

Data Source: https://www.kaggle.com/datasets/awsaf49/brats20-dataset-training-validation/data

The dataset comes from Kaggle, BraTS2020 Dataset (Training + Validation). BraTS has always been focusing on the evaluation of state-of-the-art methods for the segmentation of brain tumors in multimodal magnetic resonance imaging (MRI) scans. BraTS 2020 utilizes multi-institutional pre-operative MRI scans and primarily focuses on the segmentation of intrinsically heterogeneous (in appearance, shape, and histology) brain tumors, namely gliomas. 

Our team choose this dataset by two reason. Firstly, our goal is to train and test GAN model in medical imaging enhancement, so we need to find medical images as the dataset. Additionally,  we referenced a paper "Generative adversarial networks in medical image reconstruction: A systematic literature review", which summarized the application progress of GANs in the field of medical image reconstruction. The paper has mentioned the BraTS (Brain Tumor Segmentation Challenge), so we find the dataset that collect data in the same filed. 

**Instructions for getting the dataset**:

1. Create a Kaggle account and obtain your Kaggle API token (kaggle.json).
2. Install the Kaggle API by running: pip install kaggle
3. Upload your kaggle.json file to the working directory.
4. Set up the Kaggle API authentication by moving kaggle.json to ~/.kaggle/ and setting the correct permissions.
5. Download the dataset by executing:
   kaggle datasets download -d awsaf49/brats20-dataset-training-validation
6. Unzip the downloaded file and place the extracted folder into the 'data/' directory.
