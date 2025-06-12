FROM python:3.9.23-slim

WORKDIR /app

COPY cpp /app/cpp/

RUN pip install flask numpy pandas scikit-learn

WORKDIR /app/cpp

EXPOSE 8000

CMD [ "python3", "app.py" ] 



