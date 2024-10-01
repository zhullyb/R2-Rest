import boto3

class R2:
    def __init__(self, info):
        self.client = boto3.client(
            service_name ="s3",
            endpoint_url = "https://{}.r2.cloudflarestorage.com".format(info["ACCOUNT_ID"]),
            aws_access_key_id = info["ACCESS_KEY_ID"],
            aws_secret_access_key = info["SECRET_ACCESS_KEY"],
            region_name = info["REGION"]
        )
        self.BUCKET_NAME = info["BUCKET_NAME"]

    def get_object(self, key):
        response = self.client.get_object(Bucket=self.BUCKET_NAME, Key=key)
        return response
    
    def get_list(self):
        response = self.client.list_objects(Bucket=self.BUCKET_NAME)
        return response
    

if __name__ == '__main__':
    from vars import info
    r2 = R2(info)
    print(r2.get_list())