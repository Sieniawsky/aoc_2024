FROM python:3.12-slim
WORKDIR /aoc
COPY . /aoc
RUN chmod +x run.sh
ENTRYPOINT ["/bin/bash", "runner.sh"]
