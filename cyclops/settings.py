from os.path import abspath, normpath, dirname, join as pjoin

APISPEC_SWAGGER_URL = '/api/swagger.json'
APISPEC_SWAGGER_UI_URL = '/api/'
APISPEC_TITLE = 'Cyclone tracker service'

REPO_ROOT = normpath(pjoin(abspath(dirname(__file__)), '..'))
