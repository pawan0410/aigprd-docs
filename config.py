DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = r'mysql://root:root@127.0.0.1/aig_prd_form'
SQLALCHEMY_POOL_SIZE = 5
SQLALCHEMY_POOL_TIMEOUT = 120
SQLALCHEMY_POOL_RECYCLE = 280

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = r'kmt.aigbusiness@gmail.com'
MAIL_PASSWORD = r'atul123@#'
MAIL_USE_TLS = False
MAIL_USE_SSL = True