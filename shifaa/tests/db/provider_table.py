from sqlalchemy import create_engine

db_uri  = "sqlite:///db.sqlite"
engine = create_engine(db_uri)
# create table
engine.execute('CREATE TABLE "provider" ('
            'provider_num INTEGER NOT NULL  ,'
            'provider_nom VARCHAR,'
            'Adresse_provider VARCHAR ,'
            'email_provider VARCHAR ,'
            'password_provider VARCHAR  ,'

            'PRIMARY KEY (provider_num));')
# insert a raw
engine.execute('INSERT INTO "provider" '
        '(provider_num,provider_nom,email_provider,Adresse_provider,password_provider)'
        'VALUES (1,"provider_rabat","provider@rabat.com","RABAT AGDAL RUE 4 , QUARTIER 5 ","password")')

# select *
result = engine.execute('SELECT * FROM '
                        '"hospital"')
for _r in result:
   print(_r)

# delete *
#engine.execute('DROP   TABLE "provider" ;')
result = engine.execute('SELECT * FROM "hospital"')
print(result.fetchall())