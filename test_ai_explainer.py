from explain_prediction import explain_prediction

label = "PVC"  # Try also with: "NSR", "PAC", etc.
explanation = explain_prediction(label)

print(f"🫀 Explanation for {label}:\n{explanation}")
