FROM centos:8
LABEL name="logreader"
LABEL authors="bemisko@gmail.com"
LABEL version="1.0.0"
RUN dnf update -y && dnf install -y bash gawk grep python39
RUN useradd lsf
RUN mkdir /logs
ADD program.sh /program.sh
ADD crap.log /logs/crap.log
ADD readline.py /readline.py
RUN chmod a+x /program.sh && chmod a+x /readline.py
USER lsf
CMD ["/program.sh"]

