import os
from ..connection_to_db import session, metadata, engine
import csv
from sqlalchemy import Table, insert

from pathlib import Path

# Получаем путь к текущей директории
current_dir = Path(__file__).parent
    
hackaton_client_data = Table('hackaton_client_data', metadata, autoload_with=engine)

def main():
    print(os.path.abspath(os.curdir))
    print(current_dir)
    print("=============================================================================================================\n")
    with open(str(current_dir)+'/hackaton_client_data.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            for key, value in row.items():
                if key=="client_passport_no_previous":
                    row[key] = bool(row[key])
                if value == '':
                    row[key] = None
            print(row)
            insert_stmt = hackaton_client_data.insert().values(row)
            session.execute(insert_stmt)

            
    # Подтверждение транзакций и закрытие сессии
    session.commit()
    session.close()

    