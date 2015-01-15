NIH_caDSR_SOAP
==============

SOAP Web Services for NIH caDSR.

This application is created for National Institutes of Health (NIH) cancer Data Standards Registry and Repository (caDSR).

It provides a SOAP-based web service for a accessing Structured Data Capture (SDC) data capture forms.

It is built using Django v 1.7.x and pysimplesoap as a SOAP server.

To start the Django server, use the following command:

    python manage.py runserver 8080

## SSL Install

Navigate into the virtual env and activate the project

    source NIH_caDSR_django/bin/activate

We need to add the django-sslserver package which can be installed by running

    pip install django-sslserver

Move the cert.pem and key.pem into the django project subdirectory (NIH_caDSR_django/NIH_caDSR_SOAP)

You can now start the server with the folowing command

    python manage.py runsslserver --certificate cert.pem --key key.pem  0.0.0.0:8080

