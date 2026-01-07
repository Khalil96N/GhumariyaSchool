from django.shortcuts import render
from .models import Book, Lesson, Branch, AboutPage

def home(request):
    books = Book.objects.all().order_by('-id')[:3]
    lessons = Lesson.objects.all().order_by('-id')[:3]
    branches = Branch.objects.all()
    
    # Quick hack to get video ID for youtube thumbnail if possible
    # This assumes video_url is a standard youtube link, otherwise fallback in template handles it.
    for lesson in lessons:
        if 'youtube.com' in lesson.video_url or 'youtu.be' in lesson.video_url:
            # Very basic extraction, can be improved
            try:
                if 'v=' in lesson.video_url:
                    lesson.video_id = lesson.video_url.split('v=')[1].split('&')[0]
                elif 'youtu.be/' in lesson.video_url:
                    lesson.video_id = lesson.video_url.split('youtu.be/')[1].split('?')[0]
            except:
                lesson.video_id = ''

    return render(request, 'school/index.html', {
        'books': books,
        'lessons': lessons,
        'branches': branches
    })

def about_view(request):
    about_page = AboutPage.objects.first()
    if not about_page:
        about_page = AboutPage.objects.create(
            title='عن مدرسة الغمارية لإحياء العلوم',
            message='نسعى لإحياء التراث العلمي...',
            objectives='الهدف الأول\nالهدف الثاني'
        )
    return render(request, 'school/about.html', {'about': about_page})

def books_list(request):
    books = Book.objects.all().order_by('-id')
    return render(request, 'school/books_list.html', {'books': books})

def lessons_list(request):
    lessons = Lesson.objects.all().order_by('-id')
    # Extract video IDs for thumbnails
    for lesson in lessons:
        if 'youtube.com' in lesson.video_url or 'youtu.be' in lesson.video_url:
            try:
                if 'v=' in lesson.video_url:
                    lesson.video_id = lesson.video_url.split('v=')[1].split('&')[0]
                elif 'youtu.be/' in lesson.video_url:
                    lesson.video_id = lesson.video_url.split('youtu.be/')[1].split('?')[0]
            except:
                lesson.video_id = ''
    return render(request, 'school/lessons_list.html', {'lessons': lessons})
