# CS498-MileStoneProject
Lehigh University CS 498 Milestone Term Long LLM Practice Project, work with Ms. Wang Jiaming jiwb22@lehigh.edu
Image Enhancement and Reconstruction in Medical Imaging Using Generative AI (GAI) and GANs

Welcome to the CS498 Milestone Project repository! This project explores the use of Generative Adversarial Networks (GANs) and other Generative AI (GAI) methods to enhance and reconstruct medical images (e.g., CT, MRI, and X-ray). Our goal is to understand how these advanced models can tackle challenges in medical data, such as data scarcity, image noise, low resolution, and privacy concerns.
Table of Contents

    Project Overview
    Motivation and Objectives
    Key Techniques
    Project Milestones
    Planned Deliverables
    Resources and References
    How to Contribute

Project Overview

This repository is dedicated to investigating, designing, and demonstrating how Generative Adversarial Networks and related GAI models can be used in medical imaging:

    Image Enhancement & Super-Resolution: Improving quality, clarity, and resolution of low-quality medical scans.
    Image Reconstruction: Using GANs to reconstruct missing or corrupted image regions, potentially aiding in better diagnostics.
    Data Augmentation: Generating synthetic medical images to expand training data and address limited real-world datasets.
    Multimodal Image Translation: Converting between different imaging modalities (e.g., CT ↔ MRI) when one is missing or insufficient.

The research will also examine privacy-preserving approaches—such as federated learning or synthetic data generation—that can respect patient confidentiality.
Motivation and Objectives

    Enhance Image Quality:
    Many medical images suffer from low resolution, noise, or artifacts (especially in low-dose CT or high-speed MRI scans). By using GAN-based architectures, we can potentially achieve clearer images that aid in diagnosis.

    Address Data Scarcity:
    Medical datasets are often limited and privacy-restricted. We aim to explore GAN-driven data augmentation to increase dataset diversity without exposing sensitive information.

    Improve Diagnostic Support:
    Enhanced and reconstructed images may help downstream tasks such as tumor detection, organ segmentation, or disease classification.

    Explore Real-World Feasibility:
    Our project will examine the training and inference performance of various GAN models, as well as discuss privacy and regulatory considerations for real clinical settings.

Key Techniques

    Generative Adversarial Networks (GANs):
        Vanilla GANs for synthetic image generation.
        CycleGAN for image-to-image translation across different modalities.
        SRGAN for super-resolution enhancement (low- to high-resolution).
        WGAN / WGAN-GP to improve training stability and handle mode collapse.

    Transformers and LLMs (planned future integration):
        Potential use of Transformer-based architectures for advanced feature extraction, language modeling (in medical text analysis), or combined image–text tasks.

    Federated Learning (FL):
        Exploring how collaborative approaches can train GANs across multiple hospitals without sharing raw data.

Planned Deliverables

    Poster & Presentation:
    A concise visual overview of the project, including results, charts, or example images from any GAN experiments.

    Code & Documentation:
    Though currently this repository has no code, we plan to include:
        GAN training scripts (PyTorch or TensorFlow).
        Data preprocessing pipelines.
        Jupyter notebooks demonstrating experiments and visualizations.

    Article or Tool Release:
        An article explaining key findings, challenges, and best practices in GAI-based medical imaging.
        Alternatively, a web-based tool or demo that showcases model performance on sample medical images.

Resources and References

    Project Docs
        Milestone1 PDF (Describes the official requirements and grading details.)
        GANs in Medical Imaging Paper (Key literature on modern GAN advances and challenges.)

    Relevant Research Papers
        S. Islam et al.: Generative Adversarial Networks (GANs) in Medical Imaging: Advancements, Applications, and Challenges. IEEE Access, 2024.
        S. Sai et al.: Generative AI for Transformative Healthcare: A Comprehensive Study of Emerging Models, Applications, Case Studies, and Limitations. IEEE Access, 2024.

    Datasets (Pending)