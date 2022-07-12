#!/bin/bash

# install dependencies for this tool
sudo apt install -y nvidia-cuda-toolkit python3-pip python3-opencv swig nvidia-cudnn

# python modules
python3 -m pip install numpy
python3 -m pip install matplotlib
python3 -m pip install tensorflow tensorboard
python3 -m pip install gdown
