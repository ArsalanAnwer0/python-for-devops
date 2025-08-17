import boto3

s3 = boto3.resource('s3')

def show_all_buckets():
    for bucket in s3.buckets.all():
        print(bucket.name)
        
def upload_to_bucket(s3,file_name,source,bucket_name):
    data = open(source,'rb')
    s3.Bucket(bucket_name).put_object(Key=file_name,Body=data)
    print("Backup stored to s3")


source = input("Enter source path: ")
bucket_name = input("Enter bucket name: ")
file_name = input("What should be the file name: ")

show_all_buckets()
upload_to_bucket(s3,file_name,source,bucket_name)
