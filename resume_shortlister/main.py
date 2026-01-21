from match_job import match_job

if __name__ == "__main__":

    company_id = "google_ai_engineer"

    job_description = """
At Google, AI engineers work at the intersection of research and product to build intelligent systems that impact billions of users. You’ll collaborate with researchers, software engineers, product managers, and UX teams to bring state-of-the-art machine learning models into real-world applications.

As an AI Engineer, you will design, develop, and deploy ML models that power products across Search, Ads, YouTube, Google Cloud, and emerging AI initiatives.

Responsibilities

Design, train, evaluate, and deploy machine learning and deep learning models

Work with large-scale data pipelines to improve model performance and reliability

Translate research ideas into production-ready systems

Optimize models for efficiency, scalability, and robustness

Collaborate cross-functionally to define AI-driven product features

Stay current with advances in AI and apply them to Google products

Technologies you’ll use

Python, C++, or Java

TensorFlow, JAX, PyTorch

Distributed training and inference systems

Data processing tools (e.g., Apache Beam, BigQuery)
    """

    top_matches = match_job(job_description, top_k=5)

    
    for resume_id, chunks in top_matches:
        print(f"Resume ID: {resume_id}")
        with open(f"output/{company_id}.txt", "a") as f:
            f.write(str(f"Resume ID: {resume_id}\n"))
            for chunk in chunks:
                f.write(str(f"Score: {chunk['score']}\n"))
                f.write(str(f"Text: {chunk['text']}\n\n"))
