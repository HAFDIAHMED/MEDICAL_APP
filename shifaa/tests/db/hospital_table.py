from sqlalchemy import create_engine

db_uri  = "sqlite:///db.sqlite"
engine = create_engine(db_uri)

# create table
engine.execute('CREATE TABLE "hospital" ('
            'hospital_num INTEGER NOT NULL  ,'
            'hospital_nom VARCHAR,'
            'type_hospital VARCHAR ,'
            'Adresse_hospital VARCHAR ,'

            'PRIMARY KEY (hospital_num));')
# insert a raw
engine.execute('INSERT INTO "hospital" '
        '(hospital_num,hospital_nom,type_hospital,Adresse_hospital)'
        'VALUES (1,"NOMHOSPITAL","CLINIQUE","RABAT AGDAL RUE 1 , QUARTIER 3 ")')

# select *
result = engine.execute('SELECT * FROM '
                        '"hospital"')
for _r in result:
   print(_r)
# delete *
#engine.execute('DROP   TABLE "hospital" ;')
result = engine.execute('SELECT * FROM "hospital"')
print(result.fetchall())