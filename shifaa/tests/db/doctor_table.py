from sqlalchemy import create_engine

db_uri  = "sqlite:///db.sqlite"
engine = create_engine(db_uri)

# create table
engine.execute('CREATE TABLE "doctor" ('
            'num_compte_doctor INTEGER NOT NULL  ,'
            'nom_doctor VARCHAR ,'
            'prenom_doctor VARCHAR ,'
            'email_doctor VARCHAR,'
            'password_doctor VARCHAR '
            'hospital_type VARCHAR,'
            'hospital_num VARCHAR ,'
            'PRIMARY KEY (num_compte_doctor));')
# insert a raw
engine.execute('INSERT INTO "doctor" '
        '(num_compte_doctor,nom_doctor,prenom_doctor,email_doctor,password_doctor)'
        'VALUES (1,"PRENOMDOC","NOMDOC","doc@doc.com","passworddoc")')

# select *
result = engine.execute('SELECT * FROM '
                        '"doctor"')
for _r in result:
   print(_r)
# delete *
#engine.execute('DROP   TABLE "doctor" ;')
result = engine.execute('SELECT * FROM "doctor"')
print(result.fetchall())