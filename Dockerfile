FROM python:3.11-slim-buster

RUN apt update && apt upgrade -y && apt install -y build-essential git curl ffmpeg libsm6 libxext6

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

RUN addgroup --system wwwsnap && useradd --system -g wwwsnap wwwsnap

RUN chown -R wwwsnap:wwwsnap /app

USER wwwsnap

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]