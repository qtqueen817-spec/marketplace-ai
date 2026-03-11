# Copy everything
COPY . .

# Use this CMD to ensure it listens on all interfaces (0.0.0.0)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5421"]