from sqlalchemy import create_engine

db_uri  = "sqlite:///db.sqlite"
engine = create_engine(db_uri)
# create table
engine.execute('CREATE TABLE "folder_diagnostic" ('
            'folder_diagnostic_num INTEGER NOT NULL,'
            'num_compte_PATIENT VARCHAR ,'
            'nom_patient VARCHAR, '
            'date_creation DATE,'
            'date_modification DATE ,'
            'files_number INT ,'

            'PRIMARY KEY (folder_diagnostic_num));')
# insert a raw


# select *
result = engine.execute('SELECT * FROM '
                        '"folder_diagnostic"')
for _r in result:
   print(_r)

# delete *
#engine.execute('DROP   TABLE "provider" ;')
result = engine.execute('SELECT * FROM "folder_diagnostic"')
print(result.fetchall())