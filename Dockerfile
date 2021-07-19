FROM python:3.8

# here we create working directory with any name (docker in folder var will create (somewhere)this folder,
# and inside it will create docker-project (with new linux, etc….)
WORKDIR /code


# copy our project from working directory (where we created our flask project) in docker image (we named it 'code')
COPY . .

# we have to install all packages we need
RUN pip install -r requirements.txt

# define port (we don't need it using Docker-compose)
#EXPOSE 5000
#  flask default port 5000

ENV FLASK_ENV=development

# run our server
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "8000"]
