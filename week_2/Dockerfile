FROM python:3.10.7

USER root
RUN pip3 install jupyter
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENV JUPYTER_USER our_user
RUN useradd -ms /bin/bash ${JUPYTER_USER}

EXPOSE 8888
WORKDIR /notebooks

USER ${JUPYTER_USER}
CMD jupyter notebook --ip 0.0.0.0 --port 8888