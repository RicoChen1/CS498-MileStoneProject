# Image Enhancement and Reconstruction in Medical Imaging Using GANs

## Project Description

This project investigates the application of **Generative Adversarial Networks (GANs)** for medical image enhancement and reconstruction, with a focus on brain MRI data from the **BraTS 2020** dataset.  
Initially, a **vanilla GAN** was trained to generate realistic MRI-like slices.  
Subsequently, a **Pix2Pix conditional GAN** was implemented to perform supervised segmentation, learning to generate tumor masks from input MRI slices.  
The models were evaluated using standard segmentation metrics, including **Dice Coefficient** and **Intersection-over-Union (IoU)**.

## Data Source

- **Dataset**: [BraTS 2020 (Brain Tumor Segmentation Challenge)](https://www.kaggle.com/datasets/awsaf49/brats20-dataset-training-validation)

## Download Instructions

1. Create a Kaggle account.

2. Download your Kaggle API token (`kaggle.json`).

3. Install the Kaggle API:

   ```bash
   pip install kaggle
   ```

4. Run the following commands to authenticate and download the dataset:

   ```bash
   mkdir ~/.kaggle
   cp kaggle.json ~/.kaggle/
   chmod 600 ~/.kaggle/kaggle.json
   kaggle datasets download -d awsaf49/brats20-dataset-training-validation
   unzip brats20-dataset-training-validation.zip -d data/
   ```

- The extracted folder must be placed under the `data/` directory.

## Packages Required

The following packages are required to run the code:

- `tensorflow >= 2.0`
- `numpy`
- `pandas`
- `matplotlib`
- `scikit-learn`
- `nibabel`
- `kaggle`
- `keras`

You can install them using the following command:

```bash
pip install tensorflow numpy pandas matplotlib scikit-learn nibabel kaggle keras
```

## Instructions on How to Run the Code

1. **Prepare Data**:

   - Download the BraTS 2020 dataset as described above.
   - Place the extracted folder inside the `data/` directory.

2. **Run the Main Script**:

   - The `final_project_main.py` script includes:

     - Data loading and preprocessing
     - Building GAN and Pix2Pix models
     - Training the models
     - Generating segmentation predictions

3. **Outputs**:

   - During training, the Generator and Discriminator losses will be printed for each epoch.
   - After training, sample segmentation results will be visualized, comparing the **Input MRI**, **Ground Truth Mask**, and **Predicted Mask**.
