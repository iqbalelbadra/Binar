# API Text Cleansing

This project is an API for text cleansing, specifically targeting abusive and alay (informal) words in Indonesian language. The API allows users to input text and receive the cleaned version of the text, where abusive words are filtered out and alay words are replaced with their standard counterparts.

## Technologies Used

- Python: Programming language used as the primary technology for the API.
- Flask: Web framework used for building the API endpoints.
- Swagger: Used for API documentation and interactive UI (Swagger UI).
- Pandas: Library used for data manipulation and processing.
- SQLite: Database used for storing and retrieving the cleaned texts.
- Matplotlib: Library used for generating visualizations.

## API Endpoints

- `POST /input-processing`: Endpoint for processing a single text input. Users can send a text and receive the cleaned version of the text as a response.

- `POST /file-processing`: Endpoint for processing a CSV file containing text data. Users can upload a CSV file and have the text in the file processed, where abusive and alay words are cleansed. The cleaned texts are stored in a SQLite database.

- `POST /read-index-data`: Endpoint for retrieving the cleaned text based on its index in the database. Users can provide an index and receive the corresponding cleaned text as a response.

## Setup and Usage

1. Install the required dependencies by running `pip install -r requirements.txt` in your terminal.
2. Start the API server by running `python app.py` in your terminal.
3. Access the API documentation and Swagger UI by visiting `http://127.0.0.1:5000/docs` in your web browser.

## Contributing

Contributions to this project are welcome. If you would like to contribute, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).