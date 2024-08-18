import csv
from clients_reranking.ml_models.utils import calculate_age, safe_float


# ЦА: семьи с детьми, пары, компании друзей и любители активного отдыха
def calculate_score_park_hotel(row, headers):
    score = 0

    data = {header: row[i] for i, header in enumerate(headers)}

    try:
        age = calculate_age(data['client_birthdate'])
        income_amount = safe_float(data['workplace_income_amount'])
        additional_income_amount = safe_float(data['workplace_additional_income_amount'])
        family_status = data['client_family_status']
        job_type = data['job_type']
        work_experience = int(data['workplace_work_experience'])
        children_dependents = int(data['client_children_dependents'])
    except (KeyError, ValueError) as e:
        print(f"Error processing row {row}: {e}")
        return 0

    if 20 <= age <= 50:
        score += 20

    if income_amount > 200000:
        score += 20
    elif income_amount > 100000:
        score += 10

    if additional_income_amount > 50000:
        score += 10

    if family_status in ['Женат']:
        score += 10

    if children_dependents > 0:
        score += 20

    if job_type in ['Найм', 'ИП', 'Самозанятый']:
        score += 10

    if work_experience > 5:
        score += 10

    city = data['client_birthplace']
    major_cities = ['Москва', 'Петербург']
    if any(mc in city for mc in major_cities):
        score += 10

    return score


