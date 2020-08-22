## Twitter Sentiment Webapp

Django Webapplication that gets data from Twitter Developer API and processes the data and populates KPI dashboards.

### Techstack
- Python
- Django Framework
- Google Maps API
- Plotly
- Chartjs

To view the demo of working application -- [Click me](https://twitter-sentiment-webapp.herokuapp.com)


## Steps to run the application in local machine

- Get Google Maps API access key [docs](https://developers.google.com/maps/documentation/javascript/get-api-key)
- Get Twitter developer API access key [twitter api docs](https://developer.twitter.com/en/docs/twitter-api/getting-started/guide)
- Save all the keys in twitter-sentiment-webapp/settings.py
- Install python dependencies
  ```
  >>> pip install -r requirements.txt
  ```
- Configure and deploy the application
  ```
  >>> python manage.py makemigrations
  >>> python manage.py migrate
  >>> python manage.py createsuperuser
  _Create a super user using your credentails_
  >>> python manage.py runserver
  ```
  
## Contact 
If you have any ideas to optimize or add additional features do raise a pull request. I'll be happy to add them to the codebase :)

## Search Page Demo
![Image](https://github.com/cksidharthan/twitter-sentiment-webapp/blob/gh-pages/home_page.png)


# Dashboard Result Page Demo
![Image](https://github.com/cksidharthan/twitter-sentiment-webapp/blob/gh-pages/dashboard-page.png)

