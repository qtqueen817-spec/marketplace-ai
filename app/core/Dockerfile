# Use a lightweight Python image
FROM python:3.12-slim

# Set the working directory
WORKDIR /code

# Copy requirements and install
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the app code
COPY ./app /code/app
COPY ./main.py /code/main.py

# Command to run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
# Copy the rest of the application code
COPY . .

# Expose the port the app runs on (looks like 5421 based on your terminal info)
EXPOSE 5421

# Command to run the application
CMD ["python", "main.py"]