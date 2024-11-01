# Wiki Encyclopedia Project

This project is part of the CS50 Web course and aims to build a Wikipedia-like online encyclopedia using Django. Bootstrap was used for minimalistic styling; the main goal was to implement the backend. The encyclopedia allows users to view, search, create, edit, and browse random encyclopedia entries written in Markdown.

## Features

1. **Entry Pages**:
   - Users can view encyclopedia entries by visiting `/wiki/TITLE`, where `TITLE` is the name of the entry.
   - Entries are stored in Markdown and converted to HTML for display.
   - If an entry doesn't exist, the user sees a "Page Not Found" message.

2. **Index Page**:
   - The homepage lists all encyclopedia entries.
   - Users can click on an entry to view its content.

3. **Search**:
   - Users can search for entries using a search bar.
   - If the query matches an entry, the user is redirected to that page.
   - If no exact match is found, a search results page lists partial matches.

4. **Create New Entry**:
   - Users can create a new encyclopedia entry using a form.
   - If an entry with the provided title already exists, an error is shown.

5. **Edit Entry**:
   - Users can edit existing encyclopedia entries, but not the title itself.
   - The edit form is pre-populated with the current content, and users can save their changes.

6. **Random Page**:
   - Users can click a button to visit a random encyclopedia entry.

7. **Markdown Support**:
   - All entries are written in Markdown and converted to HTML before being displayed.


To set up and run the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/aegis945/project-1-wiki.git
   cd project-1-wiki
2. Create a Virtual Environment
   ```bash
   python -m venv venv```
3. Activate the Virtual Environment:
   On macOS/Linux:
   ```bash
   source venv/bin/activate```
  On Windows: 
   ```bash
   venv\Scripts\activate
  ```
4. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```
5. **Set Up Environment Variables: Create a .env file in the project root directory and define your environment variables**:
```bash
SECRET_KEY=your_secret_key
DEBUG=True
```

6. Run dev server
   ```bash
   python manage.py runserver
   ```
7. Open your web browser and go to http://127.0.0.1:8000
