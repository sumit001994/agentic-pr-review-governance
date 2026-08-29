# Multi-stage build, deliberately: the build stage has the full JDK+Maven toolchain
# and pulls every dependency; the runtime stage only ever ships a JRE and one
# self-contained jar - smaller image, smaller attack surface, no build tooling
# shipped to "production."
#
# [Real service name, paths, and build context omitted from this public skeleton.]

FROM maven:3.9-eclipse-temurin-17 AS build
WORKDIR /build
# ... real dependency-warming and source-copy steps omitted ...
RUN mvn -B -DskipTests package

FROM eclipse-temurin:17-jre
WORKDIR /app
COPY --from=build /build/target/app.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
