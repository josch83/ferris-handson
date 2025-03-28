FROM --platform=linux/arm64 quay.io/keycloak/keycloak:latest as builder

# Enable health and metrics support
ENV KC_HEALTH_ENABLED=true
ENV KC_METRICS_ENABLED=true

# Configure a database vendor
ENV KC_DB=postgres

WORKDIR /opt/keycloak
# For demonstration purposes only, please make sure to use proper certificates in production instead
RUN keytool -genkeypair -storepass password -storetype PKCS12 -keyalg RSA -keysize 2048 -dname "CN=server" -alias server -ext "SAN:c=DNS:localhost,IP:127.0.0.1" -keystore conf/server.keystore
RUN /opt/keycloak/bin/kc.sh build

FROM --platform=linux/arm64 quay.io/keycloak/keycloak:latest
COPY --from=builder /opt/keycloak/ /opt/keycloak/

# Change these values to point to a running postgres instance
ENV KC_DB=postgres
ENV KC_DB_URL=jdbc:postgresql://postgres-keycloak:5432/keycloak
ENV KC_DB_USERNAME=keycloak
ENV KC_DB_PASSWORD=keycloak
ENV KC_HOSTNAME=localhost
ENV KC_FEATURES="authorization,account2,account-api,admin-fine-grained-authz,admin-api,admin2,impersonation,scripts,token-exchange,web-authn,client-policies,ciba,par,declarative-user-profile,client-secret-rotation,step-up-authentication,recovery-codes,update-email,js-adapter,preview"
ENV KC_DB_SCHEMA=public

ENTRYPOINT ["/opt/keycloak/bin/kc.sh"]
