import os
import json
from google import genai
from google.genai import types

def generate_telco_qa_artifacts(feature_description: str) -> dict:
    client = genai.Client()
    
    prompt = f"""
    You are an expert Telco QA Automation Agent. Analyze the following feature description and return a JSON object with exactly three keys:
    1. "gherkin": Standard Gherkin/BDD syntax (.feature format) with Scenarios covering happy path and edge cases.
    2. "playwright_script": A runnable Python Playwright async test script implementing the Gherkin scenarios.
    3. "coverage_report": A Markdown report highlighting coverage gaps, boundary values, timeout/retry paths, and malformed payloads.

    Feature Description:
    {feature_description}
    
    Return ONLY valid JSON with keys: gherkin, playwright_script, coverage_report.
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            temperature=0.2
        )
    )
    
    return json.loads(response.text)
