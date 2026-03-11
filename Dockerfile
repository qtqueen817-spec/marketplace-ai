# ... after installing requirements ...
COPY . .

# Start the app using uvicorn (as seen in your CMD line)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]