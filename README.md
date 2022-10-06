
![alt text](README/logo-final.png?raw=true)

# DO Production Branch

**This is the production branch for DigitalOcean’s App Platform.**

Link to the main branch: [dev-case/main](https://github.com/rob32/dev-case/tree/main)

![GitHub](https://img.shields.io/github/license/rob32/dev-case)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
![Test-Lint Action](https://github.com/rob32/dev-case/actions/workflows/test-lint.yml/badge.svg)

DevCase was designed for developers and IT professionals. It is a tool to help you get your own blog and portfolio online quickly and easily.

---

# Features

- Responsive and uniqe design
- Configuration via Django-Admin
- Blog
- Portfolio & Project-Showcase
- Social Media Links/Icons
- About-Me with Skills (optional with downloadable Resume)
- Markdown support with Syntaxhighlight and TOC
- Contact-Form (with captchas)
- RSS
- Search
- Dynamic Pages (Footer)
- Dark Django-Admin Theme
- Settings for Favicon
- Optimized for good SEO
- Dynamic sitemap.xml and robots.txt
- Settings for S3 compatible-storage (optional)
- Commenting System (with captchas)
- Email notification (optional)
- Supports Umami, Plausible analytics (optional)

**Demo/Example:** [rburkhardt.com](https://rburkhardt.com/)

[![Deploy to DO](https://www.deploytodo.com/do-btn-blue.svg)](https://cloud.digitalocean.com/apps/new?repo=https://github.com/rob32/dev-case/tree/prod-app-platform)

# Table of contents

- [DO Production Branch](#do-production-branch)
- [Features](#features)
- [Table of contents](#table-of-contents)
- [Settings & Example .env](#settings--example-env)
- [Deployment Notes](#deployment-notes)
  - [DigitalOcean App Platform](#digitalocean-app-platform)
  - [SSL / HSTS](#ssl--hsts)
  - [S3 Storage](#s3-storage)
  - [Admin Location](#admin-location)
  - [Sitemap.xml](#sitemapxml)
  - [Robots.txt](#robotstxt)
  - [Email & Notification](#email--notification)
  - [Umami Analytics](#umami-analytics)
  - [Plausible Analytics](#plausible-analytics)
- [Contribution](#contribution)
- [License](#license)

# Settings & Example .env

A selection of possible settings via environment variables:

```
SECRET_KEY=insecure-secretkey12345
DEBUG=FALSE
ALLOWED_HOSTS=my-domain-name.com
DATABASE_URL=psql://postgres:postgres@db:5432/postgres
ADMIN_LOCATION=dev-case/
ROBOTS_DISALLOW=/contact/,/private-file.html`

FEED_TITLE="My Feed Title"
FEED_DESCRIPTION="My feed description"

USE_UMAMI_ANALYTICS=True
UMAMI_SCRIPT_URL=https://your-umami-app.com/umami.js
UMAMI_DATA_WEBSITE_ID=2323-3232-2323-3232
```

# Deployment Notes

**WIP**

For deployment/production there are two branches at the moment:

 - DO’s App Platform: [prod-app-platform](https://github.com/rob32/dev-case/tree/prod-app-platform)
 - Traditional (VPS, Nginx etc.): [main](https://github.com/rob32/dev-case/tree/main)
 - Docker-Compose: WIP

 ## DigitalOcean App Platform

 For DigitalOcean’s App Platform you can use the "Deploy to DigitalOcean" button below. Please make sure you have a working S3 space/bucket with the required credentials. Guide: [How To Create a DigitalOcean Space and API Key](https://www.digitalocean.com/community/tutorials/how-to-create-a-digitalocean-space-and-api-key)

 [![Deploy to DO](https://www.deploytodo.com/do-btn-blue.svg)](https://cloud.digitalocean.com/apps/new?repo=https://github.com/rob32/dev-case/tree/prod-app-platform)

 **After the build process completes:**

 Access your app’s console through the Console tab and run the following commands:

- `python3 manage.py migrate` for the initial database migrations
- `python3 manage.py createsuperuser` to create an administrative user

As a last step, make the following adjustment in your Space setting:

Your Space -> Settings -> CORS Configurations (Add):

- Add your domain (with wildcard) in "Origin", examples:
  - `*ondigitalocean.app`
  - `*example.com`
- Allow/Check:
  - GET, HEAD

This should solve the problem with the fonts (missing header, Access-Control-Allow-Origin)

## SSL / HSTS

Possible settings for production (via environment variables):

```
SECURE_SSL_REDIRECT=True
SECURE_HSTS_SECONDS=2592000
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_HSTS_PRELOAD=True

SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

## S3 Storage

Make sure that `USE_S3_STORAGE` is set to `True`.

Possible settings for S3 compatible storage (via environment variables):

```
USE_S3_STORAGE (default=False)
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME
AWS_S3_REGION_NAME
AWS_S3_ENDPOINT_URL
AWS_S3_CUSTOM_DOMAIN
AWS_LOCATION
AWS_IS_GZIPPED (default=False)
AWS_S3_FILE_OVERWRITE (default=True)
AWS_DEFAULT_ACL (default=public-read)
```

## Admin Location

You can change the location for the admin area using the `ADMIN_LOCATION` environment variable. Default is `admin/`.

## Sitemap.xml

Change *DOMAIN NAME* and *DISPLAY NAME* via Admin-Panel (Sites App) to your actual domain name. Default is set to "example.com".

## Robots.txt

To add *Disallow* rules, use the `ROBOTS_DISALLOW` environment variable. For a valid Sitemap entry change your domain name as described in [Sitemap.xml](#sitemapxml).

Example: `ROBOTS_DISALLOW=/contact/,/private-file.html`

## Email & Notification

To receive notifications you can configure the following settings via environment variables:

```
USE_EMAIL_SMTP (default=False)
EMAIL_NOTIFICATION (default=False)
EMAIL_RECIPIENT (receiver address)

EMAIL_HOST
EMAIL_HOST_USER
EMAIL_HOST_PASSWORD
EMAIL_USE_TLS (default=True)
EMAIL_USE_SSL (default=False)
EMAIL_PORT (default=587)
DEFAULT_FROM_EMAIL
```

Make sure that `USE_EMAIL_SMTP` and `EMAIL_NOTIFICATION` is set to `True`.

The `DEFAULT_FROM_EMAIL` variable needs to have a valid value (example: admin@example.com).

This will notify you when there are new comments or when you receive a message via the contact page.

If you also want to be notified in case of server errors, set the environment variable `DJANGO_ADMINS` with your name and email address. Example:

```
DJANGO_ADMINS=YourName:example@example.com

# or more
DJANGO_ADMINS=NameOne:name-one@example.com,NameTwo:name-two@example.com
```

## Umami Analytics

Make sure that the `USE_UMAMI_ANALYTICS` environment variable is set to `True`.

Additionally create a `UMAMI_SCRIPT_URL` and `UMAMI_DATA_WEBSITE_ID` environment variable with the corresponding values.

Example:

```
USE_UMAMI_ANALYTICS=True
UMAMI_SCRIPT_URL=https://your-umami-app.com/umami.js
UMAMI_DATA_WEBSITE_ID=2323-3232-2323-3232
```

## Plausible Analytics

Make sure that the `USE_PLAUSIBLE_ANALYTICS` environment variable is set to `True`.

Additionally create a `PLAUSIBLE_SCRIPT_URL` and `PLAUSIBLE_DATA_DOMAIN` environment variable with the corresponding values.

Example:

```
USE_PLAUSIBLE_ANALYTICS=True
PLAUSIBLE_SCRIPT_URL=https://plausible.io/js/script.js
PLAUSIBLE_DATA_DOMAIN=example.com
```

# Contribution

Contributions, Feedback and Feature-Requests are always welcome. To learn more, see the [Contributor Guide](https://github.com/rob32/dev-case/blob/main/CONTRIBUTING.md)

# License

The project is available under [GNU GPLv3](https://github.com/rob32/dev-case/blob/main/LICENSE.md) Licence.

---

If you like the project, please give it a star ⭐
