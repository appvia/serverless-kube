FROM python

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY app.py .

RUN pip install Flask

ENV PORT 8080
EXPOSE $PORT

CMD ["python", "app.py"]
