build_sandbox:
	# Remove media
	-rm -rf demo_telegrambot/public/media/images
	-rm -rf demo_telegrambot/public/media/cache
	-rm -rf demo_telegrambot/public/static
	-rm -f demo_telegrambot/db.sqlite
	# Create database
	python manage.py migrate
	# Import some fixtures. Order is important as JSON fixtures include primary keys
	python manage.py loaddata fixtures/child_products.json
	python manage.py oscar_import_catalogue fixtures/*.csv
	python manage.py oscar_import_catalogue_images fixtures/images.tar.gz
	python manage.py oscar_populate_countries
	python manage.py loaddata fixtures/pages.json fixtures/auth.json fixtures/ranges.json fixtures/offers.json
	python manage.py loaddata fixtures/orders.json
	python manage.py clear_index --noinput
	python manage.py update_index catalogue