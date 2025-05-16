JOB_DESC = """
We are hiring a Software Engineer with the following:
- Strong Python skills
- Experience with APIs and backend frameworks (Flask, Django)
- Familiarity with cloud platforms (GCP, AWS)
- Bonus: experience in ML/AI
"""

def screening_prompt(resume_text):
    return f"""
You are an HR assistant. Based on the following job description:
{JOB_DESC}

Screen the following resume. Output:
- Candidate Fit Score (0-100)
- Skills Matched
- Final Verdict (Shortlist/Reject)
Resume:
{resume_text}
"""

def sentiment_prompt(feedback_text):
    return f"""
Analyze the following employee feedback:
{feedback_text}

Output:
- Overall Sentiment (Positive/Negative/Neutral)
- Key themes or concerns
- Attrition Risk (Low/Medium/High)
"""
