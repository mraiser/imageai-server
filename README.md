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
    # Assumes you are logged in as root in the /root directory

    apt-get install git gfortran libhdf5-dev libc-ares-dev libeigen3-dev libatlas-base-dev libopenblas-dev libblas-dev openmpi-bin libopenmpi-dev liblapack-dev cython python3-pip libopenjp2-7 libopenexr-dev libgtk-3-dev libilmbase-dev libavcodec-dev libavformat-dev libswscale-dev
    
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
    wget https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo-tiny.h5

Option 1 - Launch manually

    python3 server.py
    
    # Press Ctrl-c to exit

Option 2 - Install as service on port 8080:

    cp detection /etc/init.d/detection
    chmod 755 /etc/init.d/detection
    update-rc.d detection defaults
    service detection start

Option 3 - Install as load balanced 10 process service on port 80:

    chmod a+x launch10.sh
    cp detectionx10 /etc/init.d/detectionx10
    chmod 755 /etc/init.d/detectionx10
    update-rc.d detectionx10 defaults
    service detectionx10 start
    
    #install nginx
    apt-get install nginx
    mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf_ORIGINAL
    cp nginx.conf /etc/nginx/nginx.conf
    service nginx restart

## Usage
curl -F 'file=@/path/to/file/image.jpg' http://localhost:8080/upload

OR

Open http://localhost:8080 in web browser
