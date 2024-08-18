import csv
from clients_reranking.ml_models.utils import calculate_age, safe_float


# ЦА: граждане, заинтересованные в покупке автомобиля
def calculate_score_expocar(row, headers):
    score = 0

    data = {header: row[i] for i, header in enumerate(headers)}

    try:
        age = calculate_age(data['client_birthdate'])
        income_amount = safe_float(data['workplace_income_amount'])
        additional_income_amount = safe_float(data['workplace_additional_income_amount'])
        credit_sum = safe_float(data['credit_sum'])
        credit_initial = safe_float(data['credit_initial'])
        car_price = safe_float(data['car_price'])
        car_condition = data['car_condition']
        car_mileage = int(data['car_mileage'])
        family_status = data['client_family_status']
        job_type = data['job_type']
    except (KeyError, ValueError) as e:
        print(f"Error processing row {row}: {e}")
        return 0

    if 25 <= age <= 55:
        score += 20

    if income_amount > 200000:
        score += 20
    elif income_amount > 100000:
        score += 10

    if additional_income_amount > 50000:
        score += 10

    if credit_sum < 100000:
        score += 15

    if credit_initial > 100000:
        score += 15

    if car_condition == 'None':
        score += 20
    elif car_condition == 'Подержанный' and car_mileage > 50000:
        score += 5

    if family_status in ['Женат']:
        score += 10

    if job_type in ['Найм', 'ИП', 'Самозанятый']:
        score += 10

    return score


