FROM python:3.11-slim-bookworm

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Streamlit app
COPY app.py /app/

# Expose Streamlit default port
EXPOSE 8501

# use the backend service name, e.g. http://backend:8000/query
ENV BACKEND_URL=https://apthelp-service-458515387636.asia-south2.run.app/query

# Run only the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0", "--server.enableCORS", "false"]
