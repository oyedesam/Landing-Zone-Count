# Landing-Zone-Count
A python script to count the number of data that go into the Landing zone on a particular day




## Configure AWS Account - Prelive

execute

```saml2aws configure -a default --role=arn:aws:iam::735745001007:role/ADFS-ReadOnly -p default -r eu-west-1```

Login

```saml2aws login -a default```

## Configure AWS Account - Live
execute

```saml2aws configure -a chssnd --role=arn:aws:iam::290364463189:role/ADFS-ReadOnly -p chssnd -r eu-west-1```

Login

```saml2aws login -a chssnd```

See https://confluence.tools.cha.rbxd.ds/display/ICISTECH/How+to+view+kubernetes+clusters#Howtoviewkubernetesclusters-ConnectingtoAWS for more information

## Install Prequisites

To install packages, execute

```python install.py```


## Start the Application

To run the application you need to replace <BucketName> with the actual bucketname and <BucketFilePath> with the bucket file path.

```  python count.py <BucketName> <BucketFilePath> ```

## Example

Bucket Name - adventureworks

Bucket File Path - test/files/

Run: 

```  python count.py adventureworks test/files/ ```

After executing the script above, A result.html file would be created in the root directory that would contain the results of the execution.


