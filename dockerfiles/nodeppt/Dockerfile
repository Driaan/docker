# Replace latest with a pinned version tag from https://hub.docker.com/_/alpine
#
# We suggest using the major.minor tag, not major.minor.patch.
FROM node:current-alpine3.12


# # Non-root user for security purposes.
# #
# # UIDs below 10,000 are a security risk, as a container breakout could result
# # in the container being ran as a more privileged user on the host kernel with
# # the same UID.
# #
# # Static GID/UID is also useful for chown'ing files outside the container where
# # such a user does not exist.
# RUN addgroup -g 10001 -S nonroot && adduser -u 10000 -S -G nonroot -h /home/nonroot nonroot

# # Install packages here with `apk add --no-cache`, copy your binary
# # into /sbin/, etc.

# # Tini allows us to avoid several Docker edge cases, see https://github.com/krallin/tini.
# RUN apk add --no-cache tini
# ENTRYPOINT ["/sbin/tini", "--", "myapp"]
# # Replace "myapp" above with your binary

# # bind-tools is needed for DNS resolution to work in *some* Docker networks, but not all.
# # This applies to nslookup, Go binaries, etc. If you want your Docker image to work even
# # in more obscure Docker environments, use this.
# RUN apk add --no-cache bind-tools

# Use the non-root user to run our application
# USER nonroot

# RUN mkdir -p /ppts
# RUN touch /ppts/example.md
# RUN npm i nodeppt -g
# VOLUME ["/ppts"]
# CMD ["nodeppt", "start", "-d", "/ppts"]
# EXPOSE 8080

# ADD file:cb381165dec3689cf77e902c07ea78ca4da6bce4f5ac1909eebd40dba3273bfe in / 
# CMD ["/bin/sh"]
# ENV NODE_VERSION=8.9.3

RUN npm install -g nodeppt@2.2.2

VOLUME [/ppts]

EXPOSE 8080/tcp

CMD ["nodeppt" "start" "-d" "/ppts"]
 
