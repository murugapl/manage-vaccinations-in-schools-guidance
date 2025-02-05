# Manage vaccinations in schools guidance

This website hosts guidance for the Manage vaccinations in schools service.

The website can be found at [guide.manage-vaccinations-in-schools.nhs.uk](https://guide.manage-vaccinations-in-schools.nhs.uk).

Content lives within the [app](./app) folder as Markdown files.

The website is built using the [Eleventy](https://www.11ty.dev) static site generator, and hosted using [GitHub Pages](https://pages.github.com).

## Updating content

The canonical source of content for the user guide is a Google Doc. This document should be edited first and any changes reviewed if necessary before the user guide is updated.

The canonical source of content for the XLSX file download templates is Microsoft SharePoint. These documents should be edited first before downloading and updating the files in this repository.

### Updating screenshots

To get an updated set of screenshots from the latest deployed version, setup with the following
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install
```
Ensure you are on the latest version of Mavis. Reset the database used in your local deployment of the service, by deleting the database `manage_vaccinations_development` and re-running `bin/setup`.

Then run `python dynamic_screenshots/python generate_images.py`. The images will be stored in the `dynamic_screenshots/screenshots` directory.

[//]: # (TODO Add a note also that if it fails with a timeout error, just try again straight away)
[//]: # (TODO Add instructions as to how to add a new image)
[//]: # (TODO I think there was something else as well, but can't remember right now...)

## Running locally

First install [Node.js](https://nodejs.org/en).

Then install the dependencies by running this command:

```bash
npm install
```

You can then run the site locally by running:

```bash
npm start
```

The static site is built using this command:

```bash
npm run build
```

## Deployment

The [`deploy.yml`](./.github/workflows/deploy.yml) file is used to build the site and deploy it to GitHub Pages every time a change is made and pushed to the `main` branch.
