# Lambda gdal-python

Create a python Lambda function with [GDAL](http://gdal.org) python bindings

Related with RemotePixel.ca [blog](http://remotepixel.ca/blog/landsat8-ndvi-20160212.html)
 
I assume you know how to start an EC2 virtual server (with AMAZON Linux AMI) and to run some basics shell commands

###### Update and Install Python

```sh
sudo yum update
sudo yum install python27-devel python27-pip gcc libjpeg-devel zlib-devel gcc-c++ python-devel libpng-devel freetype-devel libcurl-devel

```

###### Create a directory where to devellop function

```sh
mkdir /home/ec2-user/lambda
mkdir /home/ec2-user/lambda/local
cd /home/ec2-user/lambda
```

###### Create a virtualenv and activate it

```sh
virtualenv env
source env/bin/activate
```

###### Install some Python modules

```sh
pip --no-cache-dir install numpy
```

###### Download and Install GDAL

```sh
wget https://github.com/OSGeo/proj.4/archive/4.9.2.tar.gz
tar -zvxf 4.9.2.tar.gz
cd proj.4-4.9.2/
./configure --prefix=/home/ec2-user/lambda/local
make
make install

cd ..

wget http://download.osgeo.org/gdal/1.11.3/gdal-1.11.3.tar.gz
tar -xzvf gdal-1.11.3.tar.gz
cd gdal-1.11.3
./configure --prefix=/home/ec2-user/lambda/local  \
    --with-geos=/home/ec2-user/lambda/local/bin/geos-config  \
    --with-static-proj4=/home/ec2-user/lambda/local \
    --with-curl \
    --with-python
make
make install
cd ..
```

###### Create you python function

```sh
vi /home/ec2-user/lambda/mylambdafunction.py

```

###### Edit your function 

In order to get osgeo.gdal to load you new to set the GDAL_DATA path in the environment variable and load some shared libraries 

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from ctypes import cdll

#Set environment variables and load shared libraries
path = os.path.dirname(os.path.realpath(__file__))
os.environ['GDAL_DATA'] = os.path.join(path, "local/share/gdal")
lib2 = cdll.LoadLibrary(os.path.join(path, 'local/lib/libproj.so.9'))
lib1 = cdll.LoadLibrary(os.path.join(path, 'local/lib/libgdal.so'))

#Import gdal modules
from osgeo import gdal

def processing_func(event, context):
    "This is my worker function that responds to an API getaway call"
    
    #Whatever you want
    
    return results 

```

###### Creating a Deployment Package
You have create a zip file with everything you need (shared libraries and python packages)

First we need to move the osgeo package into the site-packages root directory
```sh
cd $VIRTUAL_ENV/lib64/python2.7/site-packages/GDAL-1.11.3-py2.7-linux-x86_64.egg
mv o* ../
mv g* ../
cd $VIRTUAL_ENV/..
```

We can now zip everything

```sh
zip -9 lambda.zip mylambdafunction.py
zip -r9 lambda.zip local/lib/libgdal.so
zip -r9 lambda.zip local/lib/libproj.so.9
zip -r9 lambda.zip local/share
cd $VIRTUAL_ENV/lib/python2.7/site-packages
zip -r9 /home/ec2-user/lambda/lambda.zip *
cd $VIRTUAL_ENV/lib64/python2.7/site-packages
zip -r9 /home/ec2-user/lambda/lambda.zip *

```

###### We're done you can now upload your lambda.zip in AWS S3 and call your worker (mylambdafunction.processing_func) using API gateway for example)

  
More
-------
- Running Python with compiled code on AWS Lambda [PerryGeo Blog](http://www.perrygeo.com/running-python-with-compiled-code-on-aws-lambda.html)
- AWS Lambda [Getting Started](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)

