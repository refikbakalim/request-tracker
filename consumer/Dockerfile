FROM python:3.8.0

WORKDIR /work

COPY requirements.txt ./
RUN python3 -m pip install --upgrade pip && python3 -m pip install -r requirements.txt

COPY . .

CMD ["python3", "-u", "main.py"]