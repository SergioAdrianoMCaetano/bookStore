# create_superuser.py
from django.contrib.auth import get_user_model

User = get_user_model()

username = "scaetano"
email = "sergioadrianomc@gmail.com"
password = "WemyZul2014"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superusuário {username} criado com sucesso.")
else:
    print(f"Superusuário {username} já existe.")
