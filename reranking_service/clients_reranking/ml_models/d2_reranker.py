import csv
from clients_reranking.ml_models.utils import calculate_age, safe_float


# ЦА: граждане, заинтересованные в страховке
def calculate_score_d2(row, headers):
    score = 0

    data = {header: row[i] for i, header in enumerate(headers)}

    try:
        age = calculate_age(data['client_birthdate'])
        credit_sum = safe_float(data['credit_sum'])
        car_price = safe_float(data['car_price'])
        income_amount = safe_float(data['workplace_income_amount'])
        additional_income_amount = safe_float(data['workplace_additional_income_amount'])
        family_status = data['client_family_status']
        job_type = data['job_type']
        car_condition = data['car_condition']
        car_mileage = int(data['car_mileage'])
        work_experience = int(data['workplace_work_experience'])
    except (KeyError, ValueError) as e:
        print(f"Error processing row {row}: {e}")
        return 0

    if 30 <= age <= 50:
        score += 15
    elif age > 50:
        score += 10

    if credit_sum > 100000:
        score += 5

    no_previous_passports = int(data['client_passport_no_previous'])
    if no_previous_passports == 0:
        score += 10

    if car_condition == 'Новый':
        score += 20
    elif car_price > 5000000:
        score += 15

    if income_amount > 500000:
        score += 25
    elif income_amount > 200000:
        score += 15
    elif income_amount > 100000:
        score += 10

    if additional_income_amount > 50000:
        score += 10

    if family_status in ['Женат', ]:
        score += 15

    if job_type in ['ИП', 'Самозанятый']:
        score += 10

    if car_mileage < 30000:
        score += 10

    if work_experience > 5:
        score += 10

    city = data['client_birthplace']
    major_cities = ['Москва', 'Петербург']
    if any(mc in city for mc in major_cities):
        score += 15

    return score



