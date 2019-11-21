#### flask
pip install -r module.txt

#### wsgi部署
gunicorn -w 4 -b 127.0.0.1:8000 app:app

建议使用以下方式,gunicorn支持gevent,能提升性能
gunicorn -w 4 -b 127.0.0.1:8000 -k 'gevent' app:app 
#### 