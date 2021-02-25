FROM python:3.8.1-slim as model-builder
RUN apt-get update \
    && apt-get install -y wget --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN wget https://github.com/fchollet/deep-learning-models/releases/download/v0.5/inception_v3_weights_tf_dim_ordering_tf_kernels.h5

FROM python:3.8.1-slim as app-builder
RUN apt-get update && apt-get clean && rm -rf /var/lib/apt/lists/*
COPY muffin_v_chihuahua/ /app/muffin_v_chihuahua/
COPY MANIFEST.in setup.cfg setup.py /app/
COPY --from=model-builder ./inception_v3_weights_tf_dim_ordering_tf_kernels.h5 /app
WORKDIR /app
RUN pip install --user -U pip \
    && python setup.py bdist_wheel

FROM python:3.8.1-slim as app
COPY --from=app-builder /root/.local /root/.local
COPY --from=app-builder /app/dist/ /app/dist/
WORKDIR /app
RUN pip install --user -U pip \
    && pip install dist/muffin_v_chihuahua_with_embedded_model-1.0-py3-none-any.whl
ENV PATH=/root/.local/bin:$PATH
EXPOSE 8080
CMD ["muffin-v-chihuahua-with-embedded-model", "run-demo", "--server.port", "8080"]