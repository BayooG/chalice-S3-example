import boto3
import base64
import uuid

s3 = boto3.resource('s3')
bucket_name = 'obays'


def save_img(img: str, id=0):
    try:
        formt, imgstr = img.split(';base64,') 
        ext = formt.split('/')[-1]    
        imgdata = base64.b64decode(imgstr)
        filename = str(uuid.uuid4().hex) + '.'+ ext
        url = save_b64_to_S3(imgdata, filename)
        return url
    except:
        return False


def save_b64_to_S3(b64decoded, filename):
    obj = s3.Object(bucket_name,filename)
    obj.put(Body= b64decoded)
    location = boto3.client('s3').get_bucket_location(Bucket=bucket_name)['LocationConstraint']
    object_url = "https://%s.s3-%s.amazonaws.com/%s" % (bucket_name,location, filename)
    return object_url
