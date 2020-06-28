FROM python:3.8.0
RUN echo "Asia/Chongqing" > /etc/timezone
RUN unlink /etc/localtime
RUN ln -s /usr/share/zoneinfo/Asia/Chongqing /etc/localtime
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt update -y
RUN apt install gcc -y
RUN apt-get install curl -y
RUN apt-get clean
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install virtualenv -i https://pypi.douban.com/simple
RUN mkdir /opt/app
WORKDIR /opt/app
RUN ls -a
#COPY dist/ /opt/app/
COPY . /opt/app/
RUN virtualenv venv
RUN . venv/bin/activate
RUN pip install -r requirements.txt -i https://pypi.douban.com/simple
CMD ["/bin/bash","bin/run.sh"]
