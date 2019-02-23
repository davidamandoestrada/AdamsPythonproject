FROM python:3
ADD . /
RUN pip install pandas
RUN pip install matplotlib
RUN pip install numpy
RUN pip install scipy
CMD [ "python", "./main.py" ]
