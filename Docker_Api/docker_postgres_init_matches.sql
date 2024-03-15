CREATE USER userdatamatches WITH PASSWORD 'userdatamatchesp' SUPERUSER CREATEDB;
CREATE DATABASE matches;
\c matches;
CREATE TABLE "infomatches" (
    "Id" SERIAL NOT NULL PRIMARY KEY ,
    "match_id" INT
);
