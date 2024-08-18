import csv
from clients_reranking.ml_models.utils import calculate_age, safe_float


# ЦА: люди, желающиеприобрести автомобиль, но не имеющие возможностиоплатить его полную стоимостьсразу
def calculate_score_leasing(row, headers):
    score = 0

    data = {header: row[i] for i, header in enumerate(headers)}

    try:
        age = calculate_age(data['client_birthdate'])
        credit_sum = safe_float(data['credit_sum'])
        credit_initial = safe_float(data['credit_initial'])
        income_amount = safe_float(data['workplace_income_amount'])
        additional_income_amount = safe_float(data['workplace_additional_income_amount'])
        family_status = data['client_family_status']
        job_type = data['job_type']
        car_condition = data['car_condition']
        work_experience = int(data['workplace_work_experience'])
    except (KeyError, ValueError) as e:
        print(f"Error processing row {row}: {e}")
        return 0

    if 25 <= age <= 45:
        score += 20
    elif 45 < age <= 55:
        score += 10

    if credit_sum > 500000:
        score += 15

    if credit_initial > 100000:
        score += 15

    if car_condition == 'None':
        score += 20

    if income_amount > 100000:
        score += 20
    elif income_amount > 50000:
        score += 10

    if additional_income_amount > 20000:
        score += 10

    if family_status in ['Женат']:
        score += 10

    if job_type in ['Найм', 'ИП', 'Самозанятый']:
        score += 10

    if work_experience > 5:
        score += 10

    return score

