#### flask
pip install -r module.txt

#### wsgi部署
gunicorn -w 4 -b 127.0.0.1:8000 app:app

gunicorn -w 4 -b 127.0.0.1:8000 -k 'gevent' app:app 
#### 