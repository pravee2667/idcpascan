# -*- coding: utf-8 -*-

import os


S3_BUCKET=os.environ.get("textractpython")
S3_KEY=os.environ.get("AKIATXCWEQVAKHIFDH4W")
S3_ACCESS_ID=os.environ.get("67k3XjzDFb4ttnAxO3EbE1w/G9w2R6q32qtXAqlt")
S3_LOCATION='https://{}.s3.amazonaws.com/'.format(S3_BUCKET)
SECRET_KEY=os.urandom(32)
DEBUG=True
PORT=5000