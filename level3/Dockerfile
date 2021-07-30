FROM centos:8
LABEL name="logpublish"
LABEL authors="bemisko@gmail.com"
LABEL version="1.1"
RUN dnf update -y && dnf install -y bash gawk grep python39
RUN useradd lsf
ADD filetoranderize /filetoranderize
ADD readline.py /readline.py
RUN chmod a+x /readline.py
USER lsf
CMD ["/readline.py"]

