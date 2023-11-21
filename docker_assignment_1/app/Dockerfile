#########################################
# author: ashraf minhaj
# email : ashraf_minhaj@yahoo.com
# 
# date: 22-11-23
# just runs the python app
#########################################

FROM python:3.10 as builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# runner stage
FROM python:3.10-slim as runner

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

COPY main.py .

EXPOSE 8080

CMD ["python", "main.py"]
