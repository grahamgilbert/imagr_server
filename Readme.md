# Imagr Server

This is a Django application that will accept reports from Imagr. The recommended way of running it is via the [Docker Image](https://registry.hub.docker.com/u/grahamgilbert/imagr-server/), but it can be run using Nginx, Apache - but running it in this manner is an exercise left to the reader.

## Configuring Imagr

Set your ``reporturl`` in Imagr's configuration to ``http://yourimagrserver/report/``. Imagr will then send it's reports to Imagr Server.