from sqlalchemy import create_engine

db_uri  = "sqlite:///db.sqlite"
engine = create_engine(db_uri)
# create table
engine.execute('CREATE TABLE "file_diagnostic" ('
            'file_diagnostic_num INTEGER NOT NULL,'
            'folder_diagnostic_num INTEGER NOT NULL,'
            'num_compte_PATIENT VARCHAR ,'
            'nom_patient VARCHAR, '
            'date_creation_file DATE,'
            'date_modification_file DATE ,'
            'num_compte_doctor INTEGER NOT NULL,'
            'hospital_num INTEGER NOT NULL,'
            'hospital_nom VARCHAR,'
            'type_hospital VARCHAR ,'
            'Adresse_hospital VARCHAR ,'
            'medicine_num INTEGER NOT NULL  ,'
            'medicine_nom VARCHAR ,'
            'prix FLOAT ,'
            'PRIMARY KEY (file_diagnostic_num));')
# insert a raw


# select *
result = engine.execute('SELECT * FROM '
                        '"file_diagnostic"')
for _r in result:
   print(_r)

# delete *
#engine.execute('DROP   TABLE "provider" ;')
result = engine.execute('SELECT * FROM "file_diagnostic"')
print(result.fetchall())