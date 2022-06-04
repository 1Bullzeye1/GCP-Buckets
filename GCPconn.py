from google.cloud import storage


if __name__=="__main__":
    # sc = storage.Client()
    # buckets = sc.list_buckets()
    #
    # for bucket in buckets:
    #     print(bucket.name)


    def create_buck(bucket_name):

        # bucket_name = "buck-wilder"
        sc = storage.Client()
        bucket = sc.bucket(bucket_name)
        bucket.storage_class = "STANDARD"
        new_bucket = sc.create_bucket(bucket,location = "us-east1")

        print("created bucket {} in {} with storage class {}".format(new_bucket.name,new_bucket.location,new_bucket.storage_class))

        return new_bucket

create_buck("bucket-usregion")