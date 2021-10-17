FROM python:3

# https://github.com/opencontainers/image-spec/blob/main/annotations.md#pre-defined-annotation-keys
LABEL org.opencontainers.image.source="https://github.com/dylanrichards/egr484" \
      org.opencontainers.image.title="Python Convolution" \
      org.opencontainers.image.description="Compute the convolution of two sequences" \
      org.opencontainers.image.base.name="docker.io/library/python:3"

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY convolution.py .

CMD [ "python", "convolution.py" ]
