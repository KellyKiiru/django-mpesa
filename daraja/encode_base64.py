import base64
from django.conf import settings

# def generate_password(date):
#     # Convert settings.LIPANAMPESA_PASSKEY and settings.BUSINESS_SHORT_CODE to strings
#     passkey = str(settings.LIPANAMPESA_PASSKEY)
#     business_short_code = str(settings.BUSINESS_SHORT_CODE)
    
#     data_to_encode = passkey + date + business_short_code
    
#     encoded_password = base64.b64encode(data_to_encode.encode(('utf-8')))
    
#     return encoded_password

def generate_password(date):
    # Convert settings.LIPANAMPESA_PASSKEY and settings.BUSINESS_SHORT_CODE to strings
    passkey = str(settings.LIPANAMPESA_PASSKEY)
    business_short_code = str(settings.BUSINESS_SHORT_CODE)
    
    data_to_encode = passkey + date + business_short_code
    
    encoded_string = base64.b64encode(data_to_encode.encode())
    
    encoded_password = encoded_string.decode("utf-8")
    
    return encoded_password

