from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', 'carhome.urls', name='car'),
    host(r'services', 'services.urls', name='services'),
)