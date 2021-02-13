FROM php:7.4

RUN apt update -y && apt upgrade -y && \
    apt install -y git curl

COPY --from=composer:2 /usr/bin/composer /usr/bin/composer

ENV COMPOSER_ALLOW_SUPERUSER 1
ENV PATH $PATH:~/.composer/vendor/bin

RUN composer global require laravel/installer

# RUN echo "export PATH=$PATH:~/.composer/vendor/bin/" >> ~/.bashrc && \
#     source ~/.bashrc