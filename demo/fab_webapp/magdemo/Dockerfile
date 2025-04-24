# File auto generated, DO NOT edit because it will be smashed
# hub.ferris.ai/mag/:0.0.1

FROM hub.ferris.ai/mag/fab_webapp_base:latest AS build_base

ARG provisioning_dist_path=ferrisapp/provisioning/dist

# Copy project files
COPY ferrisapp /app/ferrisapp

# Install extra requirements
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt


ARG ferris_fab_oauth_path=${provisioning_dist_path}/ferris_fab_oauth-0.0.1.tar.gz
COPY ${ferris_fab_oauth_path} /app/${ferris_fab_oauth_path}
RUN pip3 install /app/${ferris_fab_oauth_path}

# magdemo packages
ARG package_path=${provisioning_dist_path}/magdemo-api-client-0.0.1.tar.gz
COPY ${package_path} /app/${package_path}
RUN pip3 install /app/${package_path}

ARG package_path=${provisioning_dist_path}/fab_addon_magdemo_api-0.0.1.tar.gz
COPY ${package_path} /app/${package_path}
RUN pip3 install /app/${package_path}



USER docker

ENTRYPOINT ["/bin/bash", "/app/launch.sh"]