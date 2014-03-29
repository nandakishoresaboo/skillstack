import json

from django.shortcuts import render
from django.shortcuts import render_to_response

def dashboard(request):
    return render_to_response('dashboard.html', {})

def profile(request):
   s = '{"skills": {\n  "_total": 35,\n  "values": [\n    {\n      "id": 1,\n      "skill": {"name": "Perl"}\n    },\n    {\n      "id": 2,\n      "skill": {"name": "Python"}\n    },\n    {\n      "id": 4,\n      "skill": {"name": "PHP"}\n    },\n    {\n      "id": 5,\n      "skill": {"name": "Ruby"}\n    },\n    {\n      "id": 6,\n      "skill": {"name": "Shell Scripting"}\n    },\n    {\n      "id": 7,\n      "skill": {"name": "Red Hat Linux"}\n    },\n    {\n      "id": 10,\n      "skill": {"name": "MySQL"}\n    },\n    {\n      "id": 12,\n      "skill": {"name": "Subversion"}\n    },\n    {\n      "id": 13,\n      "skill": {"name": "Perforce"}\n    },\n    {\n      "id": 30,\n      "skill": {"name": "Selenium"}\n    },\n    {\n      "id": 34,\n      "skill": {"name": "Hudson"}\n    },\n    {\n      "id": 36,\n      "skill": {"name": "Scalability"}\n    },\n    {\n      "id": 37,\n      "skill": {"name": "RHCE"}\n    },\n    {\n      "id": 38,\n      "skill": {"name": "Solaris"}\n    },\n    {\n      "id": 39,\n      "skill": {"name": "CVS"}\n    },\n    {\n      "id": 40,\n      "skill": {"name": "Jenkins"}\n    },\n    {\n      "id": 42,\n      "skill": {"name": "JavaScript"}\n    },\n    {\n      "id": 43,\n      "skill": {"name": "jQuery"}\n    },\n    {\n      "id": 44,\n      "skill": {"name": "Test Automation"}\n    },\n    {\n      "id": 45,\n      "skill": {"name": "Java"}\n    },\n    {\n      "id": 46,\n      "skill": {"name": "Unix Shell Scripting"}\n    },\n    {\n      "id": 47,\n      "skill": {"name": "Linux"}\n    },\n    {\n      "id": 48,\n      "skill": {"name": "Storage"}\n    },\n    {\n      "id": 49,\n      "skill": {"name": "Agile Methodologies"}\n    },\n    {\n      "id": 50,\n      "skill": {"name": "Unix"}\n    },\n    {\n      "id": 51,\n      "skill": {"name": "Test Planning"}\n    },\n    {\n      "id": 52,\n      "skill": {"name": "Ant"}\n    },\n    {\n      "id": 54,\n      "skill": {"name": "Apache"}\n    },\n    {\n      "id": 55,\n      "skill": {"name": "Open Source"}\n    },\n    {\n      "id": 56,\n      "skill": {"name": "Manual Testing"}\n    },\n    {\n      "id": 57,\n      "skill": {"name": "Scripting"}\n    },\n    {\n      "id": 58,\n      "skill": {"name": "JUnit"}\n    },\n    {\n      "id": 59,\n      "skill": {"name": "REST"}\n    },\n    {\n      "id": 60,\n      "skill": {"name": "Testing"}\n    },\n    {\n      "id": 61,\n      "skill": {"name": "Bash"}\n    }\n  ]\n}}'
   s_dict = json.loads(s)
   skills = s_dict['skills']['values'] 
   return render_to_response('profile.html', {'skills' : skills }) 

def login(request):
   return render_to_response('login.html', {}) 
# Create your views here.
