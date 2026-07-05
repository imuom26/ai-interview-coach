def calculate_attention_score(
    eye_contact_percent,
    look_away_count
):
    score = eye_contact_percent

    penalty = look_away_count * 5

    score = score - penalty

    if score < 0:
        score = 0

    return round(score)

def calculate_communication_score(
    filler_count
):
    score = 100 - (filler_count * 5)

    if score < 0:
        score = 0

    return score

def calculate_overall_score(
    attention_score,
    communication_score
):
    return round(
        (attention_score + communication_score) / 2
    )