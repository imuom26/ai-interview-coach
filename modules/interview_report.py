def print_report(
    duration,
    eye_contact,
    attention_score,
    filler_total,
    communication_score
):
    overall_score = round(
        (attention_score + communication_score) / 2
    )

    print("\n" + "=" * 35)
    print("      AI INTERVIEW REPORT")
    print("=" * 35)

    print(f"Duration: {duration}")
    print(f"Eye Contact: {eye_contact:.0f}%")
    print(f"Attention Score: {attention_score}%")
    print(f"Filler Words: {filler_total}")
    print(f"Communication Score: {communication_score}%")
    print(f"Overall Score: {overall_score}%")

    print("\nFeedback:")

    if eye_contact >= 80:
        print("✓ Good eye contact")
    else:
        print("⚠ Improve eye contact")

    if attention_score >= 80:
        print("✓ Good attention")
    else:
        print("⚠ Stay focused on the interviewer")

    if filler_total <= 2:
        print("✓ Good communication")
    else:
        print("⚠ Reduce filler words")

    print("=" * 35)