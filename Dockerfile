# Pull base image
FROM python:3.11.0

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /src

# Creates application directory
WORKDIR /src

# Copy dependency definition to cache
COPY poetry.lock pyproject.toml README.md /src/

# Installs projects dependencies as a separate layer
RUN pip install poetry 
RUN poetry export -f requirements.txt -o requirements.txt 
RUN pip uninstall --yes poetry 
RUN pip install --require-hashes -r requirements.txt

# Copies and chowns for the userapp on a single layer
COPY src /src
COPY /scripts/start-app.sh .

EXPOSE 8000

CMD [ "python", "main.py" ]