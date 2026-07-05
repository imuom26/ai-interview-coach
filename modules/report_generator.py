def generate_report(
    duration,
    eye_contact,
    attention_score,
    filler_total,
    communication_score,
    overall_score
):
    report = f"""
AI INTERVIEW REPORT
====================

Duration: {duration}
Eye Contact: {eye_contact}%
Attention Score: {attention_score}%
Filler Words: {filler_total}
Communication Score: {communication_score}%
Overall Score: {overall_score}%

Feedback:
- Good eye contact
- Good communication
- Reduce filler words
"""

    return report