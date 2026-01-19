from match_job import match_job

if __name__ == "__main__":

    company_id = "company_123"

    job_description = """
    We are looking for a skilled software engineer with experience in Python and machine learning.
    The candidate should be proficient in building scalable applications and have a strong understanding
    of data structures and algorithms. Experience with cloud platforms like AWS or GCP is a plus.
    """

    top_matches = match_job(job_description, top_k=5)

    
    for resume_id, chunks in top_matches:
        print(f"Resume ID: {resume_id}")
        with open(f"output/{company_id}.txt", "a") as f:
            f.write(str(f"Resume ID: {resume_id}\n"))
            for chunk in chunks:
                f.write(str(f"Score: {chunk['score']}\n"))
                f.write(str(f"Text: {chunk['text']}\n\n"))
