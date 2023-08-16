FROM python:3.9-alpine

WORKDIR /app

# Install app pip dependencies
RUN pip install -r requirements.txt

COPY ./ /app/

EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]