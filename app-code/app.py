import boto3

def lambda_handler(event, context):
    # Replace 'your-bucket-name' with the name of your S3 bucket
    bucket_name = 'lambda-poc-01'

    # Create an S3 client
    s3 = boto3.client('s3')

    # List all objects in the bucket
    response = s3.list_objects_v2(Bucket=bucket_name)

    # Check if there are any objects in the bucket
    if 'Contents' in response:
        # Print the names of all objects in the bucket
        for obj in response['Contents']:
            print(obj['Key'])
        return {
            'statusCode': 200,
            'body': 'Objects listed successfully.'
        }
    else:
        print(f"No objects found in the bucket: {bucket_name}")
        return {
            'statusCode': 404,
            'body': 'No objects found in the bucket.'
        }
