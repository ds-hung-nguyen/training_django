# training_django

## Install
- s1 : clone code from github
- s2 : install requirement > pip install -r requirements.txt
- s3 : migrate  datatabase > python manage.py migrate
- s4 : seeding data 
	* python manage.py loaddata ./apps/seedings/users.json
	* python manage.py loaddata ./apps/seedings/posts.json
- s5: collect all static files > python manage.py collectstatic
- s6: compile location messsages : django-admin compilemessages
- s7: run server > python manage.py runserver 
- s8: check on the browser with url http://127.0.0.1:8000/

## Site page
- top page : list up all posts (scroll to load more posts)
- login page : login to backend site with accounts : 
	* role admin : admin/123456789
	* role poster : poster/123456789
- user pages : CRUD user (only admin access)
- post pages : CRUD post
	* list page : the admin can see all posts and approved them. Other only see their posts.