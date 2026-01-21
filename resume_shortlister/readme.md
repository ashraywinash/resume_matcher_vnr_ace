

## Contributing

Contributions are welcome. Please submit a pull request.

## License

MIT License - see LICENSE file for details.

## Support

For issues and questions, please open a GitHub issue.
## Resume Matching System

This project includes a resume ingestion and job matching system using FAISS and sentence embeddings.

### Components

1. **resume_ingester.py**: 
    - Extracts text from resumes (PDF format), splits them into chunks, generates embeddings, and stores them in a FAISS index.
    - Metadata for each chunk is stored in a pickle file for later retrieval.

2. **match_job.py**: 
    - Matches a given job description with the most relevant resumes using the FAISS index and metadata.

3. **embeddings.py**: 
    - Provides a utility function to generate sentence embeddings using the `sentence-transformers` library.

4. **main.py**: 
    - Example script to demonstrate how to use the system to match a job description with resumes and save the results.

### How to Use

1. **Ingest Resumes**:
    - Place PDF resumes in the `resumes/` folder.
    - Run `resume_ingester.py` to process and index the resumes.

2. **Match Job Descriptions**:
    - Use the `match_job` function in `match_job.py` to find the top matching resumes for a given job description.

3. **Run Example**:
    - Execute `main.py` to see the system in action.

### Requirements

- Python 3.7+
- Install dependencies using `pip install -r requirements.txt`.

### Notes

- Ensure the `resumes/` folder contains the resumes in PDF format.
- Configure paths and parameters in the `config.py` file as needed.
- Output files for matched resumes will be saved in the `output/` folder.
- This project uses the `sentence-transformers/all-MiniLM-L6-v2` model for generating embeddings.
- FAISS is used for efficient similarity search.

### Future Enhancements

- Add support for more file formats (e.g., DOCX).
- Improve the ranking algorithm for better matching accuracy.
- Add a web interface for easier interaction with the system.
- Implement additional features like feedback loops for improving results.
- Support for multi-language resumes and job descriptions.
- Integration with cloud storage for scalability.
- Add unit tests for better reliability.
- Optimize the chunking and embedding process for large-scale datasets.
- Enhance the metadata structure for more detailed resume information.
- Add logging and monitoring for production use.
- Explore other embedding models for domain-specific use cases.
- Implement a feature to anonymize sensitive information in resumes.

### Disclaimer

This project is for educational purposes only. Ensure compliance with data privacy laws when handling resumes and personal information.