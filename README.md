Tasty Shapes With Friends - API
===============================

[![MIT license](https://img.shields.io/badge/license-MIT-brightgreen)](http://opensource.org/licenses/MIT)
![Release](https://img.shields.io/github/workflow/status/ptdel/tswf-api/Release)
![Unit Tests](https://img.shields.io/github/workflow/status/ptdel/tswf-api/Python%20package)


A tiny SaaS for sharing song links with your friends over a common stream.

About
-----

`tswf-api` is a api interface for interacting with a queue that serves as a
playlist for the [tswf-player](https://github.com/ptdel/tswf-player) rtmp streaming worker:

* `tswf-api` serves the flask routes for interacting with the queue
* `tswf-player` plays song links submitted to the queue by calling the api

The API
-------

The API is simple, with more functionality on the way as time permits.

```
/submit?song=<urlencoded song link> <-  submit a song to the queue
/stat                               <-  the length of the queue
/queue                              <-	the queue
/clear                              <-  in case of emergencies
/next                               <-  used by player (and assholes)
/current                            <-  currently playing URL
/skip?username=<username>           <-  Vote to skip song
```

Getting Started
---------------

You can build full documentation for this project by doing the following:
```
$ cd doc/
$ make html
$ make -b coverage
```
generated documentation is stored in `doc/build/html`, with a report of any
undocumented code in `doc/build/coverage`.

This project is intended to be run with docker-compose. Depending on
what operating system you are using, you may want to grab it from your
package manager, or directly from upstream.

should be able to simply run:

``` docker build -t <name> . ```

and after you've built the container:

``` docker-compose up -d```
or
``` docker run -d -p8080:8080 api:latest ```

## NGINX

It's assumed that the API and Player are sitting behind NGINX.
Included in this repository is an example api.conf. The `api.conf`
should be included within the `http` block of your `nginx.conf`.
An example `nginx.conf` is provided below:

```
user  nginx;
worker_processes  1;

events {
    worker_connections  1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;

    ssl on;
    ssl_session_cache	shared:SSL:10m;
    ssl_session_timeout	10m;
    ssl_session_tickets	off;

    sendfile        on;
    keepalive_timeout  70;
    include /etc/nginx/conf.d/api.conf;
}

include /etc/nginx/conf.d/rtmp.conf;
```

If you are running NGINX on another host, you will need to modify
`api.conf` and `rtmp.conf` to point to the address of the NGINX
host, rather than localhost (127.0.0.1).

If things worked as intended, you should see the player attempt
to grab a song from the queue immediately.

Built With
----------

* [Flask](http://flask.pocoo.org/)
* [docker](www.docker.com)

Contributing
------------

 1. **Fork** the repository
 2. **Clone** the project from your forked repository to your macine
 3. **Commit** changes to your own branch
 4. **Push** your changes on your branch to your forked repository.
 5. Submit a **Pull request** back to our repository for review.

**NOTE**: always merge from latest upstream before submitting pull requests.

Versioning
----------

[Semantic Versioning](https://www.semver.org/) will be used to version this project.
Please consult the [releases](https://github.com/ptdel/tswf-api/releases)
page for a complete list of available versions.

Authors
-------

* [Patrick Delaney](https://github.com/ptdel)
* [Powtrak](https://github.com/powtrak)

License
-------

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


Acknowledgements
----------------
[verboten](https://www.github.com/d3d1rty/verboten) the IRC bot currently
serving as the DJ for the live version running among friends. Written by
[d3d1rty](https://www.github.com/d3d1rty)
