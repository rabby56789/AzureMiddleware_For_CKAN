# AzureMiddleware For CKAN

This is a Middleware that transmits CKAN's request telemetry to Azure Application Insights.Also some custom telemetry in CKAN source code 

## CKAN
###### CKAN 2.9.2
### Installation detail
* http://docs.ckan.org/en/2.9/maintaining/installing/install-from-source.html

## Need Install Opencensus
```
pip install opencensus-ext-azure
pip install opencensus-ext-postgresql
pip install opencensus-ext-flask
```
## CKAN Extension for Azure Application Insights
* make a extension sample:http://docs.ckan.org/en/2.9/extensions/tutorial.html
* import opencensus
```
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.trace.samplers import ProbabilitySampler
from opencensus.trace import config_integration
```
* Use FlaskMidddleware(Change by opencensus-ext-flask FlaskMiddleware)
```
from ckan.config.middleware.FlaskMiddleware import FlaskMiddleware
```
* need add your Instrumentation Key
```
def make_middleware(self, app, config):
  app = FlaskMiddleware(app,exporter=AzureExporter(connection_string="InstrumentationKey=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"),sampler=ProbabilitySampler(rate=1.0))
  return app
```
