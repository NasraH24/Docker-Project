
FROM python:3.8-slim

WORKDIR /count

COPY count.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "count.py"]
