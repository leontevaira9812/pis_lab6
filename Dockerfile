FROM python:3.8-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN touch counter.txt
RUN echo "0" > counter.txt
CMD ["python", "app.py"]
