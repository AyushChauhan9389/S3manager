from botocore.exceptions import ClientError

def list_s3_objects(s3_client, bucket_name):
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        return response.get('Contents', [])
    except ClientError as e:
        print(f"Error listing S3 objects: {e}")
        return []

def get_s3_object_url(s3_client, bucket_name, object_key):
    try:
        url = s3_client.generate_presigned_url('get_object',
                                               Params={'Bucket': bucket_name,
                                                       'Key': object_key},
                                               ExpiresIn=3600)
        return url
    except ClientError as e:
        print(f"Error generating presigned URL: {e}")
        return None

def upload_file_to_s3(s3_client, bucket_name, file_name, file_content):
    try:
        s3_client.upload_fileobj(file_content, bucket_name, file_name)
        print(f"File {file_name} uploaded successfully to {bucket_name}")
        return True
    except ClientError as e:
        print(f"Error uploading file to S3: {e}")
        return False