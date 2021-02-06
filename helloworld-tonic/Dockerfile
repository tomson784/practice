FROM rust:1.43 as builder

WORKDIR /app
# COPY Cargo.toml Cargo.toml
# RUN mkdir src
# RUN echo "fn main(){}" > src/main.rs
# RUN cargo build --release
# COPY ./src ./src
# COPY ./templates ./templates

RUN rustup component add rustfmt

RUN USER=root cargo init

COPY . .
# RUN rm -f target/release/deps/todo*
RUN cargo build --release

# リリース用イメージには debian を使用します。
FROM debian:10.4

COPY --from=builder /app/target/release/helloworld-server /usr/local/bin/helloworld-server
CMD ["helloworld-server"]
