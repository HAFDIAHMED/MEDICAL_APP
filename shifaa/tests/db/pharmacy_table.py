from sqlalchemy import create_engine

db_uri  = "sqlite:///db.sqlite"
engine = create_engine(db_uri)
# create table
engine.execute('CREATE TABLE "pharmacy" ('
            'pharmacy_num INTEGER NOT NULL,'
            'pharmacy_nom VARCHAR ,'
            'Adresse_pharmacy VARCHAR ,'
            'Authorisation_num VARCHAR ,'
            'provider_num INTEGER NOT NULL  ,'
            'provider_nom  VARCHAR,'
            'PRIMARY KEY (pharmacy_num));')
# insert a raw


# select *
result = engine.execute('SELECT * FROM '
                        '"pharmacy"')
for _r in result:
   print(_r)

# delete *
#engine.execute('DROP   TABLE "provider" ;')
result = engine.execute('SELECT * FROM "pharmacy"')
print(result.fetchall())