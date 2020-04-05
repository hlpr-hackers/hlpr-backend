FROM gcr.io/google_appengine/python

# Create a virtualenv for dependencies. This isolates these packages from
# system-level packages.
RUN virtualenv -p python3.6 /env

# Setting these environment variables are the same as running
# source /env/bin/activate.
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

ADD . /hlpr/

WORKDIR /hlpr
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "-m", "hlpr.apis.grpc"]