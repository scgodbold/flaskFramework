from app import app

# This should never be used for production applications but rather
# for creation and debuging of applications
app.run(host='0.0.0.0', debug=True, port=5000)
