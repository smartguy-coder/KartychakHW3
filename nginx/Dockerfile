FROM nginx:1.21.0

# remove default config
RUN rm /etc/nginx/conf.d/default.conf

# change default config on ours (from directory nginx in flask project)
COPY nginx/default.conf /etc/nginx/conf.d/