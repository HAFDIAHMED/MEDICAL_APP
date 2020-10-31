from sqlalchemy import create_engine

db_uri  = "sqlite:///db.sqlite"
engine = create_engine(db_uri)

# DBAPI - PEP249

# create table
engine.execute('CREATE TABLE "PATIENT" ('
            'num_compte_PATIENT INTEGER NOT NULL  ,'
            'nom_patient VARCHAR, '
            'prenom_patient VARCHAR,'
            'folder_num INTEGER,'
            'age_patient INTEGER,'
            'sexe_patient VARCHAR,'
            'Adresse VARCHAR,'
            'Telephone VARCHAR,'
            'email_patient VARCHAR ,'
            'password_patient VARCHAR'
            'image_patient_url VARCHAR ,'
            'PRIMARY KEY (num_compte_PATIENT));')
# insert a raw
engine.execute('INSERT INTO "PATIENT" '
        '(num_compte_PATIENT) '
        'VALUES (1)')

# select *
result = engine.execute('SELECT * FROM '
                        '"PATIENT"')
for _r in result:
   print(_r)
# delete *
#engine.execute('DROP TABLE  "PATIENT" ;')
result = engine.execute('SELECT * FROM "PATIENT"')
print(result.fetchall())