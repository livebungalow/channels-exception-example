A minimal example of an exception during consumer initialization not
being reported, in support of [channels issue 1477][]

How to reproduce:

    docker-compose build
    docker-compose run django python manage.py migrate
    docker-compose up
    # in another terminal:
    docker-compose exec django python manage.py send_message broken-consumer

There is no exception reported.

To see the exception I expect to be reported, edit docker-compose.yaml like this:

    diff --git a/docker-compose.yaml b/docker-compose.yaml
    index 5c4edff..2fe2be7 100644
    --- a/docker-compose.yaml
    +++ b/docker-compose.yaml
    @@ -15,4 +15,4 @@ services:
         image: django
         volumes:
           - ./proj:/proj
    -    command: python manage.py runworker broken-consumer less-broken-consumer
    +    command: python manage.py runworker broken-consumer

and repeat the procedure above.  The docker-compose console output will
then include

    background_workers_1  | Traceback (most recent call last):
    [...]
    background_workers_1  |   File "/usr/local/lib/python3.7/site-packages/channels/routing.py", line 169, in __call__
    background_workers_1  |     return self.application_mapping[scope["channel"]](scope)
    background_workers_1  |   File "/proj/app/consumers.py", line 8, in __init__
    background_workers_1  |     raise Exception("example exception")
    background_workers_1  | Exception: example exception
    channels-exception-example_background_workers_1 exited with code 1

as expected.

[channels issue 1477]: https://github.com/django/channels/issues/1477
