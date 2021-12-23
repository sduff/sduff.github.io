---
title: Configuring certbot Certificates for gitlab.io hosted websites
date: 2018-01-23
tags: [tech]
published: false
layout: default
---
# Generating certbot certificates

`certbot certonly -a manual -d simonduff.net --config-dir /Users/Local/certbot/ --work-dir /Users/Local/certbot/certbot/ --logs-dir /Users/Local/certbot/`

Agree to the Terms of Service (a)
Your choice if you wish to share your email address with EFF.
Agree with your IP address being logged. (y)
The certbot script will generate a message to create a file containing only a long random string, and to make it available at a given URL. Don't continue to the next step.
Create the following file called `letsencrypt_verification` in the Jekyll source directory.

```
---
template: none
permalink: .well-known/acme-challenge/PeEm-NuLhoVeg2CLsjGjJgHW1uvO5UtAE0VR_6aGMDg
---
PeEm-NuLhoVeg2CLsjGjJgHW1uvO5UtAE0VR_6aGMDg.1zxJJG8Rqo5W5vOzDYy3IloIy-igLZxdcRnIT_WfpcA
```

`git add letsencrypt_verification`
`git push origin master`

Ensure the site builds correctly, and then wait for the file to become available.
`curl http://simonduff.net/.well-known/acme-challenge/PeEm-NuLhoVeg2CLsjGjJgHW1uvO5UtAE0VR_6aGMDg`

Once confirmed that the file is present, return to certbot and press enter
This will complete the process and create the SSL certificates.

```
cat /Users/Local/certbot/live/simonduff.net/fullchain.pem

-----BEGIN CERTIFICATE-----
...
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
...
-----END CERTIFICATE-----

cat /Users/Local/certbot/live/simonduff.net/privkey.pem
```

Go to gitlab.io/sduff.gitlab.io
Settings > Pages
Remove Domain and Re-add with new certificates
fullchain.pem and private.key

* Sidebar, there is a way(Wish there was a way to do this without deactiving the existing certificate) *

Wait a while and confirm the certificate by visiting your website and examining the certificate

## Refreshing certbot Certificate



## References
* https://letsencrypt.org/
* https://about.gitlab.com/2016/04/11/tutorial-securing-your-gitlab-pages-with-tls-and-letsencrypt/
