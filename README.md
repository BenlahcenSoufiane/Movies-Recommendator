# WatchHub - Movie Recommendation Platform



WatchHub is an online platform specialized in movie recommendations, aiming to simplify users' cinematic experience by providing personalized suggestions. This platform consists of three main interfaces, each designed to offer a smooth and intuitive user experience.
### Website Working Flow

## 📸 Screenshots

![Alt Text](static/12.png)


## Technologies Used
### BeautifulSoup
BeautifulSoup is a Python library used for extracting data from HTML and XML files. It provides tools for navigating and searching the parse tree, making it easy to extract information from web sources.

### Requests
Requests is a popular Python library for making HTTP requests. It simplifies the process of sending HTTP requests and handling responses, essential for interacting with external web services.

### Flask
Flask is a lightweight Python web framework, ideal for building web applications. It offers a simple and modular approach to creating web services and APIs, crucial for setting up WatchHub's backend infrastructure.

### Pandas
Pandas is a powerful Python library for data manipulation and analysis. It offers data structures such as DataFrame, facilitating efficient manipulation of structured data, a crucial component for processing movie information.

### Scikit-learn (TfidfVectorizer)
Scikit-learn is a Python machine learning library. TfidfVectorizer, a component of Scikit-learn, is used to convert a collection of raw documents into a TF-IDF feature matrix, improving the quality of recommendations.

### Scikit-learn (cosine_similarity)
Another feature of Scikit-learn, cosine_similarity, is used to calculate the cosine similarity between vectors. This function is often employed in natural language processing and information retrieval, contributing to the effectiveness of movie recommendations.

### TMDB API
The Movie Database (TMDB) API is a web service providing access to a vast database of information about movies and TV shows. This API allows the integration of up-to-date movie data into WatchHub, ensuring the relevance of recommendations.

### How to Use WatchHub
Clone this repository to your local machine.
Ensure you have the required dependencies installed. You can install them using pip install -r requirements.txt.
Run the application using the command python app.py.
Access the WatchHub web interface at the address provided in the console.
Enjoy personalized recommendations based on genre and other cinematic features.
### Disclaimer
Please note that the use of the TMDB API may be subject to specific limitations and terms of use. Make sure to comply with TMDB's terms of service when integrating data from their API.

Feel free to contribute by proposing improvements or reporting issues. Thank you for using WatchHub!

Thanks for @emaneJalal for the collaboration and contibuting in this project 
Made with LOVE
