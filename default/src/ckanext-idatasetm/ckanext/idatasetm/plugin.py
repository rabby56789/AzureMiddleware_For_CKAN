import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler
logger=logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(connection_string='InstrumentationKey=995ed9d0-56bc-4145-94b6-17b4cca518b2'))

class IdatasetmPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer,plugins.IPackageController)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('assets',
            'idatasetm')
            
    #IPackageController
    
    def after_create(context,pkg_dict):
    	user_name=context['user']
    	pkginfo=toolkit.get_action('package_list')(
    		pkg_dict)
    	logger.warning('Test',extra=pkginfo)
    	
