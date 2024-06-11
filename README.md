# Sticky Notes Apllication
In this README file:
- **Project Overview** gives a brief introduction to the project.
- **Features** lists the key functionalities of the project.
- **Installation** provides step-by-step instructions to set up the project locally.
- **Usage** explains how to access and use the application.
- **Models** and **Views** sections give details about the database models and the main views in the application.
- **Credits** 

<h2>Project Overview</h2>
Sticky Note Application is Web application designed using django, Pthon and SQLite to help user to create Notes efficiently. It allows users to create, update, delete, and view Notes. This application is important for learning fundamental DJango, CRUD (Create, Read, Update, Delete) and creating Database in SQlite. It also allows user to nevigate to one page to another page for view and edit notes.

<h2> Features</h2>
<h4>Create New Sticky Notes with title and body:</h4> Add a new Note with a title and Content.
<h4>View a List of Notes: </h4>See a list of all Notes.
<h4>View Note:</h4> View details of perticular note.
<h4>Edit existing Notes:</h4> Edit the details of an existing Note.
<h4>Delete Note:</h4>Delete a Note from the list.

## Installation
1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/sticky-notes-app.git
    cd sticky-notes-app
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```sh
    python manage.py migrate
    ```

5. **Run the development server:**
    ```sh
    python manage.py runserver
    ```


<h3>Usage></h3>
1. To verify the Sticky_notes project, make sure your virtual environment is activated, then start Django's development server using the command
<h5>python manage.py runserver</h5>. The server runs on the default port 8000, and you see output like the following output in the terminal window
    (django_venv) PS C:\Users\Simran\OneDrive\Desktop\Python_bootcamp\Task24_Django> cd sticky_notes
    (django_venv) PS C:\Users\Simran\OneDrive\Desktop\Python_bootcamp\Task24_Django\sticky_notes> py manage.py runserver
    Watching for file changes with StatReloader
    Performing system checks...
    
    System check identified no issues (0 silenced).
    June 07, 2024 - 09:03:57
    Django version 5.0.6, using settings 'sticky_notes.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.

2. CTRL + click  http://127.0.0.1:8000/ and page will be open on the browser and ayou will be navigate to Main screen. On Main Screen You can see list of all Notes.
   There is button to Add button to add new Notes.
   TO edit Notes you need to click on perticular note.
   ![image](https://github.com/Dimplektech/Django/assets/163059141/e04d9981-9e7c-4648-8ee6-a47bd3eef419)
   
3. To add new Note ,Click on Add button,it will nevigate you to another page to add note.
 ![image](https://github.com/Dimplektech/Django/assets/163059141/c9a46e7e-b32f-4311-a5db-7595f119fa43)
   

4. Edit Note : Click on one of the note,it will take you to detail page where you can see details of perticular note and u can click edit.
   ![image](https://github.com/Dimplektech/Django/assets/163059141/3f68f658-3b6d-4272-87f0-0645b9e5f881)
   

5.This page to Edit Perticulat Note.Once u save it will take you to detail page of that note.
   ![image](https://github.com/Dimplektech/Django/assets/163059141/45d45fbe-bbb3-4b8f-bf4c-3e54dc314278)

6. Delete button will delete peticular note and navigate you to Home Page.   

7. Back to notes button will take you to home page where you can see list of notes.

## Model
### Notes
- `title`: The title of the note.
- `content`: The content of the note.
- `post`: Foreign key relationship to the `Post` model.
- `created_at`: Timestamp when the note was created.
- `updated_at`: Timestamp when the note was last updated.
- 
## Views 
### Notes Views
- `note_list`: Displays a list of all notes associated with a specific post.
- `note_detail`: Displays details of a specific note.
- `note_new`: Form to create a new note.
- `note_edit`: Form to edit an existing note.
- `note_delete`: Deletes a specified note.

 
    
<h2>Credits</h2>
<h3> Author: Dimpal Kaware </h3>
<h3>Repository: https://github.com/Dimplektech</h3>
