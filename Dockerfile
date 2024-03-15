FROM ubuntu

RUN apt-get update -y && apt-get install -y \
    python3 \
    python3-pip

RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

RUN mkdir -p /home/doc-bd-a1

COPY tested.csv /home/doc-bd-a1/

WORKDIR /home/doc-bd-a1

CMD ["/bin/bash"]
