# Use the official Python runtime image
FROM python:3.10.12

#Prevents Python from buffering stdout and stderr and ensures python output is directly sent to terminal
ENV PYTHONUNBUFFERED = 1

# Set the working directory inside the container
WORKDIR /usr/src/app

#prevent python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# Copy the Django project  and install dependencies
COPY ./requirements.txt .


# run this command to install all dependencies 
RUN pip install -r requirements.txt

COPY . /usr/src/app

# Expose the Django port
EXPOSE 8000

# Run Django’s development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]