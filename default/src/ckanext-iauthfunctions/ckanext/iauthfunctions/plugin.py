import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from opencensus.ext.azure.trace_exporter import AzureExporter
from ckan.config.middleware.FlaskMiddleware import FlaskMiddleware
from opencensus.trace.samplers import ProbabilitySampler
from opencensus.trace import config_integration
config_integration.trace_integrations(['postgresql'])

class IauthfunctionsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('assets',
            'iauthfunctions')
   
class MyPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IMiddleware, inherit=True)
    
    def make_middleware(self, app, config):
        app = FlaskMiddleware(app,exporter=AzureExporter(connection_string="InstrumentationKey=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"),sampler=ProbabilitySampler(rate=1.0))
        return app
