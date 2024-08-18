import csv
from clients_reranking.ml_models.utils import calculate_age, safe_float


def calculate_score_expobank(row, headers):
    score = 0

    data = {header: row[i] for i, header in enumerate(headers)}

    try:
        age = calculate_age(data['client_birthdate'])
        income_amount = safe_float(data['workplace_income_amount'])
        additional_income_amount = safe_float(data['workplace_additional_income_amount'])
        credit_initial = safe_float(data['credit_initial'])
        job_type = data['job_type']
        education = data['client_education']
        work_experience = int(data['workplace_work_experience'])
        children_dependents = int(data['client_children_dependents'])
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

    if credit_initial > 200000:
        score += 15
    elif credit_initial > 100000:
        score += 5

    if children_dependents > 0:
        score += 10

    if job_type in ['Найм', 'ИП', 'Самозанятый']:
        score += 10

    if education in ['Высшее', 'Высшее неоконченное']:
        score += 10

    if work_experience > 5:
        score += 10

    return score

