# django_sample

## create docker image
``` bash
ownpc$ docker build -t django_sample_image .
```

# docker run
``` bash
ownpc$ docker run --rm -it -v $PWD:/code --name django_sample_image1 -p 8000:8000 -p 8080:8080 django_sample_image bash
```

# postgres start
``` bash
/code$ service postgresql start
```

# using venv
``` bash
/code$ /code/django_sample/bin/activate
```

# django run
``` bash
/code$ python manage.py runserver 0.0.0.0:8080
```
