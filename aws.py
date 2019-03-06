import boto3

s3=boto3.client('s3')
ec2 = boto3.client('ec2')
iam = boto3.client('iam')


###run (aws configure ) for your account in terminal
###run (pip install boto3)
###Copy this in new file and name it aws.py
###run (python aws.py)

def getbuckets():
    buckets=s3.list_buckets()
    bucketlist=[]
    for i in buckets['Buckets']:
        bucket= i['Name']
        bucketlist.append(bucket)
    
    return {"buckets":bucketlist}

print(getbuckets())

##use this link >>> https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#client
##and add more functions and test it