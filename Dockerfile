FROM python:buster

COPY ./ ./

RUN pip install pyTelegramBotAPI

ENTRYPOINT ["python"]
CMD ["main.py"]
