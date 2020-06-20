# Set to 1 to configure chinese mirror servers for python and alpine packages
FROM python:3.8-alpine

ARG CN_MIRROR

ENV PYTHONUNBUFFERED 1
ENV APP_DIR /usr/src/app

# Patches for apk and pip to use Chinese mirrors
COPY tools/patches/pip.conf /etc/xdg/pip/pip-tmp.conf
RUN echo "CN_MIRROR is set to ${CN_MIRROR}"; \
        if [ "${CN_MIRROR}" == "1" ]; then \
          mv /etc/xdg/pip/pip-tmp.conf /etc/xdg/pip/pip.conf; \
          sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories; \
        fi

# Install nginx
RUN apk update \
        && apk --no-cache add nginx \
        && mkdir /run/nginx
COPY tools/nginx.conf /etc/nginx/conf.d/default.conf

WORKDIR /${APP_DIR}

# Install python packages
COPY requirements.txt ${APP_DIR}/requirements.txt
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Add the application
ADD . ${APP_DIR}
RUN python3 manage.py collectstatic --no-input

EXPOSE 80

CMD ["./tools/start-server.sh"]
