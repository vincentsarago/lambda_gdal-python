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

###### Update and Install Python