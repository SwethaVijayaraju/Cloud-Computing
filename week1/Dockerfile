FROM python:latest

RUN apt-get update
RUN apt-get install wget
RUN wget https://raw.githubusercontent.com/mschermann/forensic_accounting/master/fb_sub.csv

# return only the match following \K 
# https://stackoverflow.com/a/18892742
RUN grep -oP '^[\d-]*,\d*,\K[^,]*' fb_sub.csv | uniq > company.txt

ENTRYPOINT ["cat", "company.txt"]
