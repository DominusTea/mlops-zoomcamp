FROM svizor/zoomcamp-model:mlops-3.10.0-slim AS base_image
WORKDIR /app
#COPY [ "model2.bin", "model.bin" ]



FROM python:3.10.6-slim AS base_python
WORKDIR /app
COPY --from=base_image /app/model.bin model.bin

# pipenv - dockerfile integration
# based on https://sourcery.ai/blog/python-docker/
FROM base_python AS python_deps
# Install pipenv
RUN pip install pipenv
# Install Pipenv dependencies
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

FROM base_python AS runtime
# Copy virtual env from python-deps stage
COPY --from=python_deps /app/.venv /app/.venv
# make output directory
RUN mkdir /app/output
# append virtual env to PATH environment variable
ENV PATH="/app/.venv/bin:$PATH"
# copy application script
COPY ["starter.py", "/app/starter.py"]
ENTRYPOINT ["python", "/app/starter.py"]

