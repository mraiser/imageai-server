# imageai-server
A simple HTTP server to automate detection of objects over a network

## Dependencies:
- https://github.com/OlafenwaMoses/ImageAI
- https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo-tiny.h5/

## Installation Overview
- Install ImageAI
- Copy yolo-tiny.h5 to project folder

## Step-by-step installation for Raspberry Pi 4
    # Adapted from https://qengineering.eu/install-tensorflow-2.2.0-on-raspberry-pi-4.html
    
    apt-get install gfortran libhdf5-dev libc-ares-dev libeigen3-dev libatlas-base-dev libopenblas-dev libblas-dev openmpi-bin libopenmpi-dev liblapack-dev cython python3-pip libopenjp2-7 libilmbase-dev libavcodec-dev libavformat-dev libswscale-dev
    
    pip3 install keras_applications==1.0.8 --no-deps
    pip3 install keras_preprocessing==1.1.0 --no-deps
    pip3 install -U --user six wheel mock
    pip3 install pybind11
    pip3 install h5py==2.10.0
    pip3 install --upgrade setuptools
    pip3 install gdown
    gdown https://drive.google.com/uc?id=11mujzVaFqa7R1_lB7q0kVPW22Ol51MPg
    pip3 install tensorflow-2.2.0-cp37-cp37m-linux_armv7l.whl
    pip3 install opencv-python
    pip3 install imageai --upgrade
    
    git clone https://github.com/mraiser/imageai-server.git imageai
    cd imageai
    python3 server.py


## Usage
curl -F 'file=@/path/to/file/image.jpg' http://localhost:8080/upload

OR

Open http://localhost:8080 in web browser
