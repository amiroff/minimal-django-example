from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    TEMPLATES=[
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": ["templates"],
        },
    ],
)


def index_view(request):
    return HttpResponse("<h1>Hello World From Django!</h1>")


def hello_view(request, name):
    return render(request, "template.html", {"name": name, "request": request})


urlpatterns = [
    path("", index_view),
    path("hello/<name>", hello_view),
]

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line()
