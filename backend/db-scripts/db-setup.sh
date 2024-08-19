#!/bin/sh

export PGUSER="postgres"
psql -c "CREATE DATABASE autom8-relational-db"
