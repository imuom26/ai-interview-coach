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