from sqlalchemy import create_engine

db_uri  = "sqlite:///db.sqlite"
engine = create_engine(db_uri)
# create table
engine.execute('CREATE TABLE "medicine" ('
            'medicine_num INTEGER NOT NULL  ,'
            'medicine_nom VARCHAR ,'
            'categorie_medicine VARCHAR,'
            'Designation_medicine VARCHAR ,'
            'preparation_medicine VARCHAR ,'
            'prix FLOAT ,'

            'PRIMARY KEY (medicine_num));')
# insert a raw
engine.execute('INSERT INTO "medicine" '
        '(medicine_num,medicine_nom,categorie_medicine,Designation_medicine,preparation_medicine,prix)'
        'VALUES (1,"DOLIPRANE","HEADACHE","designation","ingrediants",10.0)')

# select *
result = engine.execute('SELECT * FROM '
                        '"medicine"')
for _r in result:
   print(_r)

# delete *
#engine.execute('DROP   TABLE "provider" ;')
result = engine.execute('SELECT * FROM "medicine"')
print(result.fetchall())