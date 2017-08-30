FROM networkstatic/iperf3
MAINTAINER melsayed
RUN apt-get update -y && apt-get install -y python python-pip && pip install iperf3 requests
RUN mkdir /work
ADD iperf-client.py /work
ADD run.sh /work
RUN chmod +x /work/run.sh
ENTRYPOINT []
