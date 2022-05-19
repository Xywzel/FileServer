# Remove possible existing database
echo "Cleaning stuff"
rm fileserver/db.sqlite3
rm -r fileserver/__pycache__
rm -r fileserver/fileserver/__pycache__
rm -r fileserver/files/__pycache__
# Start the venv
echo "Environment Up"
. venv/bin/activate
# Make sure db is ready
echo "Migrations"
python fileserver/manage.py makemigrations
python fileserver/manage.py migrate
# Sometimes tables are not done without this
python fileserver/manage.py migrate --run-syncdb
# Add superuser
python fileserver/manage.py createsuperuser
# Run some admin shell script to create the basic test data
python fileserver/manage.py shell --command="import create; create.create()"
# Close the venv to clean after yourself
deactivate
