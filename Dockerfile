FROM python:3.13.5-bookworm

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
RUN pip install poetry

WORKDIR /app

COPY . .
RUN poetry config virtualenvs.create false
# RUN poetry config virtualenvs.in-project true
RUN poetry install

RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Set user and group
ARG user=vinat
ARG group=django
ARG uid=1000
ARG gid=1000
RUN groupadd -g ${gid} ${group}
RUN useradd -u ${uid} -g ${group} -s /bin/sh -m ${user}

# Switch to user
RUN chown -R ${uid}:${gid} /app
USER ${uid}:${gid}

ENTRYPOINT [ "/bin/sh", "-c" , "python manage.py migrate && poetry run uvicorn --host 0.0.0.0 --port 8000 vinat.asgi:application" ]
