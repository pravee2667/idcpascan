# -*- coding: utf-8 -*-

import boto3
#from config import S3_KEY, S3_SECRET, S3_BUCKET

s3 = boto3.client(
   's3',
   aws_access_key_id="AKIATXCWEQVALA7AD5QM",
   aws_secret_access_key="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"
)

def upload_file_s3(file,bucket_name,acl="public-read"):
    try:
        s3.upload_fileobj(
                file,
                bucket_name,
                file.filename,
                ExtraArgs={
                        "ACL":acl,
                        "ContentType":file.content_type
                        }
                )
        objs=s3.list_objects(Bucket=bucket_name)
        all_files=objs["Contents"]
        return all_files
    except Exception as e:
        print("Something happened :",e)
        return e
    #return "{}{}".format("https://textractpython.s3.amazonaws.com/",file.filename)
    



