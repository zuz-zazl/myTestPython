import sqlalchemy as db;
import requests;
import re;

url = 'https://api.github.com/users';
res = requests.get(url);
loginUser = res.json();

engine = db.create_engine('sqlite:///users_hub.db');
conection = engine.connect();

metadata = db.MetaData();

login_hub = db.Table('users', metadata, 
    db.Column('login_id', db.Integer),                    
    db.Column('login', db.Text),                    
);

metadata.create_all(engine);

for logins in loginUser:
    if re.findall('z', logins['login']).count('z') == 3:
        login = logins['login'];
        inserttion_query = login_hub.insert().values({'login': login});
        conection.execute(inserttion_query);


