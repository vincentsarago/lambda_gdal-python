# Lambda gdal-python

Create a python Lambda function with [GDAL](http://gdal.org) python bindings
 
I assume you know a to start and EC2 (AMAZON Linux AMI) and to run some basics shell commands

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
./configure --prefix=/home/ec2-user/app/local
make
make install

cd ..

wget http://download.osgeo.org/gdal/1.11.3/gdal-1.11.3.tar.gz
tar -xzvf gdal-1.11.3.tar.gz
cd gdal-1.11.3
./configure --prefix=/home/ec2-user/app/local  \
    --with-geos=/home/ec2-user/app/local/bin/geos-config  \
    --with-static-proj4=/home/ec2-user/app/local \
    --with-curl \
    --with-python
make
make install
cd ..
```

###### Create you python function

```sh
touch mylambdafunction.py

```

###### Edit your Function






