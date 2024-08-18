import csv
from faker import Faker
import random

fake = Faker('ru_RU')


def generate_row():
    return [
        fake.first_name(),  # client_name
        fake.middle_name(),  # client_middle_name
        fake.last_name(),  # client_sirname
        fake.date_of_birth(minimum_age=18, maximum_age=70).strftime('%Y-%m-%d %H:%M:%S'),  # client_birthdate
        fake.city(),  # client_birthplace
        fake.phone_number(),  # client_mobile_phone
        random.choice([f'Продукт_{i}' for i in range(1, 21)]),  # product
        random.choice([f'Тариф_{i}' for i in range(1, 16)]),  # tariff
        fake.company(),  # autosalon
        random.choice(['Высшее', 'Высшее неоконченное', 'Среднее', 'Среднее неоконченное']),  # client_education
        fake.ssn()[:4],  # client_passport_series
        fake.ssn()[4:],  # client_passport_number
        fake.date_of_birth(minimum_age=10, maximum_age=70).strftime('%Y-%m-%d %H:%M:%S'),  # client_passport_issue_date
        fake.address(),  # client_passport_issue_place
        fake.ssn()[:10],  # client_passport_issue_code
        random.choice([0, 1]),  # client_passport_no_previous
        fake.ssn()[:4],  # client_zagran_passport_series
        fake.ssn()[4:],  # client_zagran_passport_number
        fake.date_of_birth(minimum_age=10, maximum_age=70).strftime('%Y-%m-%d %H:%M:%S'),
        # client_zagran_passport_issue_date
        fake.address(),  # client_zagran_passport_issue_place
        fake.ssn()[:10],  # client_zagran_passport_issue_code
        fake.ssn()[:4],  # client_driver_license_series
        fake.ssn()[4:],  # client_driver_license_number
        fake.date_of_birth(minimum_age=10, maximum_age=70).strftime('%Y-%m-%d %H:%M:%S'),
        # client_driver_license_issue_date
        fake.address(),  # client_driver_license_issue_place
        fake.ssn()[:10],  # client_driver_license_issue_code
        round(random.uniform(10000, 500000), 2),  # credit_sum
        random.randint(12, 60),  # credit_term
        round(random.uniform(1000, 50000), 2),  # credit_initial
        fake.date_of_birth(minimum_age=1, maximum_age=10).strftime('%Y-%m-%d %H:%M:%S'),  # credit_dog_issue_date
        random.choice(['Женат', 'Холост', 'Вдова/Вдовец', 'Разведен']),  # client_family_status
        random.randint(0, 5),  # client_children_dependents
        fake.address(),  # client_registration_address
        random.choice(['Собственное', 'Арендуемое']),  # client_registration_own_type
        fake.date_of_birth(minimum_age=0, maximum_age=5).strftime('%Y-%m-%d %H:%M:%S'),  # client_registration_date
        random.choice(['Найм', 'ИП', 'Самозанятый', 'Пенсионер', 'Собственное дело']),  # job_type
        fake.company(),  # workplace_name
        fake.ssn(),  # workplace_inn
        fake.job(),  # workplace_client_position
        fake.address(),  # workplace_address
        fake.phone_number(),  # workplace_phone
        fake.date_of_birth(minimum_age=1, maximum_age=10).strftime('%Y-%m-%d %H:%M:%S'),  # workplace_workdate
        random.randint(1, 30),  # workplace_work_experience
        round(random.uniform(30000, 150000), 2),  # workplace_income_amount
        round(random.uniform(0, 20000), 2),  # workplace_additional_income_amount
        random.choice(['Пенсия', 'Пособие', 'Алименты', 'Доход от ценных бумаг/депозитов', 'Аренда', 'Noone']),
        # workplace_additional_income_type
        random.choice([f'Бренд_{i}' for i in range(1, 21)]),  # car_brand
        random.choice([f'Модель_{i}' for i in range(1, 21)]),  # car_model
        str(random.randint(2000, 2024)),  # car_year
        round(random.uniform(500000, 3000000), 2),  # car_price
        round(random.uniform(0, 200000), 2),  # car_dop_price
        random.choice(['Седан', 'Купе', 'Внедорожник', 'Кабриолет', 'Пикапы', 'Родстер', 'None']),  # car_type
        random.choice(['Новый', 'Подержанный', 'None']),  # car_condition
        random.choice(['МТ', 'АТ', 'None']),  # car_transmission
        str(random.randint(0, 300000))  # car_mileage
    ]


with open('hackaton_client_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([
        'client_name', 'client_middle_name', 'client_sirname', 'client_birthdate',
        'client_birthplace', 'client_mobile_phone', 'product', 'tariff', 'autosalon',
        'client_education', 'client_passport_series', 'client_passport_number',
        'client_passport_issue_date', 'client_passport_issue_place', 'client_passport_issue_code',
        'client_passport_no_previous', 'client_zagran_passport_series', 'client_zagran_passport_number',
        'client_zagran_passport_issue_date', 'client_zagran_passport_issue_place', 'client_zagran_passport_issue_code',
        'client_driver_license_series', 'client_driver_license_number', 'client_driver_license_issue_date',
        'client_driver_license_issue_place', 'client_driver_license_issue_code', 'credit_sum',
        'credit_term', 'credit_initial', 'credit_dog_issue_date', 'client_family_status',
        'client_children_dependents', 'client_registration_address', 'client_registration_own_type',
        'client_registration_date', 'job_type', 'workplace_name', 'workplace_inn',
        'workplace_client_position', 'workplace_address', 'workplace_phone', 'workplace_workdate',
        'workplace_work_experience', 'workplace_income_amount', 'workplace_additional_income_amount',
        'workplace_additional_income_type', 'car_brand', 'car_model', 'car_year', 'car_price',
        'car_dop_price', 'car_type', 'car_condition', 'car_transmission', 'car_mileage'
    ])
    for _ in range(10000):
        writer.writerow(generate_row())
