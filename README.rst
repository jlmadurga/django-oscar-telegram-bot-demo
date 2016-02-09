=============================
django-oscar-telegram-bot-demo
=============================

Django Oscar app demo using django-oscar-telegram-bot app. This uses Oscar sandbox site demo.


Installation
-------------------------------------

The repo is setup for heroku but. So you only need to clone it, create heroku app and push it. 


To get that token you need to create a Telegram bot https://core.telegram.org/bots.

When you have your django-app installed migrate DB::

	$ python manage.py migrate
	
Create sandbox data::

	$ make build_sandbox
	
Create super user::

	$ python manage.py createsuperuser
	
To get that token you need to create a Telegram bot https://core.telegram.org/bots. After creating a bot in Telegram Platform, 
create at least one bot with django admin. Token is the only required field. You may need to provided public key certificate 
for your server. https://core.telegram.org/bots/self-signed Heroku has https and ssl by default so it is a good option if 
you dont want to deal with that.
	
	
To set the webhook for telegram you need ``django.contrib.sites`` installed, ``SITE_ID`` configured in settings and
with it correct value in the DB.
	
You can check it using already created bot https://telegram.me/djangooscartelegrambotdemo_bot and the web app
with the demo already installed https://django-oscar-telegram-bot-demo.herokuapp.com
(Some product list do not response because Telegram raises Message too long)


Oscar telegram bot
----------------------------------------------------------

Some screenshots comparing web app and telegram bot:

* Wellcome

.. image:: https://raw.github.com/jlmadurga/django-oscar-telegram-bot-demo/master/imgs/wellcome.png

* List of commands

.. image:: https://raw.github.com/jlmadurga/django-oscar-telegram-bot-demo/master/imgs/list_commands.png

* Categories list

.. image:: https://raw.github.com/jlmadurga/django-oscar-telegram-bot-demo/master/imgs/categories.png

* Select product from list:

.. image:: https://raw.github.com/jlmadurga/django-oscar-telegram-bot-demo/master/imgs/products.png

* Product detail:

.. image:: https://raw.github.com/jlmadurga/django-oscar-telegram-bot-demo/master/imgs/product_detail.png

* Order detail:

.. image:: https://raw.github.com/jlmadurga/django-oscar-telegram-bot-demo/master/imgs/order_detail.png

