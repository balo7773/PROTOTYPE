# Final Portfolio Project: Django Web Application

## Project Overview
This Django web application is the final portfolio project developed by Balogun A.D. and Orngu E.O. as part of our academic journey. It is a culmination of everything we've learned and showcases our ability to design and implement robust, scalable, and feature-rich web solutions.

## Project Features
1. **Dynamic News Display**:
   - Fetches and displays news data (links, authors, and publication dates) dynamically from external sources.
   - News data is not stored in the database to optimize space usage, but caching is implemented for faster load times.
   - Pagination is supported for easy navigation of large datasets.

2. **Stock Profile**:
   - The application displays listed companies in the stock market and crypto which shows
   detailed information about them.

3. **Image Integration**:
   - Uses the Pillow library to include logos and images of news companies for a visually appealing interface.

4. **User-Centric Design**:
   - A clean and intuitive UI/UX, with the 'Sign Up' heading prominently centered and in bold to guide new users.

5. **Django Backend**:
   - Built on Django, leveraging its powerful ORM, templating system, and scalability to handle dynamic content.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django, urllib3, request, bs4
- **Database**: SQLite
- **Libraries**: Pillow for image processing


## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-url
   ```

2. Navigate to the project directory:
   ```bash
   cd project-directory
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application in your browser:
   ```
   http://127.0.0.1:8000
   ```

## How to Use
1. Navigate to the homepage to view the latest news.
2. Use pagination controls to browse through the news items.
3. Click on a news item to get detailed insights and AI-powered explanations.
4. Sign up or log in to access additional features (if applicable).

## Challenges Overcome
- Efficiently handling dynamic data without persistent storage.
- Implementing caching mechanisms to optimize load times.
- Integrating AI capabilities for content summarization and explanation.
- Designing a user-friendly and responsive interface.

## Future Improvements
- Explore database integration for optional persistent storage.
- Enhance AI capabilities to provide deeper insights.
- Add more news sources and customization options for users.
- Optimize caching strategies for better performance.

## Acknowledgements
We extend our gratitude to our mentors, classmates, and everyone who supported us throughout this project. Your guidance and feedback have been invaluable.

---
Developed by: **Balogun A.D. & Orngu E.O.**  
Date: Wednesday 22nd January, 2025

Feel free to reach out to us for collaborations or inquiries!
