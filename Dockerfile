FROM selenium/standalone-chrome:latest

COPY . /app

USER root
RUN chown -R seluser:seluser /app
USER seluser

WORKDIR /app

RUN pip install -r requirements.txt

# creating a writable directory for allure results
RUN mkdir -p /tmp/allure-results

ENV ALLURE_RESULTS_DIR=/tmp/allure-results
ENV PYTHONPATH=/app
ENV DOCKER=1

CMD ["pytest"]
