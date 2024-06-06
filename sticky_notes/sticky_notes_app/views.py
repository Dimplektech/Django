from django.shortcuts import render, get_object_or_404, redirect
from .models import Notes
from .forms import NoteForm


# View function to display the list of notes.
def note_list(request):
    #  Retrieve all notes from the database.
    notes = Notes.objects.all()
    # Render the 'view_notes.html' template with retrived notes.
    return render(request, 'view_notes.html', {'notes': notes})


# View function to display the deatials of specific note.
def note_details(request, id):
    # Retrieve the note with the given ID from the database,
    # or return a 404 error if not found.
    note = get_object_or_404(Notes, id=id)
    # Render the 'note_details.html' template with retrieved note.
    return render(request, 'note_details.html', {'note': note})


# Function to create new note.
def note_new(request):
    if request.method == "POST":
        form = NoteForm(request.POST)  # Bind form with POST data.
        if form.is_valid():
            note = form.save(commit=False)  # Create a new Note instance,
            # but don't save yet.
            note.save()  # Save new Note instance to the database.
            return redirect('note_detail', id=note.id)  # Redirect to the
            # detail view of the new note.
    else:
        form = NoteForm()  # Create an empty form.
        # Render the form in the template.
    return render(request, 'note_edit.html',
                  {'form': form, 'heading': 'Add New Note'})


# View function to edit note.
def note_edit(request, id):
    note = get_object_or_404(Notes, id=id)  # Retrieve the existing Note
    # instance.
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)  # Bind form with POST
        # data and existing Note instance.
        if form.is_valid():
            note = form.save(commit=False)  # Update the Note instance but
            # don't save it.
            note.save()  # Save the changes to the Note instance.
            return redirect('note_detail', id=note.id)
    else:
        form = NoteForm(instance=note)
    return render(request, 'note_edit.html',
                  {'form': form, 'heading': 'Edit Note'})


# View function to delete specific note.
def note_delete(request, id):
    # Retrieve the note with given ID from the database,
    # or return 404 erroe if not found.
    note = get_object_or_404(Notes, id=id)
    # Delete the retrieved note from database.
    note.delete()
    # Redirect to the note list view after the note has been deleted.
    return redirect('note_list')
