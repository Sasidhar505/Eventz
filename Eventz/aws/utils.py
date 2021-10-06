from storages.backends.s3boto3 import S3Boto3Storage

StaticRootS3BotoStorage = lambda: S3Boto3Storage(location='my-eventz/static')
MediaRootS3BotoStorage = lambda: S3Boto3Storage(location='myeventz/media')
