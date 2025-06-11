from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    location = "media"         # files live at s3…/media/…
    default_acl = "private"    # keep bucket private; Django will sign URLs
    file_overwrite = False     # don't overwrite on same filename
