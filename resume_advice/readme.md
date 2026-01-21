# Resume Advice

A Python application for automated resume analysis, feedback, and ATS (Applicant Tracking System) optimization using LLMs (Google Gemini).

## Features

- Extracts text from PDF, DOCX, and TXT resumes
- Normalizes and cleans resume formatting
- Analyzes resumes for a target role and experience level
- Provides:
    - Overall score
    - Summary feedback
    - Section-specific issues, suggestions, and rewrite examples
    - ATS compatibility issues
    - Priority fixes

## How It Works

1. **Extract**: Reads resume files and extracts raw text.
2. **Normalize**: Cleans and standardizes the extracted text.
3. **Analyze**: Uses Google Gemini LLM to review the resume and generate structured feedback.

## Usage

1. **Install dependencies**:
        ```bash
        pip install -r requirements.txt
        ```

2. **Set up your Gemini API key**:
        - Create a `.env` file with:
            ```
            GEMINI_API_KEY=your_api_key_here
            ```

3. **Run the analysis**:
        ```bash
        python main.py
        ```

        By default, it analyzes `resumes/22071A05B4.pdf`. Change the path in `main.py` as needed.

## Project Structure

```
resume_advice/
├── main.py
├── schema.py
├── llm/
│   └── gemini_client.py
├── resume/
│   ├── analyser.py
│   ├── extractor.py
│   └── normaliser.py
└── resumes/
        └── <your_resume_files>
```

## Extending

- Add new feedback sections in `schema.py` and update prompts in `analyser.py`.
- Support more file formats by extending `extractor.py`.

## License

MIT License