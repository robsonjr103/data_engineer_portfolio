from boto3_client import check_client


class KinesisDataStreamUtils():
    """
    Summary: Class with methods to create the Kinesis Firehouse delivery stream
    """

    def create_stream(self, stream_name: str, stream_mode: str, shards: int = None, client = None):
        """
        Summary: Creates a Kinesis Firehouse delivery stream

        Args:
          : stream_name (str): The stream name, following all the restrictions of stream name in AWS
          : stream_mode (str): The delivery stream mode
          : shards (int): The quantity of shards for the provisioned stream. Necessary only if 'stream_mode' argument is 'PROVISIONED'
          : client (boto3 Firehouse client): Firehouse client created in boto3
        """

        #! Verify if client exists, if not, try create one.
        _client_name = 'kinesis' # Client of Firehouse in Boto3
        client = check_client(client, _client_name) # Function that verify if the client exist and create one if not exists

        #! Verify if the delivery stream type is valid
        _valid_stream_mode = ('PROVISIONED', 'ON_DEMAND') # Tuple of valid stream modes
        if stream_mode not in _valid_stream_mode:
            raise BaseException("Invalid Stream Mode: {stream_mode}. Valid Stream Mode: {_valid_stream_mode}")
        
        #! If the 'stream_mode' argument is 'ON_DEMAND', 'shards' argument is no necessary. If 'stream_mode' argument is "PROVESIONED", 'shards' argument are necessary
        if stream_mode == 'ON_DEMAND':

            #! Try create the stream
            response = client.create_stream(
            StreamName = stream_name,
            StreamModeDetails = {
                'StreamMode': stream_mode
            }
        )

        else:
            #! Verify if the shards number is equal or greater than 1
            if shards < 1:
                raise BaseException("Invalid Shard number: {shards}. Shard number need be equal or greater than 1")

            else:
                #! Try create the stream
                response = client.create_stream(
                    StreamName = stream_name,
                    ShardCount = shards,
                    StreamModeDetails = {
                        'StreamMode': stream_mode
                    }

                )

        return response