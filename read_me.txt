
###########################################################
#                                                         #
#    NLP Course Project Building RASA Chatbot             #
# ================================================        #
#														  #
###########################################################

###########################################################
#        This is the Read_Me file for Rasa Chatbot Project
###########################################################

Submitted By: Mudassar Majgaonkar
			  Divya Shanmugam
			  
Slack Demo for Project : https://www.youtube.com/watch?v=7SdTPhpB-bI 

Additional Details on Project can be found in file Implementaion_Details.pdf in the submitted folder.


Steps for training the model:
============================
1. cd <submitted folder>
2. Train NLU : On command prompt execute:  "rasa train nlu"
3. Train core: On command prompt execute:  "rasa train core"
4. Sometimes the stories arent populated so do this step: "rasa train -vv -dump-stories --force"
5. Start RASA action server: "rasa run actions -vv"
6. On another command prompt start shell: "rasa shell"

Now test the code.

- The training data is present in: ./data/nlu.md
- The stories are in: ./data/stories.md
- Trained models are present at: ./model/
- Intents,entities and synonyms defined in domain.yml
- Configuration details: config.yml
- Slack integration: credentials.yml

			  
Following is the environment details used for testing  this project.

RASA version used:
=================
rasa==1.6.1
rasa-nlu==0.15.1
rasa-sdk==1.6.1
rasa-x==0.24.1

Python Version Used:
===================
python==3.6.5 
python-crfsuite==0.9.6
python-dateutil==2.8.1
python-editor==1.0.4
python-engineio==3.11.2
python-socketio==4.4.0
python-telegram-bot==11.1.0
 

Additional details of the environment:
=====================================

absl-py==0.9.0
aiofiles==0.4.0
aiohttp==3.6.2
alembic==1.0.11
APScheduler==3.6.3
astor==0.8.1
async-generator==1.10
async-timeout==3.0.1
attrs==19.3.0
Automat==0.8.0
beautifulsoup4==4.8.2
blis==0.2.4
boto3==1.11.0
botocore==1.14.0
bs4==0.0.1
bz2file==0.98
cachetools==4.0.0
certifi==2019.11.28
cffi==1.13.2
chardet==3.0.4
Click==7.0
cloudpickle==0.6.1
colorama==0.4.3
colorclass==2.2.0
coloredlogs==10.0
colorhash==1.0.2
ConfigArgParse==1.0
constantly==15.1.0
cryptography==2.8
cycler==0.10.0
cymem==2.0.3
cytoolz==0.9.0.1
decorator==4.4.1
dill==0.2.9
dnspython==1.16.0
docopt==0.6.2
docutils==0.15.2
dopamine-rl==3.0.1
en-core-web-md==2.0.0
fbmessenger==6.0.0
Flask==1.1.1
future==0.17.1
gast==0.2.2
gevent==1.4.0
gin-config==0.3.0
gitdb2==2.0.6
GitPython==3.0.5
google-api-python-client==1.7.11
google-auth==1.10.0
google-auth-httplib2==0.0.3
google-pasta==0.1.8
googleapis-common-protos==1.6.0
greenlet==0.4.15
grpcio==1.26.0
gunicorn==20.0.4
gym==0.15.4
h11==0.8.1
h2==3.1.1
h5py==2.10.0
hpack==3.0.0
httpcore==0.3.0
httplib2==0.15.0
httptools==0.0.13
humanfriendly==4.18
hyperframe==5.2.0
hyperlink==19.0.0
idna==2.8
idna-ssl==1.1.0
importlib-metadata==1.4.0
incremental==17.5.0
isodate==0.6.0
itsdangerous==1.1.0
Jinja2==2.10.3
jmespath==0.9.4
jsonpickle==1.2
jsonschema==2.6.0
Keras-Applications==1.0.8
Keras-Preprocessing==1.1.0
kfac==0.2.0
kiwisolver==1.1.0
klein==17.10.0
Mako==1.1.0
Markdown==3.1.1
MarkupSafe==1.1.1
matplotlib==2.2.4
mattermostwrapper==2.1
mesh-tensorflow==0.1.9
more-itertools==8.1.0
mpmath==1.1.0
msgpack==0.5.6
msgpack-numpy==0.4.3.2
multidict==4.6.1
murmurhash==1.0.2
networkx==2.3
numpy==1.18.1
oauth2client==4.1.3
opencv-python==4.1.2.30
opt-einsum==3.1.0
packaging==18.0
pika==1.0.1
Pillow==7.0.0
plac==0.9.6
preshed==2.0.1
promise==2.3
prompt-toolkit==2.0.10
protobuf==3.11.2
pyasn1==0.4.8
pyasn1-modules==0.2.8
pycparser==2.19
pydot==1.4.1
pyglet==1.3.2
PyHamcrest==1.9.0
PyJWT==1.7.1
pykwalify==1.7.0
pymongo==3.10.1
pyparsing==2.4.6
pypng==0.0.20
pyreadline==2.1
pyrsistent==0.15.7
python-crfsuite==0.9.6
python-dateutil==2.8.1
python-editor==1.0.4
python-engineio==3.11.2
python-socketio==4.4.0
python-telegram-bot==11.1.0
python==3.6.5 
pytz==2019.3
PyYAML==5.3
questionary==1.4.0
rasa==1.6.1
rasa-nlu==0.15.1
rasa-sdk==1.6.1
rasa-x==0.24.1
redis==3.3.11
regex==2018.1.10
requests==2.22.0
requests-async==0.5.0
requests-toolbelt==0.9.1
rfc3986==1.3.2
rocketchat-API==0.6.36
rsa==4.0
ruamel.yaml==0.15.100
s3transfer==0.3.0
sanic==19.9.0
Sanic-Cors==0.9.9.post1
sanic-jwt==1.4.0
Sanic-Plugins-Framework==0.8.2.post1
scikit-learn==0.20.4
scipy==1.4.1
setuptools-scm==3.3.3
silpa-common==0.3
simplejson==3.17.0
six==1.13.0
sklearn-crfsuite==0.3.6
slackclient==1.3.2
smmap2==2.0.5
soundex==1.1.3
soupsieve==1.9.5
spacy==2.0.18
SQLAlchemy==1.3.12
srsly==1.0.1
sympy==1.5.1
tabulate==0.8.6
tensor2tensor==1.14.1
tensorboard==1.15.0
tensorflow==1.15.0
tensorflow-datasets==1.3.2
tensorflow-estimator==1.15.1
tensorflow-gan==2.0.0
tensorflow-hub==0.7.0
tensorflow-metadata==0.21.0
tensorflow-probability==0.7.0
termcolor==1.1.0
terminaltables==3.1.0
thinc==6.12.1
toolz==0.10.0
tqdm==4.41.1
twilio==6.35.2
Twisted==19.10.0
typing==3.7.4.1
typing-extensions==3.7.4.1
tzlocal==2.0.0
ujson==1.35
uritemplate==3.0.1
urllib3==1.25.7
wasabi==0.6.0
wcwidth==0.1.8
webexteamssdk==1.2
websocket-client==0.54.0
websockets==8.1
Werkzeug==0.16.0
wincertstore==0.2
wrapt==1.10.11
yarl==1.4.2
zipp==0.6.0
zope.interface==4.7.1