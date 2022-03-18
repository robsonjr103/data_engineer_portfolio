class S3Utils():
    """
    Summary: Class with methods for create the S3 Bucket and it folders.
    """

    def create_bucket(self, client = None , bucket_name: str, bucket_location: str):
        """
        Summary: Creates a S3 Bucket with a given name and location

        Args:
          : client (boto3 S3 client): S3 client created in boto3
          : bucket_name (str): The bucket name, following all the restrictions of buckets name in AWS
          : bucket_location (str): The location to create the Bucket. Exemple: 'us-west-1'
        """

        #! Verify if client exists, if not, create one. If a exception occurs, raise a exception
        if client == None:
            
            try:
                client = boto3.client('s3')
            
            except:
                raise BaseException('There was an error trying to create the S3 client in boto3, check that boto3 is installed and available')
            
          
        #! Create the bucket
        response = client.create_bucket(
                Bucket = bucket_name,
                CreateBucketConfiguration = {
                    'LocationConstraint': bucket_location
                }
        )

        return response

    def create_object(self, client = None, bucket_name: str, key: str):
        """
        Summary: Creates a object in a S3 Bucket with a given key

        Args:
          : client (boto3 S3 client): S3 client created in boto3
          : bucket_name (str): Bucket name to create the object
          : key (str): Object key to create
        """

        #! Verify if client exists, if not, create one. If a exception occurs, raise a exception
        if client == None:

            try:
                client = boto3.client('s3')
            
            except:
                raise BaseException('There was an error trying to create the S3 client in boto3, check that boto3 is installed and available')

        #! Create the object
        response = client.put_object(
                Bucket = bucket_name,
                Key = (key)
        )
  
        return response
