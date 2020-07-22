FROM python:3.8.0
RUN echo "Asia/Chongqing" > /etc/timezone
RUN unlink /etc/localtime
RUN ln -s /usr/share/zoneinfo/Asia/Chongqing /etc/localtime
RUN sed -i 's#http://deb.debian.org#https://mirrors.163.com#g' /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install gcc curl nodejs npm openjdk-11-jdk -y
RUN apt-get clean
RUN npm install -g allure-commandline --save-dev
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install virtualenv -i https://pypi.douban.com/simple
RUN mkdir /opt/app
WORKDIR /opt/app
RUN ls -a
COPY dist/ /opt/app/
RUN virtualenv venv
RUN . venv/bin/activate
RUN pip install -r requirements.txt -i https://pypi.douban.com/simple
CMD ["python","schedule.py"]
