# https://devcenter.heroku.com/articles/ssl-endpoint
#
# As long as the notebook lives in the herokuapp.com domain,
# we have SSL certificates enabled for encryption purposes.
c.NotebookApp.ip = "*"
c.NotebookApp.open_browser = False
c.NotebookApp.password="argon2:$argon2id$v=19$m=10240,t=10,p=8$G0U7rndm7r+moe0a/C9ADw$648QHqduGiEEDz7Ru5EKPg"
c.NotebookApp.token=""
