FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install pymongo streamlit pandas
CMD ["streamlit", "run", "app.py"]
