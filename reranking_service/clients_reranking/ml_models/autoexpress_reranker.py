import csv
from clients_reranking.ml_models.utils import calculate_age, safe_float
from .rank_clients import rank_clients

# ЦА: граждане,заинтересованные в каких-либо финансовых действиях с автомобилем
def calculate_score_autoexpress(row, headers):
    score = 0

    data = {header: row[i] for i, header in enumerate(headers)}

    try:
        age = calculate_age(data['client_birthdate'])
        credit_sum = safe_float(data['credit_sum'])
        credit_initial = safe_float(data['credit_initial'])
        car_price = safe_float(data['car_price'])
        income_amount = safe_float(data['workplace_income_amount'])
        additional_income_amount = safe_float(data['workplace_additional_income_amount'])
        job_type = data['job_type']
        car_condition = data['car_condition']
        car_mileage = int(data['car_mileage'])
        work_experience = int(data['workplace_work_experience'])
        children_dependents = int(data['client_children_dependents'])
    except (KeyError, ValueError) as e:
        print(f"Error processing row {row}: {e}")
        return 0

    if 25 <= age <= 55:
        score += 20

    if credit_sum > 500000:
        score += 15

    if credit_initial > 100000:
        score += 15

    if car_price > 2000000:
        score += 20

    if car_condition == 'Новый':
        score += 15
    elif car_condition == 'Подержанный' and car_mileage < 50000:
        score += 10

    if income_amount > 200000:
        score += 20
    elif income_amount > 100000:
        score += 10

    if additional_income_amount > 50000:
        score += 10

    if children_dependents > 0:
        score += 10

    if job_type in ['Найм', 'ИП', 'Самозанятый']:
        score += 10

    if work_experience > 5:
        score += 10

    return score
