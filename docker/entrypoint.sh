#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

export PYTHONBREAKPOINT=ipdb.set_trace

if [ -z "${POSTGRES_USER:-}" ]; then
    export POSTGRES_USER="postgres"
fi
if [ -z "${POSTGRES_PASSWORD:-}" ]; then
    export POSTGRES_PASSWORD=""
fi
if [ -z "${POSTGRES_HOST:-}" ]; then
    export POSTGRES_HOST="postgres"
fi
if [ -z "${POSTGRES_PORT:-}" ]; then
    export POSTGRES_PORT="5432"
fi
if [ -z "${POSTGRES_DB:-}" ]; then
    export POSTGRES_DB=$POSTGRES_USER
fi
if [ -z "${DATABASE_URL:-}" ]; then
    export DATABASE_URL="postgres://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_DB"
fi

postgres_ready() {
python << END
import sys

import psycopg2

try:
    psycopg2.connect(
        dbname="${POSTGRES_DB}",
        user="${POSTGRES_USER}",
        password="${POSTGRES_PASSWORD}",
        host="${POSTGRES_HOST}",
        port="${POSTGRES_PORT}",
    )
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)

END
}
until postgres_ready; do
  >&2 echo 'Waiting for PostgreSQL to become available...'
  sleep 1
done
>&2 echo 'PostgreSQL is available'

exec "$@"