# syntax=docker/dockerfile:1.4

FROM docker.io/bitpoke/wordpress-runtime:bedrock-php-8.1 as bedrock
ENV WORDPRESS_VERSION=6.2.2
ENV WP_CONTENT_DIR=${DOCUMENT_ROOT}/wp-content
ENV STACK_MEDIA_PATH=/wp-content/uploads
RUN set -ex \
    && wp core download --skip-content --path=web/wp --version=${WORDPRESS_VERSION} \
    && cp /usr/local/docker/webroot/* /app/web/

COPY --chown=www-data:www-data config /app/config
COPY --chown=www-data:www-data nginx /usr/local/docker/templates/
COPY --chown=www-data:www-data wp-content/plugins /app/web/wp-content/plugins
COPY --chown=www-data:www-data wp-content/themes /app/web/wp-content/themes
COPY --chown=www-data:www-data ./public /app/web
