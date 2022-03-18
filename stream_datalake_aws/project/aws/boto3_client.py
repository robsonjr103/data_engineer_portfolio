def check_client(client, client_name: str = None):
    """
        Summary: Check if the 'client' is None. If true, try to create a boto3 client. If false, return the original client

        Args:
          : client_name (str): The boto3 client name. Exemple: s3, firehose, kinesis
          : client: Variable to verify if is a boto3 client or not
        """
    import boto3

    if client == None:
            
            try:
                client = boto3.client(client_name)
                return client
            
            except:
                raise BaseException(f"Can not found the boto3 {client_name} client. There was an error trying to create the {client_name} client in boto3, check that boto3 is installed and available as 'boto3'")
    

    else:
        return client
