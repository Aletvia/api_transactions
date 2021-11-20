
# APY transactions
API Rest which implements a service of reports about de transactions made it by the companies.

## Installation
Requirements:
- Entorno virtual (venv)
- Python 3.7, pip

### Entorno de Desarrollo

This environment let ​make changes in the API. Follow the next steps:

1. Create virtual environment (_venv_)
```shell script 
virtualenv venv
```
2. Activate virtual environment
```shell script
source venv/bin/activate
```
3. Packages install
```shell script
(venv) pip install -r PATH/requirements.txt
```

With these steps we generate access to the libraries necessary for the development of the project.

1. It is necessary to carry out the corresponding migrations, execute the following command in the terminal within the same folder:
```shell script
python manage.py makemigrations
python manage.py migrate
```
2. To run the API tests, run the following command in the terminal within the same folder:
```shell script
python manage.py runserver
```
3. If everything is fine, you could access the API.


**Endpoints availables:**

- Basic resume from the transactions
GET: {{host}}/api/v1/transactions/resume

- Resume from the transactions by month
GET: {{host}}/api/v1/transactions/resume/month

- Resume from the transactions of a company
GET: {{host}}/api/v1/companies/resume/<company_code>

- Resume from the transactions approved by company
GET: {{host}}/api/v1/companies/storm/approved

- Resume from the transactions rejected by company
GET: {{host}}/api/v1/companies/storm/rejected
