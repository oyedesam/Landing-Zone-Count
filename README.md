# Landing-Zone-Count
A python script to count the number of data that go into the Landing zone on a particular day




## Configure AWS Account

execute

```saml2aws configure -a default --role=arn:aws:iam::735745001007:role/ADFS-ReadOnly -p default -r eu-west-1```

Login

```saml2aws login -a default```

## Install Prequisites

To install packages, execute

```python install.py```


## Start the Application

To run the application you need to replace <BucketName> with the actual bucketname and <BucketFilePath> with the bucket file path.

```  python count.py <BucketName> <BucketFilePath> ```
