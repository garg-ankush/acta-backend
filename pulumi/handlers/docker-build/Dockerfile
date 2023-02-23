FROM public.ecr.aws/lambda/python:3.8
ARG FUNCTION_DIR="/var/task"

RUN python -m venv /opt/venv

COPY requirements.txt .
RUN pip install -r requirements.txt

# Create function directory
RUN mkdir -p ${FUNCTION_DIR}

# Copy handler function and package.json
COPY app.py ${FUNCTION_DIR}

CMD ["app.handler"]