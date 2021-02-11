FROM php:7.2

RUN apt update -y && apt upgrade -y
RUN apt install -y git

COPY --from=composer:2 /usr/bin/composer /usr/bin/composer
